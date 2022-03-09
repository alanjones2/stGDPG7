# G7 GDP Explorer 2007 to 2021
#
# This is a prototype: the code is untidy and it uses data tables
# that were derived manually from the original
#
# The next version will be better structured, use the original data set
# and will utilise Plotly as the graphing engine (probably)
# Future versions will hopefully use live data downloaded directly from OECD

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout = "wide")

st.title('GDP Explorer for G7 Countries')
st.subheader('See the changes in GDP for any period from 2007 to 2021')

# GPSA: Growth rate based on seasonally adjusted volume data, percentage change from previous quarter
gpsa = pd.read_csv('GPSA.csv', index_col='Country').T   

# GYSA: Growth rate based on seasonally adjusted volume data,  percentage change from same quarter of previous year
gysa = pd.read_csv('GYSA.csv', index_col='Country').T 

# VIXOBSA: Volume index, OECD reference year, seasonally adjusted       
vixobsa = pd.read_csv('VIXOBSA.csv', index_col='Country').T

fig, ax = plt.subplots()

dfcols = list(vixobsa.index)
dfcountries = list(vixobsa.columns)



col1,pad1,col2 = st.columns([10,1,10])
with col1:
     st.markdown('''
          Select a set of G7 countries from the list on the left - you can add or delete as many as you want - 
          and then adjust the left slider to the first quarter of interest and the right one to last quarter 
          that you want data for.

          The first quarter that there is data for is Q! 2007 and the final one is Q4 2021.

          When you have selected the countries and the time period should select a data table.

          The tables available are:

          - __GPSA__ - Growth rate based on seasonally adjusted volume data, percentage change from previous quarter
          - __GYSA__ - Growth rate based on seasonally adjusted volume data,  percentage change from same quarter of previous year, 
          - __VIXOBSA__ - Volume index, OECD reference year, seasonally adjusted

          ''')
with col2:

     selected_countries = st.multiselect(
          'Select countries',
          dfcountries, dfcountries)

     start_period, end_period = st.select_slider(
          'Select a range ',
          options=dfcols,
          value=(dfcols[4],dfcols[-4]))

     startindex = dfcols.index(start_period)
     endindex = dfcols.index(end_period)

option = st.selectbox(
     'Select a data table from the drop down list below:',
     ('VIXOBSA: Volume index, OECD reference year, seasonally adjusted',
     'GPSA: Growth rate based on seasonally adjusted volume data, percentage change from previous quarter', 
     'GYSA: Growth rate based on seasonally adjusted volume data,  percentage change from same quarter of previous year'))

if option == 'GPSA: Growth rate based on seasonally adjusted volume data, percentage change from previous quarter':chart = gpsa
if option == 'GYSA: Growth rate based on seasonally adjusted volume data,  percentage change from same quarter of previous year':chart = gysa
if option == 'VIXOBSA: Volume index, OECD reference year, seasonally adjusted':chart = vixobsa

col3,col4 = st.columns([10,10])
with col3:
    chart[startindex:endindex][selected_countries].plot(figsize=(12,4),ax=ax)
    ax.legend(loc=3)
    st.pyplot(fig)

with col4:
     fig, ax = plt.subplots()
     (chart.T[end_period][selected_countries]-chart.T[start_period][selected_countries]).plot.bar(xlabel='',figsize=(12,4),ax=ax)
     plt.xticks(rotation=45)
     plt.xlabel('')
     plt.grid(axis='y')
     st.pyplot(fig)
     
col5,pad1,col6 = st.columns([5,1,10])
with col5:
    st.info('''
     In the charts above you can see a _line_ chart that tracks the change in value over time for the data selected and for each 
     country and a vertical bar chart that shows the difference between the first and last chosen quarters.

     The data table on the right is a the raw data for the period, country and table selected - if not all the data is
     immediately visible, you can scroll though the rows and columns.
    ''')

with col6:
    st.dataframe(chart[startindex:endindex][selected_countries], width=1000)



st.caption('Data Source - OECD: Quarterly National Accounts  : G7 GDP for EI copy')



