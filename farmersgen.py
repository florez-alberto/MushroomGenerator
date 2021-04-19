from PIL import Image
import random

def set_attributes(i):
    
    id=i
    _background=(random.randint(0, 3))
    _outershape=(random.randint(0, 3))
    _hairs= (random.randint(0, 10))
    _eyes= (random.randint(0, 3))
    _hat= (random.randint(0, 1))
    _mushroom= (random.randint(0, 1))
    _shirt=(random.randint(0, 1))
    _skin=(random.randint(0, 3)) 
    _trousers=0
    
    return [id,_background,_outershape, _hairs, _eyes, _hat, _mushroom, _shirt, _skin, _trousers] 
    

def create_image(img_attributes):

    img_created = Image.open('img/background/'+str(img_attributes[1])+'.png', 'r')
    img_created = img_created.convert("RGBA")

    img_outershape = Image.open('img/outershape/'+str(img_attributes[2])+'.png', 'r')
    img_outershape = img_outershape.convert("RGBA")

    img_hairs= Image.open('img/hairs/'+str(img_attributes[3])+'.png', 'r')
    img_hairs = img_hairs.convert("RGBA")

    img_eyes = Image.open('img/eyes/'+str(img_attributes[4])+'.png', 'r')
    img_eyes = img_eyes.convert("RGBA")

    img_hat= Image.open('img/hat/'+str(img_attributes[5])+'.png', 'r')
    img_hat = img_hat.convert("RGBA")

    img_mushroom = Image.open('img/mushroom/'+str(img_attributes[6])+'.png', 'r')
    img_mushroom = img_mushroom.convert("RGBA")

    img_shirt = Image.open('img/shirt/'+str(img_attributes[7])+'.png', 'r')
    img_shirt = img_shirt.convert("RGBA")

    img_skin = Image.open('img/skin/'+str(img_attributes[8])+'.png', 'r')
    img_skin = img_skin.convert("RGBA")

    img_trousers = Image.open('img/trousers/'+str(img_attributes[9])+'.png', 'r')
    img_trousers= img_trousers.convert("RGBA")
    
    img_created.paste(img_outershape,(0, 0),img_outershape)
    img_created.paste(img_hairs,(0, 0),img_hairs)
    img_created.paste(img_eyes,(0, 0),img_eyes)
    img_created.paste(img_hat,(0, 0),img_hat )
    img_created.paste(img_mushroom,(0, 0),img_mushroom)
    img_created.paste(img_shirt,(0, 0),img_shirt)
    img_created.paste(img_skin,(0, 0),img_skin)
    img_created.paste(img_trousers,(0, 0),img_trousers)

    
    img_created.save('img/mushs/Mush_number'+str(img_attributes[0])+'.png')


img_attributes=[0,0,0,0,0,0,0,0,0,0]

i = 0
while i < 150:
  img_attributes=set_attributes(i) #give randomly the mushroom attributes
  create_image(img_attributes) #create the image 
  
  i += 1

print('Finished!')
