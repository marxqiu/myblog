import re 

# reaf file
f = open('a-framework-for-the-mind.md', 'r')
txt = f.read()

# this line is from 4castle: https://stackoverflow.com/a/38645273
txt = re.sub(r'\$([^$]*)\$', r'`$\1$`', txt)

txt = re.sub(r'`\$\$`([^$]*)`\$\$`', r'`$$\1$$`', txt)
with open('txt.md', 'w') as f:
    f.write(txt)