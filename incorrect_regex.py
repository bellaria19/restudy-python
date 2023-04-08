import sys
import re

for _ in range(int(sys.stdin.readline())):
    input = sys.stdin.readline()
    try:
        m = re.compile(input)
        print(True)
    except:
        print(False)
