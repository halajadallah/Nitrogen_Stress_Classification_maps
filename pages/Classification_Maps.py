
'''
The use of gdal to open and manipulate raster data done using
code adapter from https://github.com/GISerDaiShaoqing/My-Studies-of-Urban-GIS/blob/master/3.Spatial%20visualization%20demo%20in%20folium(for%20Python)/src/foliumrastervisdemo.py

setting up folium to display images over map using code adapter from
# code adapted from: https://github.com/python-visualization/folium/blob/main/examples/ImageOverlay.ipynb

coloring based on classification classes using code from answer of D_Serg in https://stackoverflow.com/questions/50689068/display-raster-data-in-folium-handling-no-data-values,  
'''
import numpy as np
import folium
from folium import plugins
#from osgeo import gdal
import gdal
import os
import streamlit as st
import matplotlib.pyplot as plt

#st.set_page_config(page_title='Shoreline Change Rate', layout = 'wide')

#st.header('Classification Maps for Boro and Aman seasons')
#st.subheader('four classes per year')


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

#Open raster file
driver=gdal.GetDriverByName('GTiff')
driver.Register()

def gdal_open(file): 
    ds = gdal.Open(file)
    if ds is None:
        print('Could not open : '+file)
        return
    return ds

ds_boro_2018 = gdal_open(boro_2018_path)
ds_boro_2019 = gdal_open(boro_2019_path)
ds_boro_2020 = gdal_open(boro_2020_path)
ds_boro_2021 = gdal_open(boro_2021_path)

ds_aman_2018 = gdal_open(aman_2018_path)
ds_aman_2019 = gdal_open(aman_2019_path)
ds_aman_2020 = gdal_open(aman_2020_path)
ds_aman_2021 = gdal_open(aman_2021_path)

#Get coordinates, cols and rows
# all files are similar in cols, rows and geotransform data
ds = ds_boro_2018
geotransform = ds.GetGeoTransform()
cols = ds.RasterXSize 
rows = ds.RasterYSize 


#Get extent/ boundaries of image to be displayed on map (lat, lon)
xmin=geotransform[0]
ymax=geotransform[3]
xmax=xmin+cols*geotransform[1]
ymin=ymax+rows*geotransform[5]

#Get Central point
centerx=(xmin+xmax)/2
centery=(ymin+ymax)/2

#Raster convert to array in numpy
def tif_to_array(ds):
    bands = ds.RasterCount
    band=ds.GetRasterBand(1)
    dataset= band.ReadAsArray(0,0,cols,rows)
    #dataimage=dataset
    return dataset

boro_2018 = tif_to_array(ds_boro_2018)
boro_2019 = tif_to_array(ds_boro_2019)
boro_2020 = tif_to_array(ds_boro_2020)
boro_2021 = tif_to_array(ds_boro_2021)

aman_2018 = tif_to_array(ds_aman_2018)
aman_2019 = tif_to_array(ds_aman_2019)
aman_2020 = tif_to_array(ds_aman_2020)
aman_2021 = tif_to_array(ds_aman_2021)



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
    bounds=[[ymin, xmin], [ymax, xmax]],
    opacity=0.7,
    colormap=lambda x: raster_to_coloridx[x],
    interactive=True,
    cross_origin=False,
    zindex=1,
    ).add_to(m)

folium.LayerControl().add_to(m)
m
