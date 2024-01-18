from PIL import Image,ImageDraw,ImageFont
img = Image.open('image processing/nature image.jpg')
text = 'Hello Bangladesh'
font = ImageFont.truetype('loveyou.otf',128)
draw = ImageDraw.Draw(img)
draw.text((200,200),text=text, font=font, fill='RED')
img.show()