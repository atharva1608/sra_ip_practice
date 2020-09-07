import numpy as np
import matplotlib.pyplot as plt
img=plt.imread('roi.jpg')
#print(img.shape)
roi=img[880:1040, 1030:1190,:]
#plt.imshow(roi)
#plt.show()
image=img.copy()
final_place=image[836:996, 220:380,:]
#plt.imshow(final_place)
#plt.show()
final_place[:,:,:]=roi[:,:,:]
plt.imshow(img)
plt.show()
plt.imshow(image)
plt.show()

