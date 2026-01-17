LOAN APPROVAL PREDICTION

This project is part of my data science portfolio. It uses machine learning to predict loan approval and includes a web application for real-time predictions. After testing 3 different algorithms, the best accuracy on the leaderboard was achieved by Logistic Regression (78.47%), followed by RandomForest (77.78%), while Decision Tree performed the worst (64.58%).



PROJECT OVERVIEW


This project covers the entire machine learning pipeline:

1. Problem Statement
2. Hypothesis Generation
3. Data Collection
4. Exploratory Data Analysis (EDA)
5. Data Pre-processing
6. Model Development and Evaluation
7. Web Application Deployment



PROBLEM STATEMENT


BUSINESS PROBLEM

Dream Housing Finance company deals in all home loans. They have presence across all urban, semi urban and rural areas. Customer first apply for home loan after that company validates the customer eligibility for loan. Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others. To automate this process, they have given a problem to identify the customers segments, those are eligible for loan amount so that they can specifically target these customers.

Loan prediction is a very common real-life problem that every retail bank faces in their lending operations. If the loan approval process is automated, it can save a lot of man hours and improve the speed of service to the customers. The increase in customer satisfaction and savings in operational costs are significant. However, the benefits can only be reaped if the bank has a robust model to accurately predict which customer's loan it should approve and which to reject, in order to minimize the risk of loan default.

ML PROBLEM FORMULATION

This is a classification problem where we have to predict whether a loan will be approved or not. Specifically, it is a binary classification problem where we have to predict either one of the two classes given i.e. approved (1) or not approved (0). The dependent variable or target variable is the Loan_Status, while the rest are independent variables or features. We need to develop a model using the features to predict the target variable.


KEY FEATURES

KEY FEATURES

Trained Logistic Regression Model with 78.47% accuracy
Flask Web Application with interactive form interface
Real-time Loan Prediction using trained ML pipeline
Automatic Data Preprocessing with StandardScaler and OneHotEncoder
Production-Ready with scikit-learn 1.7.0
Easy-to-use HTML and CSS frontend


TECHNOLOGY STACK

Machine Learning: scikit-learn, Logistic Regression, Pandas, NumPy
Backend Framework: Flask
Frontend: HTML, CSS
Data Visualization: Matplotlib, Seaborn
Model Storage: Pickle files (.pkl)
Development Environment: Jupyter Notebook


HOW IT WORKS

1. User fills the loan application form on the web interface
2. Flask backend receives the form data
3. Data is preprocessed (scaled and encoded) using the saved pipeline
4. Logistic Regression model makes the prediction
5. Result (Approved or Rejected) is displayed to the user



INSTALLATION


PREREQUISITES

Python 3.7 or higher
pip package manager
Git


STEP 1: CLONE REPOSITORY

git clone https://github.com/edimekalajayakrishna/Loan-Approval-Prediction.git
cd Loan-Approval-Prediction


STEP 2: CREATE VIRTUAL ENVIRONMENT

python -m venv venv


STEP 3: ACTIVATE VIRTUAL ENVIRONMENT

Windows:
.\venv\Scripts\Activate.ps1

Mac/Linux:
source venv/bin/activate


STEP 4: INSTALL DEPENDENCIES

pip install -r requirements.txt




USAGE


STEP 1: RUN THE FLASK APPLICATION

python app.py


STEP 2: ACCESS THE WEB APPLICATION

Open your browser and go to http://127.0.0.1:5000


STEP 3: FILL LOAN DETAILS

Enter the required information:

- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term (in months)
- Credit History
- Gender
- Marital Status
- Dependents
- Education
- Self Employed Status
- Property Area


STEP 4: GET PREDICTION

Click Submit button to get the loan approval prediction (Approved or Rejected)



MODEL PERFORMANCE


ALGORITHM COMPARISON RESULTS

Logistic Regression: 78.47% accuracy (SELECTED)
Random Forest: 77.78% accuracy
Decision Tree: 64.58% accuracy

Logistic Regression was selected for deployment due to superior accuracy and model simplicity.


DATASET INFORMATION

Training Data: trainloan.csv
Test Data: testloan.csv


NUMERIC FEATURES

ApplicantIncome
CoapplicantIncome
LoanAmount
Loan_Amount_Term
Credit_History


CATEGORICAL FEATURES

Gender
Married
Dependents
Education
Self_Employed
Property_Area


TARGET VARIABLE

Loan_Status (1 = Approved, 0 = Rejected)


TROUBLESHOOTING

ISSUE: InconsistentVersionWarning from scikit-learn

Error Message: "Trying to unpickle estimator from version 1.7.0 when using version 1.8.0"

Solution: Ensure scikit-learn version 1.7.0 is installed
pip install scikit-learn==1.7.0


ISSUE: Flask not found

Error Message: "No module named 'flask'"

Solution: Activate virtual environment and install dependencies
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt


ISSUE: Port 5000 already in use

Error Message: "Address already in use"

Solution: Change port in app.py line 87
Modification: app.run(debug=True, port=5001)


ISSUE: Model file not found

Error Message: "FileNotFoundError: loan_pipeline.pkl"

Solution: Ensure loan_pipeline.pkl and feature_columns.pkl are in the project root directory


MODEL RETRAINING

To retrain the model with new data:

1. Update trainloan.csv and testloan.csv with new data

2. Open loanprediction.ipynb in Jupyter Notebook
   jupyter notebook loanprediction.ipynb

3. Run all cells in sequence

4. The .pkl files will be regenerated with the new model

5. The Flask app will automatically use the updated model


PROJECT FILES

app.py                      Main Flask application
loanprediction.ipynb        Jupyter Notebook for model training
trainloan.csv               Training dataset
testloan.csv                Test dataset
loan_pipeline.pkl           Trained ML model and preprocessor
feature_columns.pkl         Expected feature column names
requirements.txt            Python dependencies
.gitignore                  Git ignore patterns
README.md                   This file
templates/index.html        Web form interface
static/style.css            CSS styling


LICENSE

This project is open source and available for educational purposes.


AUTHOR

Jaya Krishna
GitHub: https://github.com/edimekalajayakrishna

Portfolio: This project is part of a data science portfolio demonstrating machine learning model development, data preprocessing, model evaluation, and web application deployment.


SUPPORT

For issues, questions, or suggestions, please open a GitHub issue in the repository.

For bug reports, please include:
- Error message and traceback
- Python and scikit-learn versions
- Operating system
- Steps to reproduce the issue


ACKNOWLEDGMENTS

Analytics Vidhya: For the original hackathon and dataset
scikit-learn: For the machine learning library
Flask: For the web framework
