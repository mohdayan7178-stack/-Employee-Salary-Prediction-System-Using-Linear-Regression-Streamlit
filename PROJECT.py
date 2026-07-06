import pandas as pd
import numpy as np
import joblib
import os
import sys

def load_model():
    """Load the model, scaler, and model columns"""
    try:
        model = joblib.load('salary_prediction_model.joblib')
        scaler = joblib.load('scaler.joblib')
        model_columns = joblib.load('model_columns.joblib')
        return model, scaler, model_columns
    except FileNotFoundError:
        print("Error: Model files not found. Please ensure the following files exist:")
        print("- salary_prediction_model.joblib")
        print("- scaler.joblib")
        print("- model_columns.joblib")
        sys.exit(1)

def get_manual_input():
    """Get user input manually through the command line"""
    print("\n=== Employee Details ===")
    
    # Categorical Inputs
    department = input('Department (Sales, Research & Development, Human Resources): ')
    while department not in ['Sales', 'Research & Development', 'Human Resources']:
        print("Invalid department. Please choose from the options.")
        department = input('Department (Sales, Research & Development, Human Resources): ')
    
    education_field = input('Education Field (Life Sciences, Medical, Marketing, Technical Degree, Human Resources, Other): ')
    while education_field not in ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources', 'Other']:
        print("Invalid education field. Please choose from the options.")
        education_field = input('Education Field (Life Sciences, Medical, Marketing, Technical Degree, Human Resources, Other): ')
    
    job_role = input('Job Role (Sales Executive, Research Scientist, Laboratory Technician, Manufacturing Director, Healthcare Representative, Manager, Sales Representative, Research Director, Human Resources): ')
    while job_role not in ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources']:
        print("Invalid job role. Please choose from the options.")
        job_role = input('Job Role (Sales Executive, Research Scientist, Laboratory Technician, Manufacturing Director, Healthcare Representative, Manager, Sales Representative, Research Director, Human Resources): ')
    
    gender = input('Gender (Male, Female): ')
    while gender not in ['Male', 'Female']:
        print("Invalid gender. Please choose from the options.")
        gender = input('Gender (Male, Female): ')
    
    marital_status = input('Marital Status (Single, Married, Divorced): ')
    while marital_status not in ['Single', 'Married', 'Divorced']:
        print("Invalid marital status. Please choose from the options.")
        marital_status = input('Marital Status (Single, Married, Divorced): ')
    
    overtime = input('OverTime (No, Yes): ')
    while overtime not in ['No', 'Yes']:
        print("Invalid overtime option. Please choose from the options.")
        overtime = input('OverTime (No, Yes): ')
    
    business_travel = input('Business Travel (Travel_Rarely, Travel_Frequently, Non-Travel): ')
    while business_travel not in ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel']:
        print("Invalid business travel option. Please choose from the options.")
        business_travel = input('Business Travel (Travel_Rarely, Travel_Frequently, Non-Travel): ')

    # Numerical Inputs
    try:
        age = int(input('Age (18-60): '))
        while not 18 <= age <= 60:
            print("Age must be between 18 and 60.")
            age = int(input('Age (18-60): '))
            
        distance_from_home = int(input('Distance From Home (km, 1-29): '))
        while not 1 <= distance_from_home <= 29:
            print("Distance must be between 1 and 29.")
            distance_from_home = int(input('Distance From Home (km, 1-29): '))
            
        education = int(input('Education Level (1-5): '))
        while not 1 <= education <= 5:
            print("Education level must be between 1 and 5.")
            education = int(input('Education Level (1-5): '))
            
        environment_satisfaction = int(input('Environment Satisfaction (1-4): '))
        while not 1 <= environment_satisfaction <= 4:
            print("Environment satisfaction must be between 1 and 4.")
            environment_satisfaction = int(input('Environment Satisfaction (1-4): '))
            
        job_involvement = int(input('Job Involvement (1-4): '))
        while not 1 <= job_involvement <= 4:
            print("Job involvement must be between 1 and 4.")
            job_involvement = int(input('Job Involvement (1-4): '))
            
        job_level = int(input('Job Level (1-5): '))
        while not 1 <= job_level <= 5:
            print("Job level must be between 1 and 5.")
            job_level = int(input('Job Level (1-5): '))
            
        num_companies_worked = int(input('Number of Companies Worked For (0-9): '))
        while not 0 <= num_companies_worked <= 9:
            print("Number of companies must be between 0 and 9.")
            num_companies_worked = int(input('Number of Companies Worked For (0-9): '))
            
        percent_salary_hike = int(input('Percent Salary Hike (%) (11-25): '))
        while not 11 <= percent_salary_hike <= 25:
            print("Percent salary hike must be between 11 and 25.")
            percent_salary_hike = int(input('Percent Salary Hike (%) (11-25): '))
            
        performance_rating = int(input('Performance Rating (1-4): '))
        while not 1 <= performance_rating <= 4:
            print("Performance rating must be between 1 and 4.")
            performance_rating = int(input('Performance Rating (1-4): '))
            
        relationship_satisfaction = int(input('Relationship Satisfaction (1-4): '))
        while not 1 <= relationship_satisfaction <= 4:
            print("Relationship satisfaction must be between 1 and 4.")
            relationship_satisfaction = int(input('Relationship Satisfaction (1-4): '))
            
        total_working_years = int(input('Total Working Years (0-40): '))
        while not 0 <= total_working_years <= 40:
            print("Total working years must be between 0 and 40.")
            total_working_years = int(input('Total Working Years (0-40): '))
            
        work_life_balance = int(input('Work Life Balance (1-4): '))
        while not 1 <= work_life_balance <= 4:
            print("Work life balance must be between 1 and 4.")
            work_life_balance = int(input('Work Life Balance (1-4): '))
            
        years_at_company = int(input('Years at Company (0-40): '))
        while not 0 <= years_at_company <= 40:
            print("Years at company must be between 0 and 40.")
            years_at_company = int(input('Years at Company (0-40): '))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

    data = {
        'Age': age, 'DistanceFromHome': distance_from_home, 'Education': education,
        'EnvironmentSatisfaction': environment_satisfaction, 'JobInvolvement': job_involvement,
        'JobLevel': job_level, 'NumCompaniesWorked': num_companies_worked,
        'PercentSalaryHike': percent_salary_hike, 'PerformanceRating': performance_rating,
        'RelationshipSatisfaction': relationship_satisfaction, 'TotalWorkingYears': total_working_years,
        'WorkLifeBalance': work_life_balance, 'YearsAtCompany': years_at_company,
        'BusinessTravel_Travel_Frequently': 1 if business_travel == 'Travel_Frequently' else 0,
        'BusinessTravel_Travel_Rarely': 1 if business_travel == 'Travel_Rarely' else 0,
        'Department_Research & Development': 1 if department == 'Research & Development' else 0,
        'Department_Sales': 1 if department == 'Sales' else 0,
        'EducationField_Human Resources': 1 if education_field == 'Human Resources' else 0,
        'EducationField_Life Sciences': 1 if education_field == 'Life Sciences' else 0,
        'EducationField_Marketing': 1 if education_field == 'Marketing' else 0,
        'EducationField_Medical': 1 if education_field == 'Medical' else 0,
        'EducationField_Other': 1 if education_field == 'Other' else 0,
        'EducationField_Technical Degree': 1 if education_field == 'Technical Degree' else 0,
        'Gender_Male': 1 if gender == 'Male' else 0,
        'JobRole_Human Resources': 1 if job_role == 'Human Resources' else 0,
        'JobRole_Laboratory Technician': 1 if job_role == 'Laboratory Technician' else 0,
        'JobRole_Manager': 1 if job_role == 'Manager' else 0,
        'JobRole_Manufacturing Director': 1 if job_role == 'Manufacturing Director' else 0,
        'JobRole_Research Director': 1 if job_role == 'Research Director' else 0,
        'JobRole_Research Scientist': 1 if job_role == 'Research Scientist' else 0,
        'JobRole_Sales Executive': 1 if job_role == 'Sales Executive' else 0,
        'JobRole_Sales Representative': 1 if job_role == 'Sales Representative' else 0,
        'MaritalStatus_Married': 1 if marital_status == 'Married' else 0,
        'MaritalStatus_Single': 1 if marital_status == 'Single' else 0,
        'OverTime_Yes': 1 if overtime == 'Yes' else 0,
    }
    features = pd.DataFrame(data, index=[0])
    return features

def process_csv(file_path):
    """Process a CSV file with employee data"""
    try:
        df = pd.read_csv(file_path)
        print(f"\nSuccessfully loaded CSV with {len(df)} records.")
        print("First 5 rows:")
        print(df.head())
        
        # Check if required columns are present
        required_columns = [
            'Age', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction', 
            'JobInvolvement', 'JobLevel', 'NumCompaniesWorked', 'PercentSalaryHike',
            'PerformanceRating', 'RelationshipSatisfaction', 'TotalWorkingYears',
            'WorkLifeBalance', 'YearsAtCompany', 'BusinessTravel', 'Department',
            'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime'
        ]
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Error: CSV file is missing required columns: {missing_columns}")
            return None
        
        # Process categorical variables
        df_processed = pd.DataFrame()
        
        # Copy numerical columns
        numerical_columns = [
            'Age', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction', 
            'JobInvolvement', 'JobLevel', 'NumCompaniesWorked', 'PercentSalaryHike',
            'PerformanceRating', 'RelationshipSatisfaction', 'TotalWorkingYears',
            'WorkLifeBalance', 'YearsAtCompany'
        ]
        for col in numerical_columns:
            df_processed[col] = df[col]
        
        # One-hot encode categorical variables
        df_processed['BusinessTravel_Travel_Frequently'] = (df['BusinessTravel'] == 'Travel_Frequently').astype(int)
        df_processed['BusinessTravel_Travel_Rarely'] = (df['BusinessTravel'] == 'Travel_Rarely').astype(int)
        
        df_processed['Department_Research & Development'] = (df['Department'] == 'Research & Development').astype(int)
        df_processed['Department_Sales'] = (df['Department'] == 'Sales').astype(int)
        
        df_processed['EducationField_Human Resources'] = (df['EducationField'] == 'Human Resources').astype(int)
        df_processed['EducationField_Life Sciences'] = (df['EducationField'] == 'Life Sciences').astype(int)
        df_processed['EducationField_Marketing'] = (df['EducationField'] == 'Marketing').astype(int)
        df_processed['EducationField_Medical'] = (df['EducationField'] == 'Medical').astype(int)
        df_processed['EducationField_Other'] = (df['EducationField'] == 'Other').astype(int)
        df_processed['EducationField_Technical Degree'] = (df['EducationField'] == 'Technical Degree').astype(int)
        
        df_processed['Gender_Male'] = (df['Gender'] == 'Male').astype(int)
        
        df_processed['JobRole_Human Resources'] = (df['JobRole'] == 'Human Resources').astype(int)
        df_processed['JobRole_Laboratory Technician'] = (df['JobRole'] == 'Laboratory Technician').astype(int)
        df_processed['JobRole_Manager'] = (df['JobRole'] == 'Manager').astype(int)
        df_processed['JobRole_Manufacturing Director'] = (df['JobRole'] == 'Manufacturing Director').astype(int)
        df_processed['JobRole_Research Director'] = (df['JobRole'] == 'Research Director').astype(int)
        df_processed['JobRole_Research Scientist'] = (df['JobRole'] == 'Research Scientist').astype(int)
        df_processed['JobRole_Sales Executive'] = (df['JobRole'] == 'Sales Executive').astype(int)
        df_processed['JobRole_Sales Representative'] = (df['JobRole'] == 'Sales Representative').astype(int)
        
        df_processed['MaritalStatus_Married'] = (df['MaritalStatus'] == 'Married').astype(int)
        df_processed['MaritalStatus_Single'] = (df['MaritalStatus'] == 'Single').astype(int)
        
        df_processed['OverTime_Yes'] = (df['OverTime'] == 'Yes').astype(int)
        
        return df_processed
    except Exception as e:
        print(f"Error processing CSV file: {str(e)}")
        return None

def make_predictions(input_df, model, scaler, model_columns):
    """Make predictions on the input data"""
    # Align input DataFrame columns with model columns
    input_df = input_df.reindex(columns=model_columns, fill_value=0)
    
    # Scale the input data
    scaled_input = scaler.transform(input_df)
    
    # Make prediction
    predictions = model.predict(scaled_input)
    
    return predictions

def main():
    """Main function to run the salary prediction app"""
    print("=" * 50)
    print("Employee Monthly Income Prediction")
    print("=" * 50)
    
    # Load model artifacts
    model, scaler, model_columns = load_model()
    
    # Ask user for input method
    print("\nChoose input method:")
    print("1. Manual input")
    print("2. Upload CSV file")
    
    choice = input("Enter your choice (1 or 2): ")
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        # Get manual input
        input_df = get_manual_input()
        if input_df is None:
            print("Invalid input. Exiting.")
            return
        
        # Make prediction
        predictions = make_predictions(input_df, model, scaler, model_columns)
        predicted_salary = predictions[0]
        
        # Display the result
        print("\n" + "=" * 50)
        print("PREDICTION RESULT")
        print("=" * 50)
        print(f"The predicted monthly income for this employee is: ${predicted_salary:,.2f}")
    
    else:
        # Get CSV file path
        file_path = input("\nEnter the path to your CSV file: ")
        while not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            file_path = input("Enter the path to your CSV file: ")
        
        # Process CSV
        input_df = process_csv(file_path)
        if input_df is None:
            print("Error processing CSV file. Exiting.")
            return
        
        # Make predictions
        predictions = make_predictions(input_df, model, scaler, model_columns)
        
        # Add predictions to the dataframe
        input_df['PredictedSalary'] = predictions
        
        # Display results
        print("\n" + "=" * 50)
        print("PREDICTION RESULTS")
        print("=" * 50)
        print("Predicted salaries for all employees:")
        print(input_df[['PredictedSalary']].head(10))
        
        # Ask if user wants to save results
        save = input("\nDo you want to save the predictions to a CSV file? (y/n): ").lower()
        if save == 'y':
            output_path = input("Enter the output file path (e.g., predictions.csv): ")
            input_df.to_csv(output_path, index=False)
            print(f"Results saved to {output_path}")

if __name__ == "__main__":
    main()