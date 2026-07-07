Phase 6: Project Testing
1. Testing Strategy

Ensuring the reliability and accuracy of the Human Development Index (HDI) Prediction System involved multiple levels of testing, including dataset validation, Machine Learning model evaluation, backend verification, and user interface testing. The system was tested to ensure accurate predictions, fast response time, and a smooth user experience.

2. Model Evaluation (Machine Learning Testing)

The Machine Learning model was evaluated using a standard 80:20 train-test split. Different performance metrics were used to assess the model's prediction capability.

Evaluation Metrics:

R² Score
Mean Absolute Error (MAE)
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)

Model Performance:

The selected Machine Learning model achieved high prediction accuracy (approximately 95% or above) on the testing dataset.
The trained model successfully predicted the HDI Score and correctly classified countries into Very High, High, Medium, and Low Human Development categories.
The model was tested using various combinations of life expectancy, education, and income values to ensure reliable predictions.
3. Application Testing (Software Engineering)
Unit Testing: Individual functions in train_model.py and app.py were tested to ensure correct preprocessing, feature handling, and prediction generation.
Integration Testing: Verified that the Flask application successfully loaded the hdi_model.pkl file and correctly processed user inputs to generate HDI predictions.
Functional Testing: Confirmed that users could enter valid values for Life Expectancy, Mean Years of Schooling, Expected Years of Schooling, and GNI per Capita, and receive the correct HDI Score and category.
UI/UX Testing: Tested the web interface on different screen sizes to ensure responsive design. Input validation was also verified to prevent invalid or non-numeric entries.
Performance Testing: Ensured that prediction results were generated within 2 seconds and that the application remained stable during repeated prediction requests.
Deployment Testing: Verified that the application functioned correctly after deployment on the cloud platform (Render), with successful model loading and prediction generation.
