# import necessary libraries
from osgeo import gdal
import numpy as np

'''
Function to merge different Dove-C swath paths of a selected scene. 

Input:
list_to_planet_tifs: list with the file path to all images of selected scene
output_path: file path to save the merged image 
img_name: name of the merged image
'''
def merge_swath_paths(list_to_planet_tifs, output_path, img_name):
    # list to store the images that are merged
    gdal_tifs = []
    # iterate over every image of the selected scene
    for tif_file in list_to_planet_tifs:
        # Open the tif file with GDAL and add it to the list
        dataset = gdal.Open(tif_file)
        if dataset is not None:
            gdal_tifs.append(dataset)
            
    # merge the images into a single image and save it according to the output path and the name
    gdal.Warp(f"{output_path}/{img_name}.tif", gdal_tifs)   
    
    # Clean up
    for tif_file in list_to_planet_tifs:
        gdal.Unlink(tif_file)
        
        
        
'''
Function to apply contrast stretching to normalize the image based on percentiles. 
The method is similar to QGIS's DRA, which is used to display images in the QGIS software.

Input:
image: downloaded Dove-C satellite image in .tif format
lower_percentile: lower cutoff percentile. Every value below this percentile value will be set to this value
upper_percentile: upper cutoff percentile. Every value above this percentile value will be set to this value 

Output:
out = image stretched according to the chosen percentile values. The image is also rescaled to values betwee 0 and 255
'''
def contrast_stretch(image, lower_percentile=2, upper_percentile=98):
    # create emtpy image for output
    out = np.zeros_like(image, dtype=np.uint8)
    # iterate over each band
    for i in range(image.shape[0]):  
        # get lower and upper percentile values for the specific band
        p_low, p_high = np.percentile(image[i], (lower_percentile, upper_percentile))
        # Clip the values to the percentile range
        image_clipped = np.clip(image[i], p_low, p_high)
        # Rescale to 0-255
        out[i] = 255 * (image_clipped - p_low) / (p_high - p_low)
    return out