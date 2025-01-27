if __name__ == '__main__':
    my_list = []
    N = int(input())
    
    for _ in range(N):
        command = input().split()
        cmd = command[0]
        arg = list(map(int,command[1:]))
        
        if cmd =="insert":
            my_list.insert(arg[0],arg[1])
        elif cmd == 'print':
            print(my_list)
        elif cmd == 'remove':
            my_list.remove(arg[0])
        elif cmd == 'append':
            my_list.append(arg[0])
        elif cmd == 'sort':
            my_list.sort()
        elif cmd == 'pop':
            my_list.pop()
        elif cmd == 'reverse':
            my_list.reverse()
    
     
