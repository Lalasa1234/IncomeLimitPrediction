import streamlit as st
import pandas as pd
from model import predict
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
import sklearn

st.title(f'Income limit prediction')

gender_options = [' Male', ' Female']
emp_options = [' Children or Armed Forces', ' Not in labor force', ' Full-time schedules', 'Part-time schedules', ' Unemployed full-time', ' PT for non-econ reasons usually FT']
tax_options = [' Joint both under 65', ' Nonfiler', ' Joint one under 65 & one 65+', ' Single', ' Joint both 65+', ' Head of household']
edu_options = [' Bachelors degree(BA AB BS)',
 ' Some college but no degree',
 ' High school graduate',
 ' Masters degree(MA MS MEng MEd MSW MBA)',
 ' 9th grade',
 ' Children',
 ' 11th grade',
 ' 10th grade',
 ' Associates degree-academic program',
 ' Associates degree-occup /vocational',
 ' 5th or 6th grade',
 ' 7th and 8th grade',
 ' 12th grade no diploma']

house_options = [' Other relative of householder', ' Householder', ' Nonrelative of householder', ' Spouse of householder', 'Child under 18', ' Child 18 or older', ' Group Quarters- Secondary individual']

with st.form('Form'):
    st.header('Enter the people-related specifications:')
    age = st.number_input (label='Age: ',min_value = 0, max_value = 90, step = 1)
    gender = st.selectbox(label='Gender: ',options= gender_options )
    education = st.selectbox (label = 'Educational qualification: ',options = edu_options)
    employment_commitment = st.selectbox(label = 'Type of employment: ', options = emp_options)
    working_week_per_year = st.number_input (label='No. of working week per year: ',min_value = 1, max_value = 52, step = 1)
    household_summary = st.selectbox(label='Status of house ownership: ',options = house_options)
    
    tax_status = st.selectbox ('Select the characeristics of the tax filer: ', options = tax_options)
    
    mig_year = st.number_input(label='Year of migration to US: ',min_value=94,max_value=95)

    submit_values = st.form_submit_button ('Predict')
    
if submit_values:
    
    data = [age,gender,education,employment_commitment,working_week_per_year,household_summary,tax_status,mig_year]
    
    prediction = predict(data)
    
    # if prediction[0] == 1:
    #     value = 'Person is below income limit'
    # else: 
    #     value = 'Person is above income limit'
        
    st.header('Here is the prediction: ')
    st.success(f'{prediction}')
    st.balloons()
    
