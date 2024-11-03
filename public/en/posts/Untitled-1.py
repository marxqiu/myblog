import re 
import os
print(os.getcwd())

# the input obsedian file name
input_fname = '2024-06-25-Diffusion-Model.md'

# output file name
output_fname = '2024-06-25-Diffusion-Model-1.md'

# image directory
image_dir = '/media/'

# reaf file
f = open(input_fname, 'r')
txt = f.read()

# this line is from 4castle: https://stackoverflow.com/a/38645273
txt = re.sub(r'\$([^$]*)\$', r'`$\1$`', txt)

txt = re.sub(r'`\$\$`([^$]*)`\$\$`', r'`$$\1$$`', txt)

# replace ![[ with ![](/image/
txt = re.sub(r'!\[\[', f'![]({image_dir}', txt)
# replace ]] with )
txt = re.sub(r'\]\]', ')', txt)

with open(output_fname, 'w') as f:
    f.write(txt)