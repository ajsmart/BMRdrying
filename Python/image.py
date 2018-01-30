import numpy as np
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt

#####THRESHOLD, 0 is white, 255 is black#####
threshhold=50

im=Image.open("data\por\slrry.jpg")
print im.mode
iml = im.convert('L')
print iml.mode
x,y= iml.size

print x
print y
county=0
countx=0

for i in range (x):
    for j in range (y):
        if j==0:
            iml.putpixel((i,j),0)
        if j==y-1:
            iml.putpixel((i,j),0)
        if iml.getpixel((i,j))<=threshhold:
            iml.putpixel((i,j),0)
        elif iml.getpixel((i,j))>threshhold:
            iml.putpixel((i,j),255)
xplot=np.arange(x)
xstart=xplot
xend=xplot
start=np.zeros(x)
end=np.zeros(x)
for i in range(x):
    county=0
    for j in range(y):
        if iml.getpixel((i,j))==0:
            county+=1
            if start[i]==0:
                ystart=j
                start[i]=ystart
        elif iml.getpixel((i,j))==255:
            if county<50:
                county=0
                start[i]=0
            if county>50:
                if end[i]==0:    
                    end[i]=j
#for k in range(len(start)):
#    if start[k]==0:
#        xstart=np.delete(xstart,k)
#for l in range(len(end)):
#    if end[l]==0:
#        xend=np.delete(xend,l)
start=np.ma.masked_equal(start,0)
end=np.ma.masked_equal(end,0)
print end.mean()
print start.mean()
length = end.mean()-start.mean()
print length
plt.plot(xplot,start)
plt.plot(xplot,end)
plt.show()