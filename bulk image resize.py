import os

from PIL import Image

# images = os.listdir('images')
# for image in images:
#     if image != '.DS_Store':
#         img = Image.open('images/'+image)
#         h,w = img.size
#         width = 400
#         ratio = width/w
#         height = int(ratio * h)
#         resized = img.resize((width,height))
# #         resized.save('new image/'+image)
# new_iamge = os.listdir('new image')
# for i in new_iamge:
#     abc = Image.open('new image/'+i)
#     print(abc.size)
file = open('all about list.py')
content = file.read()
print(content)

