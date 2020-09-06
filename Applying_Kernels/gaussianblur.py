import numpy as np
from PIL import Image , ImageDraw
#img=Image.open('filter.png')
img=Image.open('blur.jpeg')
input_pixels=img.load()
#img=plt.imread('blur.jpeg')
print(img.size)
#height,width,num_channels=img.shape
gaussian_kernel=   [[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]

kernel=gaussian_kernel
offset=len(kernel)//2
#print(offset)
#print(len(kernel))
output_img=Image.new("RGB",img.size)
draw=ImageDraw.Draw(output_img)
for x in range(offset,img.width-offset):
    for y in range(offset,img.height-offset):
        acc=[0,0,0]
        for i in range(len(kernel)):
            for j in range(len(kernel)):
                xn = x+i-offset
                yn = y+j-offset
                pixel = input_pixels[xn,yn]
                acc[0] += pixel[0]*kernel[i][j]
                acc[1] += pixel[1]*kernel[i][j]
                acc[2] += pixel[2]*kernel[i][j]
                #acc[3] += pixel[3]*kernel[i][j]
        draw.point((x,y),(int(acc[0]),int(acc[1]),int(acc[2])))
#output_img.save("outputgaussianblurimage.jpeg")
img.show()
output_img.show()
