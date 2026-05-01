# Explainable Water Quality Prediction System

## Introduction

This project presents a machine learning-based system to predict water quality (Safe/Unsafe) using physicochemical parameters.
The system is enhanced with explainable AI to provide reasoning behind predictions and suggestions for improvement.

This work contributes to **Sustainable Development Goal 6 (Clean Water and Sanitation)** by enabling easy and accessible water safety analysis.

---

## Project Overview

The system uses a Support Vector Machine (SVM) model trained on water quality data to classify water samples as safe or unsafe.
It considers parameters such as pH, hardness, dissolved solids, turbidity, and chemical concentrations.

In addition to prediction, the system:

* Explains why water is unsafe
* Identifies problematic parameters
* Suggests improvements

---

## Features

* Machine Learning-based prediction (SVM)
* Explainable AI (reason for prediction)
* Recommendation system
* Flask web application
* REST API endpoint for prediction

---

## Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* Joblib
* Google Gemini API (for explanation)

---

## Application Deployment

The application is deployed locally using Flask.
Users can enter water parameters through a web interface and receive predictions along with explanations.

---

## How to Run the Application

1. Clone the repository:

```
git clone https://github.com/madhavkmohan003/Explainable-Water-Quality-Prediction.git
```

2. Navigate to project directory:

```
cd repo-name
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the Flask app:

```
python app.py
```

5. Open browser:

```
http://127.0.0.1:5000/
```

---

## Usage

* Enter water quality parameters
* Click Predict
* View prediction (Safe/Unsafe)
* Read explanation and suggestions

---

## API Endpoint

### POST /predict

Example request:

```
{
  "ph": 7,
  "hardness": 100,
  "solids": 500,
  "chloramines": 7,
  "sulfate": 300,
  "conductivity": 400,
  "organicCarbon": 10,
  "trihalomethanes": 50,
  "turbidity": 3
}
```

---

## Screenshots

(Add your UI screenshots here after uploading)

---

## Acknowledgement

This project is adapted from an open-source repository:

https://github.com/mallikarjun25/Water-Quality-Prediction

Licensed under MIT License.

Modifications include:

* Explainable AI integration
* Flask-based UI
* Improved prediction system

---

## Author

Madhav K Mohan
SRM Institute of Science and Technology

---