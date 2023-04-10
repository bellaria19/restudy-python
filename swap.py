def swap_case(s):
    res = []
    for chr in s:
        if chr.isupper():
            tmp = str.lower(chr)
        else:
            tmp = str.upper(chr)  
        res.append(tmp)
        
    res_str = ''.join(map(str, res))

    return res_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)