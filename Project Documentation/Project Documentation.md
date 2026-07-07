Phase 7: Project Documentation
1. System Overview

The Human Development Index (HDI) Prediction System is a Machine Learning-based web application that predicts a country's Human Development Index (HDI) score and classifies it into one of four categories: Very High, High, Medium, or Low Human Development. The application uses socio-economic indicators such as Life Expectancy, Mean Years of Schooling, Expected Years of Schooling, and Gross National Income (GNI) per Capita (PPP). This documentation serves as a guide for both end-users and future developers.

2. End-User Manual
How to Use the Application
Navigate to the deployed web application URL.
On the home page, open the HDI Prediction form.
Enter the required development indicators:
Life Expectancy: Average life expectancy at birth (years).
Mean Years of Schooling: Average years of education completed.
Expected Years of Schooling: Expected years of education for a child entering school.
Gross National Income (GNI) per Capita (PPP): Income per person in PPP (US Dollars).
Click the Predict button.
The system will display:
Predicted HDI Score
HDI Category (Very High, High, Medium, or Low)
A brief explanation of the country's development level
3. Developer Guide
Local Environment Setup

To run this project locally, ensure that Python 3.x is installed.

# Install project dependencies
pip install -r requirements.txt

# (Optional) Retrain the model if the dataset is updated
python src/train_model.py

# Start the Flask application
python src/app.py

Access the application using:

http://localhost:5000
Modifying the Machine Learning Model

To replace or retrain the existing Machine Learning model:

Update the training code in src/train_model.py.
Train the new model using the updated dataset.
Save the trained model as models/hdi_model.pkl.
Ensure the model loading path in src/app.py points to the updated .pkl file.
Restart the Flask application and verify that predictions are generated correctly.
Project Structure
HDI_Prediction_System/
│
├── Dataset/
│   └── Human Development Index.csv
├── models/
│   └── hdi_model.pkl
├── src/
│   ├── prepare_dataset.py
│   ├── train_model.py
│   ├── data_analysis.py
│   └── app.py
├── templates/
│   ├── home.html
│   └── indexnew.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md

This documentation follows the same format as your sample while being fully customized for your Human Development Index (HDI) Prediction System.
