# Image-Processing
## Tables of Contents
  * [About](#about)
  * [Task 1](#task-1)
    * [Rotation of Image](#rotating-image)
  * [Task 2](#task-2)
    * [Blurring Image](#blurring-image)
    * [Sharpening Image](#sharpening-image)
  * [Task 3](#task-3)
    * [Vertical Edge Detection](#vertical-edge)
    * [Horizontal Edge Detection](#horizontal-edge)
    * [Sobel Edge Detection](#sobel-edge)
    * [Canny Edge Detction](#canny-edge)
  * [Task 4](#task-4)
    * [Erosion](#erosion)
    * [Dilation](#dilation)
  * [Task 5](#task-5)
    * [Masking](#masking)
  * [Task 6](#task-6)
    * [Region of Image](#roi)
## About
All the Image Processing tasks are done without using any opencv library unless mentioned in order to understand the basics of image processing.
## Task 1
### 1. Image Rotation
Rotating the given image by any angle anticlockwise by using numpy and matplotlib library.Taking the rotation angle as the input from the user and rotate the given image.
> Original Input image -  
  ![**original image**](https://github.com/atharva1608/sra_ip_practice/blob/master/ImageRotation/rotate.png)  
    
  > Rotating it by 50 degree -  
  ![**rotated image**](https://github.com/atharva1608/sra_ip_practice/blob/master/ImageRotation/rotationofimageoutput1.png)
  
  ## Task 2
  ### 2. Applying Kernel
  Blurring and sharpening the image by using kernel(3x3 filters).
  > Input Image -
  ![**input image1**](https://github.com/atharva1608/sra_ip_practice/blob/master/Applying_Kernels/blur.jpeg)
  ![**input image2**](https://github.com/atharva1608/sra_ip_practice/blob/master/Applying_Kernels/filter.png)
  > Blur and Sharpen image -
  ![**blur image**](https://github.com/atharva1608/sra_ip_practice/blob/master/Applying_Kernels/outputblurimage.jpeg)
  ![**blur image2**](https://github.com/atharva1608/sra_ip_practice/blob/master/Applying_Kernels/outputblurimage1.jpeg)
  ![**sharpen image**](https://github.com/atharva1608/sra_ip_practice/blob/master/Applying_Kernels/outputsharpenimage.png)
  
  ## Task 3
  ### 3. Edge Detection
  1. Vertical Edge Detection is done by using vertical filter(3x3).
  2. Horizongtal Edge Detction is done by using horizontal filter(3x3),
  3. Sobel Edge Detection was done by using two filters sobelx and sobely and applying on the given image.
  > Input Image -
  ![**input image**](https://github.com/atharva1608/sra_ip_practice/blob/master/Edge_detection/edge-detection.png)
  
  > Applying Sobel Edge Detector -
  ![**output image**](https://github.com/atharva1608/sra_ip_practice/blob/master/Edge_detection/outputedgedetectionsobel.png)
  4. Canny Edge Detection: It basically consists of five steps- 1) Noise Reduction 2)Gradient Calculation 3)Non-maximum suppression 4)Double Threshold 5)Edge   Tracking Hysteresis
  
  ## Task 4
  Applying Morphological Transformation Erosion and Dilation on the given image.
  Erosion erodes away the boundaries of the object and used to diminsh the features of an image.
  Dilation increases the object area and used to accentuate features.
  > Input Image -
  ![**input image**](https://github.com/atharva1608/sra_ip_practice/blob/master/Morphological_Transformation/morphological.png)
  
  > Erosion Image -
  ![**erosion output**](https://github.com/atharva1608/sra_ip_practice/blob/master/Morphological_Transformation/erosion.png)
  
  > Dilation Image -
  ![**dilation image**](https://github.com/atharva1608/sra_ip_practice/blob/master/Morphological_Transformation/dilation.png)
  
  ## Task 5
  In this case the blue colour ball is to be detcted from red,green and blue balls. Using cv2.cvtColor(frame, cv.COLOR_BGR2HSV) library the given image is changed   from BGR to HSV and the masking is done to detect blue color.
 > Input Image -
 ![**input image**](https://github.com/atharva1608/sra_ip_practice/blob/master/masking/mask.jpg)
 
 > Blue Ball Detected -
 ![**output image**](https://github.com/atharva1608/sra_ip_practice/blob/master/masking/masking_output.png)
 
 ## Task 6
 Region of Image is obtained by numpy indexing.In this input image the foot ball is moved from one place to other place using numpy indexing.
 Figure 1                      |  Figure 2
:-------------------------:|:-------------------------:
<img width="640" height="450" src="https://github.com/atharva1608/sra_ip_practice/blob/master/ROI/roi.jpg">|<img width="640" height="450" src="https://github.com/atharva1608/sra_ip_practice/blob/master/ROI/roioutput.png">

>Find detailed output video [here](https://photos.app.goo.gl/EGuWSTebXgdqKd1S7)
