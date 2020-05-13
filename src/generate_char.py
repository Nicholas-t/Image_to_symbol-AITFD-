from PIL import Image, ImageDraw, ImageFont
import os

#============================= 
# initialize
#=============================

N = 500
size_image = width_image, height_image = N, N
font_path = './src/Roboto-Light.ttf'
font = ImageFont.truetype(font_path, size=N)

SPECIAL = {
    '*' : 'star',
    '|' : 'vert-line',
    '"' : 'double-quot',
    '<' : 'less',
    '>' : 'greater',
    "'" : 'single-quot',
    '?' : 'question',
    '\\' : 'slash1', 
    '/' : 'slash2'
}

dic = {}

with open('CHARS.txt', 'r') as file:
    lines = file.readlines()
    for lin in lines:
        lin = lin.strip('\n')
        cat, val = lin[:lin.index('=')], lin[lin.index('=')+1:]
        dic[cat] = val
#============================= 

for (cat, val) in dic.items():
    for t in val:
        print('generating for ', t)
        img = Image.new('RGB', size_image, color='white')
        draw = ImageDraw.Draw(img)
        width_text, height_text = draw.textsize(t, font)
        offset_x, offset_y = font.getoffset(t)
        width_text += offset_x
        height_text += offset_y

        top_left_x = width_image / 2 - width_text / 2
        top_left_y = height_image / 2 - height_text / 2
        xy = top_left_x, top_left_y

        draw.text(xy, t, font=font, fill="black")
        if t in SPECIAL.keys():
            t = SPECIAL[t]
        try :
            if (cat == 'ALPHA') & (t.capitalize() == t):
                img.save("./CHARS/"+cat+'-cap-'+str(t)+".png")
            else:
                img.save("./CHARS/"+cat+'-'+str(t)+".png")
        except:
            img.save("./CHARS/"+cat+'-'+SPECIAL[t]+".png")
