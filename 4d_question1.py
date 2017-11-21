from PIL import Image

#set size

imagewidth=64
imageheight=64


pixellist=[(255,255,255)]*imagewidth*imageheight #load all white image
for i in range((imagewidth*imageheight)/2): #put in black pattern
	pixellist[2*i]=(0,0,0)
	


#create image
img=Image.new('RGB',(imagewidth,imageheight))
img.putdata(pixellist)
img.save('answer.png', dpi=(25,25))#set dpi so 1 mm = 1 pixel

