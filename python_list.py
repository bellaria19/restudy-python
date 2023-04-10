import sys

if __name__ == '__main__':
    N = int(input())
    
    arr = list()
    for _ in range(N):
        command, *value = sys.stdin.readline().split()
        
#        match command:
#            case 'insert':
#                arr.insert(int(value[0]), int(value[1]))
#            case 'print':
#                print(arr)
#            case 'remove':
#                arr.remove(int(value[0]))
#            case 'append': 
#                arr.append(int(value[0]))
#            case 'sort':
#                arr.sort() 
#            case 'pop': 
#                arr.pop()
#            case 'reverse': 
#                arr.reverse()
                
                
        if command == 'insert':
                arr.insert(int(value[0]), int(value[1]))
        elif command== 'print':
                print(arr)
        elif command == 'remove':
                arr.remove(int(value[0]))
        elif command == 'append':
                arr.append(int(value[0]))
        elif command == 'sort':
                arr.sort() 
        elif command == 'pop':
                arr.pop()
        elif command == 'reverse':
                arr.reverse()