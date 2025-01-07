if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    remove_dup =set(arr)
    new_arr = list(remove_dup)
    new_arr.sort(reverse=True)
    if len(new_arr) > 1:
        print(new_arr[1])
    else:
        print('No runner-up exists')
