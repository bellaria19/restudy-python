def print_formatted(number):
    for i in range(1, number + 1):
        length= len(format(number, 'b'))
        print(format(i,'d').rjust(length), format(i, 'o').rjust(length), format(i, 'X').rjust(length), format(i, 'b').rjust(length))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)