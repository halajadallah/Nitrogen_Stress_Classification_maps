import streamlit as st
import pickle
import folium
import geopandas

st.set_page_config(page_title='Classification Maps Aman', layout = 'wide')

#* Classification maps

st.title("Classification Maps")

st.write("Streamlit cannot load the map for all of Natore district, therefore we selected a small region to give an appreciation of the classification on the map")
st.write("Please note the spatial resolution of each pixel is 20 meters. This is the resolution of the red edge band ")

def pickle_off(path):
    pickle_off = open(path, "rb")
    array = pickle.load(pickle_off)
    return array

#boro_2018, boro_2019, boro_2020, boro_2021, boro_2022 = pickle_off("geodata_roi/boro_clre_arrays.pkl")
aman_2018, aman_2019, aman_2020, aman_2021 = pickle_off("geodata_roi/aman_clre_arrays.pkl")
centerx, centery, xmin, ymin, xmax, ymax = pickle_off("geodata_roi/center_bounds_list.pkl")


Natore = geopandas.read_file("geodata_roi/Natore_geo.geojson")
roi = geopandas.read_file("geodata_roi/ROI_box.json")

## colors : R,G,B,alpha
raster_to_coloridx = {
 2: (0.8941176470588236, 0.10196078431372549, 0.10980392156862745,0.7), #red
 3: (1.0, 1.0, 0.2, 0.7), #yellow
 4: (0.1, 0.6, 0.1, 0.7), #green 
 5: (23.0/255, 35.0/255, 246.0/255, 0.7), #purple
 -128: (1, 1, 1, 0)}

m = folium.Map(location=[centery, centerx], zoom_start=13 ,tiles='openstreetmap')#'Stamen Terrain')
st.write('Classes : Poor (-2 to -1) (red), Mild Stress (-1 to 0) (yellow), Normal (0 to 1) (green), Good (1 to 2) (blue)')

#Natore vector
folium.GeoJson(data=Natore["geometry"], style_function = lambda x: {'fillColor' : 'none','color' : 'green'}, name = 'Natore').add_to(m)
#Subregion box vector
folium.GeoJson(data=roi["geometry"], style_function = lambda x: {'fillColor':'none', 'color':'red'}, name='roi').add_to(m)

folium.raster_layers.ImageOverlay(
    name="aman 2018",
    image=aman_2018,
    bounds=[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)
    
   
folium.raster_layers.ImageOverlay(
    name="aman 2019",
    image=aman_2019,
    bounds=[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)
    
folium.raster_layers.ImageOverlay(
    name="aman 2020",
    image=aman_2020,
    bounds=[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)
    
folium.raster_layers.ImageOverlay(
    name="aman 2021",
    image=aman_2021,
    bounds=[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)
    
# add pin to select/ unselect image        
folium.LayerControl().add_to(m)

m
