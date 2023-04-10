

def split_and_join(line):
    split_line = line.split()
    join_line = '-'.join(split_line)
    return join_line
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)