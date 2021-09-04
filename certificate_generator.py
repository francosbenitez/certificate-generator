import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

os.chdir('C:/Users/Usuario/Documents/GitHub/certificate-generator')
data = pd.read_excel (r'students.xlsx') 
name_list = data["Name"].tolist() 

for i in name_list:
    img = Image.open(r'certificate_base.png')
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r"merriweather.ttf", 46)
    w, h = draw.textsize(i, font)
    left = (img.width - w) / 2
    location = (left, 320)
    text_color = (33, 54, 101)
    draw.text(location, i, fill = text_color, font = font)
    img.save("certificates\\certificate_" + i + ".pdf")
    
