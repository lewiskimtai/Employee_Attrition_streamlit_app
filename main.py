# Import Libraries
import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="expanded", )
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit.components.v1 as components

# File location
url="WA_Fn-UseC_-HR-Employee-Attrition.csv"

# SIDEBAR

# SideBar Heading
st.sidebar.header("Employee Attrition")

df = pd.read_csv(url, encoding="ISO-8859-1", low_memory=False)

# Side Bar Menu
menu = ['Employee Data', 'Employee Attrition']

selection = st.sidebar.selectbox("Employee Information ", menu)

st.sidebar.write('Employee analytics showing Employee Attrition.')

if selection == 'Employee Data':
    st.markdown('Employee data')
    st.dataframe(df.head(50))


    



if selection== 'Employee Attrition':

    # Breakdown of distance from home by job role and attrition.
    st.header("Breakdown of distance from home by job role and attrition.")
    dist = df.groupby(['JobRole', 'Attrition'])['DistanceFromHome'].sum().reset_index()
    st.table(dist.head(20))
    
    
    fig = px.bar(dist, 
         x='JobRole', 
         y='DistanceFromHome', 
         color='Attrition',
         barmode="group",
        title='breakdown of distance from home by job role and attrition')
    st.plotly_chart(fig)
    
    # Average monthly income by education and attrition.
    st.header("Average monthly income by education and attrition.")
    income = df.groupby(['Education', 'Attrition'])['MonthlyIncome'].mean().reset_index()
    st.table(income.head(20))
    
    
    fig = px.bar(income, 
             x='Education', 
             y='MonthlyIncome', 
             color='Attrition',
             barmode="group",
            title='average monthly income by education and attrition')
    st.plotly_chart(fig)

