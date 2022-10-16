'''
The purpose of this code is to transform GeoTiff files into numpy arrays, before deploying to streamlit app
It avoids the need to install gdal or rasterio, where both are challenging. 

The use of gdal to open and manipulate raster data done using
code adapter from https://github.com/GISerDaiShaoqing/My-Studies-of-Urban-GIS/blob/master/3.Spatial%20visualization%20demo%20in%20folium(for%20Python)/src/foliumrastervisdemo.py

'''

import numpy as np
from osgeo import gdal
import os
import pickle


root_path = os.getcwd()
tif_path = os.path.join(root_path, 'tif_only')
boro_2018_path = os.path.join(tif_path,'2018_boro_clre.tif') 
boro_2019_path = os.path.join(tif_path,'2019_boro_clre.tif')
boro_2020_path = os.path.join(tif_path,'2020_boro_clre.tif')
boro_2021_path = os.path.join(tif_path,'2021_boro_clre.tif')
boro_2022_path = os.path.join(tif_path,'2022_boro_clre.tif')
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
ds_boro_2022 = gdal_open(boro_2022_path)

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

center_bounds_list = [centerx, centery, xmin, ymin, xmax, ymax]
bounds_path = os.path.join(root_path, 'geodata', 'center_bounds_list.pkl')
with open(bounds_path, 'wb') as fm:
   pickle.dump(center_bounds_list, fm)

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
boro_2022 = tif_to_array(ds_boro_2022)
boro_clre_list = [boro_2018, boro_2019, boro_2020, boro_2021, boro_2022]

aman_2018 = tif_to_array(ds_aman_2018)
aman_2019 = tif_to_array(ds_aman_2019)
aman_2020 = tif_to_array(ds_aman_2020)
aman_2021 = tif_to_array(ds_aman_2021)
aman_clre_list = [aman_2018, aman_2019, aman_2020, aman_2021]

boro_path = os.path.join(root_path, 'geodata', 'boro_clre_arrays.pkl')
with open(boro_path, 'wb') as fm:
   pickle.dump(boro_clre_list, fm)

aman_path = os.path.join(root_path, 'geodata','aman_clre_arrays.pkl')
with open(aman_path, 'wb') as fm:
   pickle.dump(aman_clre_list, fm)

