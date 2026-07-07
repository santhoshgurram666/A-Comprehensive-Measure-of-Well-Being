Phase 3: Project Design
1. System Architecture

The application follows a Client-Server Architecture:

Client Side (Frontend): Developed using HTML, CSS, and Bootstrap. It provides an interactive web interface where users can enter the required Human Development indicators and view prediction results.

Server Side (Backend): A Python Flask application (app.py) processes user requests, validates the input values, performs necessary preprocessing, and sends the data to the trained Machine Learning model.

Machine Learning Model: A trained and serialized Machine Learning model (hdi_model.pkl) is loaded into memory by the Flask application. The model predicts the HDI Score and classifies it into one of the four categories: Very High, High, Medium, or Low Human Development.

2. Directory Structure Strategy

To ensure smooth development and deployment, the project follows a well-organized directory structure. Core files such as app.py, requirements.txt, and the models folder remain in the root directory to support deployment on cloud platforms like Render or Heroku.

HDI_Prediction_System/
│
├── Dataset/
│   └── Human Development Index.csv
│
├── models/
│   └── hdi_model.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   ├── home.html
│   └── result.html
│
├── app.py
├── requirements.txt
└── README.md
3. Database Schema (Conceptual ER Diagram)
Entity Name	Attributes	Description
Users	UserID (PK), Name, Email, Password	Stores user information for future authentication.
HDI_Data	DataID (PK), UserID (FK), LifeExpectancy, MeanYearsSchooling, ExpectedYearsSchooling, GNI_PerCapita	Stores the input values entered by users.
ML_Model	ModelID (PK), ModelName, Algorithm, Accuracy, ModelFile	Stores information about the trained Machine Learning model.
Prediction_Result	PredictionID (PK), DataID (FK), ModelID (FK), HDI_Score, HDI_Category, PredictionDate	Stores the predicted HDI score and development category.
4. UI/UX Design Flow

Home Page: Displays an introduction to the Human Development Index Prediction System with a button to start prediction.

Input Form: Provides a user-friendly form where users enter the following values:

Life Expectancy
Mean Years of Schooling
Expected Years of Schooling
GNI per Capita (PPP)

Prediction Page: The system processes the input using the trained Machine Learning model.

Result Page: Displays the predicted HDI Score, HDI Category (Very High, High, Medium, or Low), and a brief explanation of the country's development status.

This follows the same format as your sample while being customized for your Human Development Index (HDI) Prediction System.
