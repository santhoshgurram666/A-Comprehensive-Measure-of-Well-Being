Phase 5: Project Development
1. Overview

The Project Development phase involved implementing the Human Development Index (HDI) Prediction System by integrating data preprocessing, machine learning model development, backend functionality, and a user-friendly web interface. The application was built using Python and Flask, enabling users to predict the Human Development Index category based on key socio-economic indicators.

2. Key Components Developed
Data Engineering (Dataset/ & src/prepare_dataset.py)

The HDI dataset was cleaned and preprocessed using Python. Missing values were handled, unnecessary columns were removed, and the required features were selected. The dataset was then split into training and testing datasets for machine learning.

Model Training (src/train_model.py)

This module implements the Machine Learning training pipeline. It reads the preprocessed HDI dataset, trains the selected regression model, evaluates its performance, and saves the trained model as models/hdi_model.pkl using Pickle for future predictions.

The Application Core (src/app.py)

The Flask framework serves as the backend of the application.

Receives user input through the web form.
Validates and preprocesses the entered values.
Converts the input into the format required by the Machine Learning model.
Loads the trained hdi_model.pkl file.
Predicts the HDI Score and determines the corresponding HDI Category (Very High, High, Medium, or Low).
Sends the prediction results back to the user interface.
Frontend (templates/ & static/)

The frontend was developed using HTML5 and CSS3 to provide a clean and responsive user interface.

Home Page: Introduces the HDI Prediction System.
Input Page: Allows users to enter:
Life Expectancy
Mean Years of Schooling
Expected Years of Schooling
Gross National Income (GNI) per Capita (PPP)
Result Page: Displays the predicted HDI Score, HDI Category, and a brief explanation of the country's development level.

The frontend communicates seamlessly with the Flask backend to provide instant prediction results.
