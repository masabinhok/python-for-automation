"""
Compress the given file using gzip.
"""
import os 
import shutil
import gzip

input_file_path = '../../04_ExtConversion/end/ext_convert.py'
output_file_path = 'ext_convert.py.gz'

with open (input_file_path, 'rb') as f_in:
  with gzip.open(output_file_path, 'wb', compresslevel=9) as f_out:
    shutil.copyfileobj(f_in, f_out)

in_size = os.path.getsize(input_file_path)
out_size = os.path.getsize(output_file_path)


print(f"Input file size: {in_size}")
print(f"Output file size: {out_size}")