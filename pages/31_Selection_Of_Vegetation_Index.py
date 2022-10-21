import streamlit as st

st.title("Selection Of Vegetation Index")

st.markdown(
'''
We considered the histogram of the index for several years. As the diagram show the Clre index is not narrow nor too wide. 
Notice the NDVI is left skewed overlaps slightly with MCARI.   
All years have similar histograms. 

As we will observe from classification analysis, Clre spread is only two standard deviations from the temporal mean. 
This allows more variability of the classification of plant chlorophyll content.

'''
)

#col1, col2 = st.columns(2)
# with col1:
#    st.image("./histograms/VI_hist_boro_2018.PNG")
   
st.image("./histograms/VI_hist_boro_2018.PNG")

st.image("./histograms/VI_hist_boro_2019.PNG")

st.image("./histograms/VI_hist_boro_2020.PNG")

st.image("./histograms/VI_hist_boro_2021.PNG")

st.image("./histograms/VI_hist_boro_2022.PNG")