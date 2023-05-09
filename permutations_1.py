from itertools import permutations

s, n = input().split()

per = permutations(sorted(s), int(n))

for it in per:
    for k in it:
        print(k, end='')
    print()