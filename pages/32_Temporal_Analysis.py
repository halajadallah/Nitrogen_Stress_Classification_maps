import streamlit as st

st.title("Temporal Analysis")

st.markdown(
'''
We compare the vegetation Index over four or five years. To make the comparison we standardize the index by computing the mean and standard deviation over the years. 

* mean =mean(ind_2019,ind_2020,ind_2021,ind_2022)

* std = std(ind_2019,ind_2020,ind_2021,ind_2022)

Standardized index = (index – mean)/std

## Classification:

#### we classify nitrogen content based on __number of standard deviations from the mean__.

#### Poor : (-2 to -1) ;  Mild Stress: (-1 to 0), Normal: (0 to 1) and Good: (1 to 2)  

'''
)

