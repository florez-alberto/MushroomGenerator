from PIL import Image
import random

def set_attributes(i):
    
    id=i
    mush_shape=0
    mush_color1=(random.randint(0, 4)) 
    mush_color2=(random.randint(0, 4)) 
    mush_eyes=(random.randint(0, 3)) 
    mush_accessories=0
    
    return [id,mush_shape,mush_color1,mush_color2,mush_eyes,mush_accessories] 
    

def create_image(img_attributes):

    img_created = Image.open('img/background.png', 'r')
    img_created = img_created.convert("RGBA")
    img_shape = Image.open('img/shape/'+str(img_attributes[1])+'.png', 'r')
    img_shape = img_shape.convert("RGBA")
    img_color1 = Image.open('img/color1/'+str(img_attributes[2])+'.png', 'r')
    img_color1 = img_color1.convert("RGBA")
    img_color2 = Image.open('img/color2/'+str(img_attributes[3])+'.png', 'r')
    img_color2 = img_color2.convert("RGBA")
    img_eyes = Image.open('img/eyes/'+str(img_attributes[4])+'.png', 'r')
    img_eyes = img_eyes.convert("RGBA")
    img_accessories = Image.open('img/accessories/'+str(img_attributes[5])+'.png', 'r')
    img_accessories = img_accessories.convert("RGBA")
    
    img_created.paste(img_shape,(0, 0),img_shape)
    img_created.paste(img_color1,(0, 0),img_color1)
    img_created.paste(img_color2,(0, 0),img_color2)
    img_created.paste(img_eyes,(0, 0),img_eyes)
    img_created.paste(img_accessories,(0, 0),img_accessories)

    
    img_created.save('img/mushs/Mush_number'+str(img_attributes[0])+'.png')


img_attributes=[0,0,0,0,0,0]

i = 0
while i < 20:
  img_attributes=set_attributes(i) #give randomly the mushroom attributes
  create_image(img_attributes) #create the image 
  
  i += 1

print('Finished!')
