from PIL import Image

#set size

im=Image.open('puppy.jpg')
pixellist = im.load()

img = Image.new( im.mode, im.size)
pixelnew = img.load()
for i in range(img.size[0]-2):
    for j in range(img.size[1]-2):
        if abs((sum(pixellist[i+2,j+1])+sum(pixellist[i,j+1])+sum(pixellist[i+1,j+2])+sum(pixellist[i+1,j])+sum(pixellist[i+2,j+2])+sum(pixellist[i+2,j])+sum(pixellist[i,j+2])+sum(pixellist[i,j]))/24-sum(pixellist[i+1,j+1])/3)>10:#compare to surrounding pixels
		#replace brightness of highest and lowest pixels with 5 remaining
			ninepixels=[pixellist[i+1,j+1],pixellist[i,j+1],pixellist[i+1,j],pixellist[i+2,j+2],pixellist[i,j+2],pixellist[i+2,j],pixellist[i,j],pixellist[i+1,j+2],pixellist[i+2,j+1]]
			brightness=[sum(a)/3 for a in ninepixels]
			brightness.sort()
			averageoffive=sum(brightness[2:7])/5
			lowest1=brightness[0]
			lowest2=brightness[1]
			highest1=brightness[7]
			highest2=brightness[8]
			if sum(pixellist[i+1,j+1])/3==lowest1:#1
				pixelnew[i+1,j+1]=tuple(x+(averageoffive-lowest1) for x in pixellist[i+1,j+1])
			elif sum(pixellist[i+1,j+1])/3==lowest2:
				pixelnew[i+1,j+1]=tuple(x+(averageoffive-lowest2) for x in pixellist[i+1,j+1])
			elif sum(pixellist[i+1,j+1])/3==highest2:
				pixelnew[i+1,j+1]=tuple(x+(highest2-averageoffive) for x in pixellist[i+1,j+1])
			elif sum(pixellist[i+1,j+1])/3==highest1:
				pixelnew[i+1,j+1]=tuple(x+(highest1-averageoffive) for x in pixellist[i+1,j+1])
			
			if sum(pixellist[i+1,j])/3==lowest1:#2
				pixelnew[i+1,j]=tuple(x+(averageoffive-lowest1) for x in pixellist[i+1,j])
			elif sum(pixellist[i+1,j])/3==lowest2:
				pixelnew[i+1,j]=tuple(x+(averageoffive-lowest2) for x in pixellist[i+1,j])
			elif sum(pixellist[i+1,j])/3==highest2:
				pixelnew[i+1,j]=tuple(x+(highest2-averageoffive) for x in pixellist[i+1,j])
			elif sum(pixellist[i+1,j])/3==highest1:
				pixelnew[i+1,j]=tuple(x+(highest1-averageoffive) for x in pixellist[i+1,j])
				
			if sum(pixellist[i,j+1])/3==lowest1:#3
				pixelnew[i,j+1]=tuple(x+(averageoffive-lowest1) for x in pixellist[i,j+1])
			elif sum(pixellist[i,j+1])/3==lowest2:
				pixelnew[i,j+1]=tuple(x+(averageoffive-lowest2) for x in pixellist[i,j+1])
			elif sum(pixellist[i,j+1])/3==highest2:
				pixelnew[i,j+1]=tuple(x+(highest2-averageoffive) for x in pixellist[i,j+1])
			elif sum(pixellist[i,j+1])/3==highest1:
				pixelnew[i,j+1]=tuple(x+(highest1-averageoffive) for x in pixellist[i,j+1])
				
			if sum(pixellist[i,j])/3==lowest1:#4
				pixelnew[i,j]=tuple(x+(averageoffive-lowest1) for x in pixellist[i,j])
			elif sum(pixellist[i,j])/3==lowest2:
				pixelnew[i,j]=tuple(x+(averageoffive-lowest2) for x in pixellist[i,j])
			elif sum(pixellist[i,j])/3==highest2:
				pixelnew[i,j]=tuple(x+(highest2-averageoffive) for x in pixellist[i,j])
			elif sum(pixellist[i,j])/3==highest1:
				pixelnew[i,j]=tuple(x+(highest1-averageoffive) for x in pixellist[i,j])
				
			if sum(pixellist[i+2,j])/3==lowest1:#5
				pixelnew[i+2,j]=tuple(x+(averageoffive-lowest1) for x in pixellist[i+2,j])
			elif sum(pixellist[i+2,j])/3==lowest2:
				pixelnew[i+2,j]=tuple(x+(averageoffive-lowest2) for x in pixellist[i+2,j])
			elif sum(pixellist[i+2,j])/3==highest2:
				pixelnew[i+2,j]=tuple(x+(highest2-averageoffive) for x in pixellist[i+2,j])
			elif sum(pixellist[i+2,j])/3==highest1:
				pixelnew[i+2,j]=tuple(x+(highest1-averageoffive) for x in pixellist[i+2,j])
				
			if sum(pixellist[i+1,j+2])/3==lowest1:#6
				pixelnew[i+1,j+2]=tuple(x+(averageoffive-lowest1) for x in pixellist[i+1,j+2])
			elif sum(pixellist[i+1,j+2])/3==lowest2:
				pixelnew[i+1,j+2]=tuple(x+(averageoffive-lowest2) for x in pixellist[i+1,j+2])
			elif sum(pixellist[i+1,j+2])/3==highest2:
				pixelnew[i+1,j+2]=tuple(x+(highest2-averageoffive) for x in pixellist[i+1,j+2])
			elif sum(pixellist[i+1,j+2])/3==highest1:
				pixelnew[i+1,j+2]=tuple(x+(highest1-averageoffive) for x in pixellist[i+1,j+2])
				
			if sum(pixellist[i+2,j+2])/3==lowest1:#7
				pixelnew[i+2,j+2]=tuple(x+(averageoffive-lowest1) for x in pixellist[i+2,j+2])
			elif sum(pixellist[i+2,j+2])/3==lowest2:
				pixelnew[i+2,j+2]=tuple(x+(averageoffive-lowest2) for x in pixellist[i+2,j+2])
			elif sum(pixellist[i+2,j+2])/3==highest2:
				pixelnew[i+2,j+2]=tuple(x+(highest2-averageoffive) for x in pixellist[i+2,j+2])
			elif sum(pixellist[i+2,j+2])/3==highest1:
				pixelnew[i+2,j+2]=tuple(x+(highest1-averageoffive) for x in pixellist[i+2,j+2])
				
				
			if sum(pixellist[i+2,j+1])/3==lowest1:#8
				pixelnew[i+2,j+1]=tuple(x+(averageoffive-lowest1) for x in pixellist[i+2,j+1])
			elif sum(pixellist[i+2,j+1])/3==lowest2:
				pixelnew[i+2,j+1]=tuple(x+(averageoffive-lowest2) for x in pixellist[i+2,j+1])
			elif sum(pixellist[i+2,j+1])/3==highest2:
				pixelnew[i+2,j+1]=tuple(x+(highest2-averageoffive) for x in pixellist[i+2,j+1])
			elif sum(pixellist[i+2,j+1])/3==highest1:
				pixelnew[i+2,j+1]=tuple(x+(highest1-averageoffive) for x in pixellist[i+2,j+1])
				
			if sum(pixellist[i,j+2])/3==lowest1:#9
				pixelnew[i,j+2]=tuple(x+(averageoffive-lowest1) for x in pixellist[i,j+2])
			elif sum(pixellist[i,j+2])/3==lowest2:
				pixelnew[i,j+2]=tuple(x+(averageoffive-lowest2) for x in pixellist[i,j+2])
			elif sum(pixellist[i,j+2])/3==highest2:
				pixelnew[i,j+2]=tuple(x+(highest2-averageoffive) for x in pixellist[i,j+2])
			elif sum(pixellist[i,j+2])/3==highest1:
				pixelnew[i,j+2]=tuple(x+(highest1-averageoffive) for x in pixellist[i,j+2])
        else:
            pixelnew[i,j] = pixellist[i,j]




img.save('answer4.tif')

