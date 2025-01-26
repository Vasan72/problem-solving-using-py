def split_and_join(line):
    splited_str = line.split(" ")
    joined_line = "-".join(splited_str)
    return joined_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
