

Uploading vid.mp4…

# Breast Cancer Recurrence Prediction

This project is a Django-based web application designed to predict the recurrence of breast cancer based on patient-provided clinical data. The application utilizes a trained Support Vector Classifier (SVC) model to classify whether a recurrence is likely. The goal is to assist healthcare professionals by providing a data-driven prediction.

---

## Features

- **Interactive User Interface**: A form to input patient data such as age, menopausal status, tumor size, tumor grade, and hormonal therapy details.
- **Machine Learning-Powered Predictions**: Leverages a trained Support Vector Classifier (SVC) model to predict recurrence.
- **Error Handling**: Includes a custom-styled 404 error page for invalid URLs.
- **Preprocessing and Scaling**: Data preprocessing steps ensure compatibility with the trained model for accurate predictions.
- **Scalable Design**: Modular codebase to add more features or integrate with external systems easily.

---

## How It Works

1. **Input**: User provides details like age, menopausal status, tumor characteristics, and hormonal therapy information.
2. **Preprocessing**: Data is normalized using a `scaler.pkl` file, ensuring the format matches the training dataset.
3. **Prediction**: The `svc_model.pkl` predicts the recurrence status using the input data.
4. **Output**: Displays a message indicating whether the patient is likely to experience a recurrence or not.

---

## Requirements

The following dependencies are required to run the application:

- Python 3.8+
- Django 4.2+
- Pandas
- Joblib
- Scikit-learn

Ensure you have these installed on your system.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YourGitHubUsername/breast-cancer-recurrence.git
cd breast-cancer-recurrence
