from PIL import Image
import random

def set_attributes(i):
    
    id=i
    _backgrounds=(random.randint(0, 7))
    _outshape=0
    _hairs= (random.randint(0, 11))
    _eyes= (random.randint(0, 3))
    
    _mushroom= (random.randint(0, 1))
    _shirt=(random.randint(0, 3))
    _tool=(random.randint(0, 1))
    _skin=(random.randint(0, 3)) 
    _hat= (random.randint(0, 1))
    _trousers=0
    
    return [id,_backgrounds,_outshape, _hairs, _eyes, _mushroom, _shirt,_tool, _skin, _hat, _trousers] 
    

def treat_image (_attribute, _attribute_number):
    image= Image.open('img2/'+_attribute +'/'+str(_attribute_number)+'.png', 'r')
    image= image.resize((720, 720))
    image= image.convert("RGBA")
    return (image)

def create_image(img_attributes):

    img_created = treat_image('backgrounds', img_attributes[1])

    img_outshape = treat_image('outshape', img_attributes[2])

    img_hairs= treat_image('hairs', img_attributes[3])

    img_eyes = treat_image('eyes', img_attributes[4])

    img_mushroom = treat_image('mushrooms', img_attributes[5])

    img_shirt = treat_image('shirt', img_attributes[6])

    img_tool = treat_image('tool', img_attributes[7])

    img_skin = treat_image('skin', img_attributes[8])

    img_hat= treat_image('hat', img_attributes[9])

    img_trousers = treat_image('trousers', img_attributes[10])
    
    img_created.paste(img_outshape,(0, 0),img_outshape)
    img_created.paste(img_eyes,(0, 0),img_eyes)
    img_created.paste(img_mushroom,(0, 0),img_mushroom)
    img_created.paste(img_shirt,(0, 0),img_shirt)
    img_created.paste(img_tool,(0, 0),img_tool)
    img_created.paste(img_skin,(0, 0),img_skin)
    img_created.paste(img_hairs,(0, 0),img_hairs)
    img_created.paste(img_hat,(0, 0),img_hat )
    img_created.paste(img_trousers,(0, 0),img_trousers)

    
    img_created.save('img2/mush_guys/farmer'+str(img_attributes[0])+'.png')


img_attributes=[0,0,0,0,0,0,0,0,0,0,0]

i = 0
while i < 150:
  img_attributes=set_attributes(i) #give randomly the mushroom attributes
  create_image(img_attributes) #create the image 
  
  i += 1

print('Finished!')
