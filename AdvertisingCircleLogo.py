from PIL import Image, ImageDraw
import math
im = Image.new("RGBA",(500,500),(0,0,0,0))
draw = ImageDraw.Draw(im)
the_number = 5
l = math.pi/16
colorFill = (255,255,0,255)
colorOutline = (255,255,0,255)
for i in range(the_number):
    angle = math.pi/the_number*i * 2 - math.pi/2
    draw.polygon( 
        (
            (250,250), 
            (100*math.cos(angle+l)+250,100*math.sin(angle+l)+250) ,
            (100*math.cos(angle-l)+250,100*math.sin(angle-l)+250)
        ), 
            fill=colorFill, outline=colorOutline
    )
    draw.polygon(
        (
            (100*math.cos(angle+l*2)+250,100*math.sin(angle+l*2)+250),
            (125*math.cos(angle)+250,125*math.sin(angle)+250),
            (100*math.cos(angle-l*2)+250,100*math.sin(angle-l*2)+250),
        ),
        fill=colorFill, outline=colorOutline
    )
    draw.ellipse((240,240,260,260), fill=colorFill, outline=colorOutline)
im.save("advertisement_circle_logo.png",quality=96)