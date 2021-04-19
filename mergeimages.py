from PIL import Image


new_image = Image.new('RGB',(8*180, 3*180), (250,250,250))


image_x= 0


i = 1
for i in range(8):
	image1= Image.open('img/mushs/Mush_number'+str(i)+'.png', 'r')
	image1 = image1.resize((180, 180))
	new_image.paste(image1,(image_x,0))
	image_x= image_x+ 180
	i+1

image_x= 0


i = 1
for i in range(8,16):
	image1= Image.open('img/mushs/Mush_number'+str(i)+'.png', 'r')
	image1 = image1.resize((180, 180))
	new_image.paste(image1,(image_x,180))
	image_x= image_x+ 180
	i+1

image_x= 0


i = 1
for i in range(16,24):
	image1= Image.open('img/mushs/Mush_number'+str(i)+'.png', 'r')
	image1 = image1.resize((180, 180))
	new_image.paste(image1,(image_x,2*180))
	image_x= image_x+ 180
	i+1

new_image.save('img/mushs/Mush_merge.png')
