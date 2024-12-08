from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import joblib,os
import pandas as pd

from breastCancer import settings

@csrf_exempt
def index(request):
    

    context = {}

    if request.method == "POST":
        patient_data = {
            "Age": int(request.POST['Age']),
            "MenopausalStatus": request.POST['MenopausalStatus'],
            "TumorSize": int(request.POST['TumorSize']),
            "TumorGrade": request.POST['TumorGrade'],
            "NodesPositive": int(request.POST['NodesPositive']),
            "ProgesteroneReceptor": int(request.POST['ProgesteroneReceptor']),
            "EstrogenReceptor": int(request.POST['EstrogenReceptor']),
            "HormonalTherapy": request.POST['HormonalTherapy'],
            "rfstime": request.POST['rfstime']
        }
        context = preprocess(patient_data)
        return render(request, "index.html", context)

    elif request.method == "GET":
        context = {'prediction':''}
        return render(request, "index.html",context)

 
def preprocess(patient_data):
    scaler_path = os.path.join(settings.BASE_DIR, 'home', 'scaler.pkl')
    model_path = os.path.join(settings.BASE_DIR, 'home', 'svc_model.pkl')
    
    if patient_data['MenopausalStatus'] == 'Premenopausal':
        patient_data['MenopausalStatus'] = 0
    else:
        patient_data['MenopausalStatus'] = 1

    if patient_data['TumorGrade'] == 'T1':
        patient_data['TumorGrade'] = 1
    elif patient_data['TumorGrade'] == 'T2':
        patient_data['TumorGrade'] = 2
    else:
        patient_data['TumorGrade'] = 3

    if patient_data['HormonalTherapy'] == 'No':
        patient_data['HormonalTherapy'] = 0
    else:
        patient_data['HormonalTherapy'] = 1

    patient_data = {
        "Age": [patient_data['Age']],
        "MenopausalStatus": [patient_data['MenopausalStatus']],
        "TumorSize": [patient_data['TumorSize']],
        "TumorGrade": [patient_data['TumorGrade']],
        "NodesPositive": [patient_data['NodesPositive']],
        "ProgesteroneReceptor": [patient_data['ProgesteroneReceptor']],
        "EstrogenReceptor": [patient_data['EstrogenReceptor']],
        "HormonalTherapy": [patient_data['HormonalTherapy']],
        "rfstime": [patient_data['rfstime']]
    }
    patient_data_df = pd.DataFrame(patient_data)

    try:
        scaler = joblib.load(scaler_path)
        model = joblib.load(model_path)

        transformed_values = scaler.transform(patient_data_df)
        single_prediction = model.predict(transformed_values)

        if single_prediction[0] == 0:
            prediction = "Predicted status: No Recurrence"
        else:
            prediction = "Predicted status: Recurrence"
        return {"prediction": prediction}

    except FileNotFoundError:
        print("Scaler or model file not found.")
        return {"error": "Model files not found. Please contact support."}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred during prediction."}

def custom_404(request, exception):
    print("Custom 404 handler triggered.")
    return render(request, "404.html", status=404)