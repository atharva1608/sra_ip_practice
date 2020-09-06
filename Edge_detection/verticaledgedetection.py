import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 
import math
vertical_edge_kernel = [[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]]

edge_kernel = [[-1, -1, -1],
               [-1,  8, -1],
               [-1, -1, -1]]


gaussian_kernel = [[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]



def kernel_apply(input_image, kernel):
    width = input_image.shape[0]
    height = input_image.shape[1]
    offset = len(kernel) // 2
    output_image = np.empty((width,height))
    output_image.fill(0)

    for x in range(offset, width - offset):
        for y in range(offset, height - offset):
            for i in range(len(kernel)):
                for j in range(len(kernel)):
                    xn = x + i - offset
                    yn = y + j - offset
                    value = input_image[xn][yn]
                    output_image[x][y] += value * kernel[i][j]
    return output_image


original_img = np.array(Image.open("edge-detection.png"))
r, g, b = original_img[:,:,0], original_img[:,:,1], original_img[:,:,2]
gray_img = 0.2989 * r + 0.5870 * g + 0.1140 * b

# blurring the image using gaussian-blur kernel
img = kernel_apply(gray_img, gaussian_kernel)

vertical_edge = Image.fromarray(np.uint8(kernel_apply(img, vertical_edge_kernel))).convert('RGB')
vertical_edge.show()



