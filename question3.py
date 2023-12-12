#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:46:41 2023

@author: papantiamoah

question 3
"""




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.title('question3')
csv_file = st.file_uploader("select csv file:", type="csv")


    
df = pd.read_csv(csv_file)

if 'Age' in df.columns and 'Name' in df.columns:
    st.write("A histogram Graph showing the ages of individuals ")
    fig, ax = plt.subplots()
    ax.hist(df['Age'], bins=100, edgecolor='black')
    ax.set_xlabel('Age')        
    ax.set_ylabel('Name')
    ax.set_title('A Histogram Graph showing Ages of Individuals')
    st.pyplot(fig)
        
else:
        st.error("Invalid File Format")
        
        