import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 
import math
img=plt.imread('edge-detection.png')
sobel_xkernel = [[ -1, 0, 1],
                 [ -2, 0, 2],
                 [ -1, 0, 1]]

sobel_ykernel = [[-1 ,-2 ,-1],
                 [ 0 , 0 , 0],
                 [ 1 , 2 , 1]]


gaussian_kernel = [[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]

def kernel_app(input_image, kernel):
    width = input_image.shape[0]
    height = input_image.shape[1]
    
    # Middle of the kernel
    offset = len(kernel) // 2

    # Create empty output array
    output_image = np.empty((width,height))
    output_image.fill(0)
    # Compute convolution between value and kernels
    for x in range(offset, width - offset):
        for y in range(offset, height - offset):
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b - offset
                    value = input_image[xn][yn]
                    output_image[x][y] += value * kernel[a][b]
    return output_image
         
def non_max_suppression(img, D):
        M, N  = img.shape
        Z = np.zeros((M,N), dtype=np.int32)
        angle = D * 180. / np.pi
        angle[angle < 0] += 180


        for i in range(1,M-1):
            for j in range(1,N-1):
                try:
                    q = 255
                    r = 255

                   #angle 0
                    if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                        q = img[i, j+1]
                        r = img[i, j-1]
                    #angle 45
                    elif (22.5 <= angle[i,j] < 67.5):
                        q = img[i+1, j-1]
                        r = img[i-1, j+1]
                    #angle 90
                    elif (67.5 <= angle[i,j] < 112.5):
                        q = img[i+1, j]
                        r = img[i-1, j]
                    #angle 135
                    elif (112.5 <= angle[i,j] < 157.5):
                        q = img[i-1, j-1]
                        r = img[i+1, j+1]

                    if (img[i,j] >= q) and (img[i,j] >= r):
                        Z[i,j] = img[i,j]
                    else:
                        Z[i,j] = 0


                except IndexError as e:
                    pass
        
        plt.imshow(Z,cmap='gray')
        plt.title('Non Max Supression')
        plt.show()
        return Z
        
def threshold(img,highThreshold=0.05,lowThreshold=0.09):

        highThreshold = img.max() * highThreshold;
        lowThreshold = highThreshold * lowThreshold;

        M, N = img.shape
        res = np.zeros((M,N), dtype=np.int32)

        weak = np.int32(25)
        strong = np.int32(255)

        strong_i, strong_j = np.where(img >= highThreshold)
        zeros_i, zeros_j = np.where(img < lowThreshold)

        weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))

        res[strong_i, strong_j] = strong
        res[weak_i, weak_j] = weak
        plt.imshow(res,cmap='gray')
        plt.title('Threshold')
        plt.show()

        return (res)

def hysteresis(img,weak=25,strong=255):

        M, N = img.shape
        weak = 25
        strong = 255

        for i in range(1, M-1):
            for j in range(1, N-1):
                if (img[i,j] == weak):
                    try:
                        if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                            or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                            or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                            img[i, j] = strong
                        else:
                            img[i, j] = 0
                    except IndexError as e:
                        pass
        plt.imshow(img,cmap='gray')
        plt.title('Hysteresis')
        plt.show()
        return img
    
   
colour_img = np.array(Image.open("edge-detection2.jpg"))


r, g, b = colour_img[:,:,0], colour_img[:,:,1], colour_img[:,:,2]
gray_img = 0.2989 * r + 0.5870 * g + 0.1140 * b


img = kernel_app(gray_img, gaussian_kernel)

sobel_x = kernel_app(img, sobel_xkernel)
sobel_y = kernel_app(img, sobel_ykernel)
D = np.arctan2(sobel_y, sobel_x)
sobel = np.empty((sobel_x.shape[0], sobel_x.shape[1]))
for i in range(sobel_x.shape[0]):
    for j in range(sobel_x.shape[1]):
        sobel[i][j] = math.sqrt(sobel_x[i][j]**2 + sobel_y[i][j]**2)
sobel_img = Image.fromarray(np.uint8(sobel)).convert('RGB')
sobel_img.show()

non_max_supp = non_max_suppression(sobel, D)

double_threshold = threshold(non_max_supp)

canny = hysteresis(double_threshold[0], double_threshold[1], double_threshold[2])


canny_img = Image.fromarray(np.uint8(double_threshold[0])).convert('RGB')
canny_img.show()


