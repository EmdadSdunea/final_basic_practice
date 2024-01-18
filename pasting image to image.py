import random

from PIL import Image

number1 = random.randint(0, 255)
number2 = random.randint(0, 255)
number3 = random.randint(0, 255)
background = Image.new('RGB', (600, 600), (number3, number1, number2))
main_imge = Image.open('image processing/abc.jpg')
h,w = main_imge.size
ratio = h/w
print(ratio)
print(h,w)
width = int(200*ratio)
height = int(200*ratio)
resized_image = main_imge.resize((height,width))
print(resized_image.size)
background.paste(resized_image,(200,200))
background.show()