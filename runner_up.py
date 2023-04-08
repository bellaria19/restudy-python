if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(list(arr))
    
    max = -101
    max_2 = max
    for i in range(0, len(arr)):
        if arr[i] > max:
            max_2 = max
            max = arr[i]
    
    print(max_2)
    