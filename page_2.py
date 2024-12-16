import streamlit as st
import numpy as np
import pandas as pd

def single_prediction(pipeline):
    st.subheader('Single Prediction')

    vehicle_class = st.selectbox(
        'Select Vehicle Class', 
        ['Four-Door Car', 'Two-Door Car', 'SUV', 'Sports Car', 'Luxury SUV', 'Luxury Car']
    )

    coverage = st.selectbox(
        'Select Coverage Type', 
        ['Extended', 'Basic', 'Premium']
    )

    renew_offer_type = st.selectbox(
        'Select Renew Offer Type', 
        ['Offer1', 'Offer2', 'Offer3', 'Offer4']
    )

    employment_status = st.selectbox(
        'Select Employment Status', 
        ['Retired', 'Employed', 'Disabled', 'Medical Leave', 'Unemployed']
    )

    marital_status = st.selectbox(
        'Select Marital Status', 
        ['Divorced', 'Married', 'Single']
    )

    education = st.selectbox(
        'Select Education Level', 
        ['High School or Below', 'College', 'Master', 'Bachelor', 'Doctor']
    )

    num_policies = st.slider(
        'Select Number of Policies', 
        1, 9, 1 
    )

    monthly_premium_auto = st.number_input(
        'Enter Monthly Premium Auto', 
        min_value=0.0, 
        step=0.1
    )

    total_claim_amount = st.number_input(
        'Enter Total Claim Amount', 
        min_value=0.0, 
        step=0.1
    )

    income = st.number_input(
        'Enter Income', 
        min_value=0.0, 
        step=1000.0
    )

    input_data = pd.DataFrame({
        'Vehicle Class': [vehicle_class],
        'Coverage': [coverage],
        'Renew Offer Type': [renew_offer_type],
        'EmploymentStatus': [employment_status],
        'Marital Status': [marital_status],
        'Education': [education],
        'Number of Policies': [num_policies],
        'Monthly Premium Auto': [monthly_premium_auto],
        'Total Claim Amount': [total_claim_amount],
        'Income': [income]
    })

    if st.button('Make Prediction'):
        prediction = pipeline.predict(input_data)
        st.write('Prediction')
        st.write('Customer Lifetime Value:', prediction[0])
