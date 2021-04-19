from PIL import Image
import random

def set_attributes(i):
    
    id=i
    _background=(random.randint(0, 3))
    _outershape=0
    _body=(random.randint(0, 4)) 
    _bottomhead=(random.randint(0, 4)) 
    _tophead=(random.randint(0, 4)) 
    _spots=(random.randint(0, 4)) 
    
    return [id,_background,_outershape,_body, _bottomhead, _tophead, _spots] 
    

def create_image(img_attributes):

    img_created = Image.open('img/background/'+str(img_attributes[1])+'.png', 'r')
    img_created = img_created.convert("RGBA")

    img_outershape = Image.open('img/outershape/'+str(img_attributes[2])+'.png', 'r')
    img_outershape = img_outershape.convert("RGBA")

    img_body = Image.open('img/body/'+str(img_attributes[3])+'.png', 'r')
    img_body = img_body.convert("RGBA")

    img_bottomhead = Image.open('img/bottomhead/'+str(img_attributes[4])+'.png', 'r')
    img_bottomhead = img_bottomhead.convert("RGBA")

    img_tophead = Image.open('img/tophead/'+str(img_attributes[5])+'.png', 'r')
    img_tophead = img_tophead.convert("RGBA")

    img_spots = Image.open('img/spots/'+str(img_attributes[6])+'.png', 'r')
    img_spots = img_spots.convert("RGBA")
    
    img_created.paste(img_outershape,(0, 0),img_outershape)
    img_created.paste(img_body,(0, 0),img_body)
    img_created.paste(img_bottomhead,(0, 0),img_bottomhead)
    img_created.paste(img_tophead ,(0, 0),img_tophead )
    img_created.paste(img_spots,(0, 0),img_spots)

    
    img_created.save('img/mushs/Mush_number'+str(img_attributes[0])+'.png')


img_attributes=[0,0,0,0,0,0]

i = 0
while i < 50:
  img_attributes=set_attributes(i) #give randomly the mushroom attributes
  create_image(img_attributes) #create the image 
  
  i += 1

print('Finished!')
