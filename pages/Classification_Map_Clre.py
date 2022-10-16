


'''

use of rasterio code from
https://discuss.streamlit.io/t/showing-geotiff-raster-data/11170/4
'''
import streamlit as st
from streamlit_folium import folium_static
import folium
import rasterio
import numpy as np


root_path = os.getcwd()
tif_path = os.path.join(root_path, 'tif_only')
boro_2018_path = os.path.join(tif_path,'2018_boro_clre.tif') 
boro_2019_path = os.path.join(tif_path,'2019_boro_clre.tif')
boro_2020_path = os.path.join(tif_path,'2020_boro_clre.tif')
boro_2021_path = os.path.join(tif_path,'2021_boro_clre.tif')
aman_2018_path = os.path.join(tif_path,'2019_aman_clre.tif')
aman_2019_path = os.path.join(tif_path,'2019_aman_clre.tif')
aman_2020_path = os.path.join(tif_path,'2020_aman_clre.tif')
aman_2021_path = os.path.join(tif_path,'2021_aman_clre.tif')


# A dummy Sentinel 2 COG I had laying around
#tif = "streamlit_app/WGS84_S2_image.tif"
# This is probably hugely inefficient, but it works. Opens the COG as a numpy array


def tif_to_array(tif_file):
    src = rasterio.open(tif)
    array = src.read()
    bounds = src.bounds
    return array, bounds
    
boro_2018, bounds = tif_to_array(boro_2018_path)
boro_2019, bounds = tif_to_array(boro_2019_path)
boro_2020, bounds = tif_to_array(boro_2020_path)
boro_2021, bounds = tif_to_array(boro_2021_path)
#boro_2022, bounds = tif_to_array(boro_2018_path)

aman_2018, bounds = tif_to_array(aman_2018_path)
aman_2019, bounds = tif_to_array(aman_2019_path)
aman_2020, bounds = tif_to_array(aman_2020_path)
aman_2021, bounds = tif_to_array(aman_2021_path)

x1,y1,x2,y2 = src.bounds
bbox = [(bounds.bottom, bounds.left), (bounds.top, bounds.right)]

st.title("Plotting maps!")
st.write('x1, y1', (x1, y1))
st.write('x2, y1',(x2, y2))
st.write('bbox', bbox)


## colors : R,G,B,alpha
raster_to_coloridx = {
 3: (0.8941176470588236, 0.10196078431372549, 0.10980392156862745,0.7), #red
 4: (1.0, 1.0, 0.2, 0.7), #yellow
 5: (0.1, 0.6, 0.1, 0.7), #green 
 6: (0.596078431372549, 0.3058823529411765, 0.6392156862745098, 0.7), #purple
 -128: (1, 1, 1, 0)}


m = folium.Map(location=[centery, centerx], zoom_start=11 ,tiles='openstreetmap')#'Stamen Terrain')
'''
folium.raster_layers.ImageOverlay(
    name="boro 2018",
    image=boro_2018,
    bounds=[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)
    
folium.raster_layers.ImageOverlay(
    name="boro 2019",
    image=boro_2019,
    bounds=[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)

folium.raster_layers.ImageOverlay(
    name="boro 2020",
    image=boro_2020,
    bounds=[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)
'''    
folium.raster_layers.ImageOverlay(
    name="boro 2021",
    image=boro_2021,
    #image=np.moveaxis(array, 0, -1),
    bounds= bbox  #[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)

folium.LayerControl().add_to(m)
#m


# call to render Folium map in Streamlit
folium_static(m)