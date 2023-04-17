if __name__ == '__main__':
    s = input()
    
    check_list = [False, False, False, False, False]

    for c in s:
        if c.isalnum():
            check_list[0] = True
            break
    
    for c in s:
        if c.isalpha():
            check_list[1] = True
            break
        
    for c in s:
        if c.isdigit():
            check_list[2] = True
            break
        
    for c in s:
        if c.islower():
            check_list[3] = True
            break
            
    for c in s:
        if c.isupper():
            check_list[4] = True
            break
        
    for check in check_list:
        print(check)