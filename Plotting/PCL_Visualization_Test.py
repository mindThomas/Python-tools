import numpy as np
import pcl

import pcl.pcl_visualization
# https://strawlab.github.io/python-pcl/

cloud = pcl.load_XYZRGB('/home/thomas/Downloads/table_scene_mug_stereo_textured.pcd')
#cloud = pcl.load("Tile_173078_LD_010_017_L22.obj")

#%%
# Centred the data
centred = cloud - np.mean(cloud, 0)
print(centred)
ptcloud_centred = pcl.PointCloud()
#ptcloud_centred.from_array(centred)
# ptcloud_centred = pcl.load("Tile_173078_LD_010_017_L22.obj")

#%%
visual = pcl.pcl_visualization.CloudViewing()

# PointXYZ
# visual.ShowMonochromeCloud(cloud, b'cloud')
# visual.ShowGrayCloud(ptcloud_centred, b'cloud')
visual.ShowColorCloud(cloud, b'cloud')
# visual.ShowColorACloud(ptcloud_centred, b'cloud')

#v = True
#while v:
    #v = not(visual.WasStopped())