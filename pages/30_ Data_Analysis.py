import streamlit as st
#*  Includes Standardization by GEE, Classification using ArcMap

st.title("Data Analysis")

st.markdown(
'''
* We use indices that combine spectral bands to show information about nitrogen related vegetation status.

* The red edge band is known to be sensitive to nitrogen content in plant leaves. Therefore, we choose to look at two such indices.

* We study several years and monitor the change in nitrogen related plant traits. 

# Vegetation related Indices:

* Important bands are near infrared (nir) 835 nm, red edge (re) 704 nm, red and green

__Normalized Difference Vegetation Index__ (NDVI) = (nir – red)/(ni + red)
NDVI reveals areas of vegetation stress.

__Modified Chlorophyll Absorption Reflectance Index__ (MCARI) = ((re  - red) -0.2*(re – green))*(re/red)

__Chlorophyll red edge index__ (Clre) = (nir/re) – 1

Both MCARI and Clre show chlorophyl strength of crop of interest. It is directly related to fertilizer need. 
Nitrogen is an essential component for plant growth. 

A map showing stress areas can guide farmers to pay attention for further follow up.   

'''
)