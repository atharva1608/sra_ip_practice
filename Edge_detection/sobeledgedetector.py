import numpy as np
import matplotlib.pyplot as plt

#define the vertical filter
vertical_filter = [[-1, -2 ,-1], 
                   [ 0  ,0  ,0], 
                   [ 1  ,2  ,1]]

#define the horizontal filter
horizontal_filter = [[-1 ,0, 1], 
                     [-2 ,0, 2], 
                     [-1 ,0, 1]]

#read in the pinwheel image
img = plt.imread('edge-detection.png')

#get the dimensions of the image
height,width,num_channels = img.shape

#initialize the edges image
sobel_edges_img = img.copy()

#loop over all pixels in the image
for i in range(3, height-2):
    for j in range(3, width-2):
        
        #create little local 3x3 box
        pixels = img[i-1:i+2, j-1:j+2, 0]
        
        #apply the vertical filter
        vertical_transforme_pixels = vertical_filter*pixels
        #remap the vertical score
        vertical_score = vertical_transforme_pixels.sum()/4
        
        #apply the horizontal filter
        horizontal_transforme_pixels = horizontal_filter*pixels
        #remap the horizontal score
        horizontal_score = horizontal_transforme_pixels.sum()/4
        
        #combine the horizontal and vertical scores into a total edge score
        sobel_edge_score = (vertical_score**2 + horizontal_score**2)**.5
        
        #insert this edge score into the edges image
        sobel_edges_img[i, j] = [sobel_edge_score]*3

#remap the values in the 0-1 range in case they went out of bounds
sobel_edges_img = sobel_edges_img/sobel_edges_img.max()

plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.subplot(1,2,2)
plt.imshow(sobel_edges_img,cmap='gray')
plt.show()


