import os
import random

from PIL import Image

i = 0
while i < 20:
    number1 = random.randint(0, 255)
    number2 = random.randint(0, 255)
    number3 = random.randint(0, 255)
    image = Image.new('RGB', (600, 600), (number1, number2, number3))
    image.save('new image/' +'blank_image_'+str(i) + '.png')
    i += 1
