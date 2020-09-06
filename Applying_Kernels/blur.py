import numpy as np
from PIL import Image , ImageDraw
img=Image.open('blur.jpeg')
#img=Image.open('blur.jpeg')
input_pixels=img.load()
print(img.size)
#height,width,num_channels=img.shape
box_kernel=[[0.3,0,0.3],
            [1/5,0,1/5],
            [0.3,0.1,0.3]]

kernel=box_kernel
offset=len(kernel)//2
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
               
        draw.point((x,y),(int(acc[0]),int(acc[1]),int(acc[2])))
#output_img.save("outputblurimage.jpeg")
img.show()
output_img.show()

