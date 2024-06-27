"""
Rename all the images in the ./images folder. There are images of .jpg, .png
extensions. The images should be renamed to 001_image.jpg(or .png according to 
original extension), 002_image.jpg and so on.
"""

import os

# specify the path where images are located. In this case, it is located at
# images folder in the current directory.
img_path = "./images"

img_lists = os.listdir(img_path) #list dinxa ni ta yesle

count = 0 
#list ma iterate garxau to access each and every image in the list.
for img in img_lists:
  count = count+1
  num = str(count).zfill(3)
  name, ext = os.path.splitext(img)
  new_name = f'{num}_{name}' + ext
  source = os.path.join(img_path, img) # constructin path
  destination = os.path.join(img_path, new_name)
  os.rename(source, destination)

