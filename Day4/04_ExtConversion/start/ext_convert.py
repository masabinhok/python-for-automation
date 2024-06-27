"""
Convert all the png images to jpg in a given source folder and store the converted image to the target folder.
"""
import os 
from PIL import Image




source_folder = './source_images'
target_folder = './target_images'

if not os.path.exists(target_folder):
  os.makedirs(target_folder)

images = os.listdir(source_folder)

for image in images:
  if image.endswith('.png'):
    base=os.path.splitext(image)[0]

    new_name = base + '.jpg'
    
    img_path = os.path.join(source_folder, image)

    img = Image.open(img_path).convert('RGB')

    dest_img_path = os.path.join(target_folder, new_name)

    img.save(dest_img_path)

print("extension conversion completed")