if __name__ == '__main__':
    
    input_list = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        input_list.append([name, score])
    
    student = sorted(input_list, key=lambda x: x[0])
    
    min = 101
    score = []
    for n, s in student:
        score.append(s)
        if s <= min:
            min = s
        
    score = sorted(list(set(score)))
    for n, s in student:
        if s == score[1]:
            print(n)
