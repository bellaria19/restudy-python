from itertools import product

lst = []
for _ in range (2):
    k = list(map(int, input().split()))
    lst.append(sorted(k))


t_lst = product(*lst)
for it in t_lst:
    print(it, end= " ")