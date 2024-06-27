"""
Convert the given images in a folder into pdf using img2pdf library. Images are
available in ./images folder. Generated pdf should be stored at the current
directory.
"""
import os 
import img2pdf

a4input = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
layout = img2pdf.get_layout_fun(a4input)

img_path = './images'
output_file_path = 'output.pdf'

img_list = os.listdir(img_path)

img_path_list = []

for img in img_list:
  img_path_list.append(os.path.join(img_path, img))


pdf_bytes = img2pdf.convert(img_path_list, layout_fun=layout)
with open(output_file_path, "wb") as f:
    f.write(pdf_bytes)

print("successfully converted to pdf.")