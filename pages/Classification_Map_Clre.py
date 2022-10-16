
import folium
import numpy as np
import pickle
import os

root_path = os.getcwd()
boro_path = os.path.join(root_path, 'geodata', 'boro_clre_arrays.pkl')
aman_path = os.path.join(root_path, 'geodata', 'aman_clre_arrays.pkl')
bounds_path = os.path.join(root_path, 'geodata', 'center_bounds_list.pkl')

pickle_boro_off = open (boro_path, "rb")
boro_arrays_list = pickle.load(pickle_boro_off)

pickle_aman_off = open (aman_path, "rb")
aman_arrays_list = pickle.load(pickle_aman_off)

boro_2018, boro_2019, boro_2020, boro_2021, boro_2022 = boro_arrays_list
aman_2018, aman_2019, aman_2020, aman_2021 = aman_arrays_list

pickle_bounds_off = open(bounds_path, "rb")
bounds_list = pickle.load(pickle_bounds_off)
centerx, centery, xmin, ymin, xmax, ymax = bounds_list

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
'''
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
    
folium.raster_layers.ImageOverlay(
    name="boro 2021",
    image=boro_2021,
    bounds=[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)

folium.raster_layers.ImageOverlay(
    name="boro 2022",
    image=boro_2022,
    bounds=[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)

folium.LayerControl().add_to(m)

m
