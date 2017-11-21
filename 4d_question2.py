from PIL import Image
import numpy

#set size

imagewidth=63
imageheight=63

#step for ~cosine look
step=(127,127,127)

pixellist=[(255,255,255)]*imagewidth*imageheight #load all white image

for i in range(imagewidth):
	if i%2==0:
		for j in range(imageheight):
			pixellist[imagewidth*j+i]=tuple(numpy.subtract(pixellist[imagewidth*j+i],step))

	
for k in range((imagewidth*imageheight)): #put in horizontal pattern
	if (k/imagewidth)%2==0:
		pixellist[k]=tuple(numpy.subtract(pixellist[k],step))

#create image
img=Image.new('RGB',(imagewidth,imageheight))
img.putdata(pixellist)
img.save('answer2.png', dpi=(25,25))#set dpi so 1 mm = 1 pixel

