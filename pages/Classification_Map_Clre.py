
import folium
import numpy as np
import pickle
import os

#loading pickled geodata into numpy arrays 
root_path = os.getcwd()
bounds_path = os.path.join(root_path, 'geodata', 'center_bounds_list.pkl')


pickle_bounds_off = open(bounds_path, "rb")
bounds_list = pickle.load(pickle_bounds_off)
centerx, centery, xmin, ymin, xmax, ymax = bounds_list

def pickle_off(path):
    pickle_off = open(path, "rb")
    array = pickle.load(pickle_off)
    return array


boro_2018_ap = os.path.join(root_path, 'geodata', 'boro_2018_array.pkl')
boro_2018 = pickle_off(boro_2018_ap)

boro_2019_ap = os.path.join(root_path, 'geodata', 'boro_2019_array.pkl')
boro_2019 = pickle_off(boro_2019_ap)

boro_2020_ap = os.path.join(root_path, 'geodata', 'boro_2020_array.pkl')
boro_2020 = pickle_off(boro_2020_ap)

boro_2021_ap = os.path.join(root_path, 'geodata', 'boro_2021_array.pkl')
boro_2021 = pickle_off(boro_2021_ap)

boro_2022_ap = os.path.join(root_path, 'geodata', 'boro_2022_array.pkl')
boro_2022 = pickle_off(boro_2022_ap)

aman_2018_ap = os.path.join(root_path, 'geodata', 'aman_2018_array.pkl')
aman_2018 = pickle_off(aman_2018_ap)

aman_2019_ap = os.path.join(root_path, 'geodata', 'aman_2019_array.pkl')
aman_2019 = pickle_off(aman_2019_ap)

aman_2020_ap = os.path.join(root_path, 'geodata', 'aman_2020_array.pkl')
aman_2020 = pickle_off(aman_2020_ap)

aman_2021_ap = os.path.join(root_path, 'geodata', 'aman_2021_array.pkl')
aman_2021 = pickle_off(aman_2021_ap)


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
