
from streamlit_option_menu import option_menu
import pickle
import streamlit as st



# loading the saved models

credit_model = pickle.load(open('loan_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Loan Status Prediction using Machine Learning',
                          
                          ['Loan_Status_Prediction'],
                          icons=['activity'],
                          default_index=0)
    
    

        
    
    

# Parkinson's Prediction Page
if (selected == "Loan_Status_Prediction"):
    
    # page title
    st.title("Loan Status Prediction using Machine Learning")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        Gender = st.text_input('Gender male  = 1')
        
    with col2:
       Married = st.text_input('Married = 1 ')
        
    with col3:
       Dependents = st.text_input('Dependents')
        
    with col4:
       Education = st.text_input('graduate = 1')
        
    with col5:
      Self_Employed = st.text_input('Self_Emp = 1')
        
    with col1:
       ApplicantIncome = st.text_input('ApplicantIncome')
        
    with col2:
        CoapplicantIncome = st.text_input('CoapplicantI')
        
    with col3:
        LoanAmount = st.text_input('LoanAmount')
        
    with col4:
       Loan_Amount_Term = st.text_input('LoanAmountTerm')
        
    with col5:
       Credit_History = st.text_input('Credit_History')
        
    with col1:
        Property_Area = st.text_input('Property_Area(Rural:0,Semiurban:1,Urban:2)')
        
   
    # code for Prediction
    loan_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Credit_Card_Fraud_Detection_Test_Result"):
        # Assuming Time, V1 to V28, and Amount are variables with proper numeric values
        #input_data = np.array([[Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]], dtype=float)

        # Now use this input_data for prediction
        #Credit_Card_Fraud_Detection = credit_model.predict(input_data)
        Loan_Status_Prediction = credit_model.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])                          
        
        if (Loan_Status_Prediction[0] == 0):
          loan_diagnosis = "No Loan"
        else:
         loan_diagnosis = "Loan"
        
    st.success(loan_diagnosis)






