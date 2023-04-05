import sys
import re

pattern = r'^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$'
character = r'[^\w\{\}#]'
n = int(sys.stdin.readline())


res = []
get_color = False
for i in range(n):
    line = sys.stdin.readline()
    line = re.sub(character, ' ', line).split(' ')
    
    for i in line:
        if get_color:
            if bool(re.match(pattern, i)):
                res.append(i)
 
        if i == '{':
            get_color = True
        elif i == '}':
            get_color = False

                
for color in res:
    print(color)

# output format start # symbol
