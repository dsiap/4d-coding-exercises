from PIL import Image

#set size

im=Image.open('puppy.jpg')
pixellist = im.load()

img = Image.new( im.mode, im.size)
pixelnew = img.load()
for i in range(img.size[0]-2):
    for j in range(img.size[1]-2):
        if abs((sum(pixellist[i+2,j+1])+sum(pixellist[i,j+1])+sum(pixellist[i+1,j+2])+sum(pixellist[i+1,j]))/12-sum(pixellist[i+1,j+1])/3)>10:#compare to pixels above, below, and on either side 
			if (sum(pixellist[i+2,j+1])+sum(pixellist[i,j+1])+sum(pixellist[i+1,j+2])+sum(pixellist[i+1,j]))/12>sum(pixellist[i+1,j+1])/3: # now match brightness
				difference=abs((sum(pixellist[i+2,j+1])+sum(pixellist[i,j+1])+sum(pixellist[i+1,j+2])+sum(pixellist[i+1,j]))/12-sum(pixellist[i+1,j+1])/3)
				pixelnew[i+1,j+1]=tuple(x-difference for x in pixellist[i+1,j+1])
			else:
				difference=abs((sum(pixellist[i+2,j+1])+sum(pixellist[i,j+1])+sum(pixellist[i+1,j+2])+sum(pixellist[i+1,j]))/12-sum(pixellist[i+1,j+1])/3)
				pixelnew[i+1,j+1]=tuple(x+difference for x in pixellist[i+1,j+1])
        else:
            pixelnew[i,j] = pixellist[i,j]




img.save('answer3.tif')

