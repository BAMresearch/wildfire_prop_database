# wildfire_prop_database
This repo includes code for pre-processing Dove-C satellite data to extract burned areas semi-automatically. 


The first step often includes merging Planet Labs Inc. images from different Dove-C satellite swath paths into a single image, as shown in the following example:

![alt text](https://github.com/BAMresearch/wildfire_prop_database/tree/main/imgs_readme/workflow_merge.png "Workflow of merging process")

Afterwards, thresholds on the NIR (or other) band are used to create an binary image with coherent clusters, from which the burned area is extracted and transformed into a GIS-readable polygon. 
The workflow is illustrated in this example:

![alt text](https://github.com/BAMresearch/wildfire_prop_database/tree/main/imgs_readme/workflow_image_to_polygon.png "Workflow of extracting the burned area")

Te code folder contains a Jupyter notebook with a working example, the necessary images, as well as the utility functions used for the process.
