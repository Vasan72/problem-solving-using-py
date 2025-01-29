import re

pattern = r"^[7-9]\d{9}$"
N = int(input())
mobile_no = []

if 1 <= N <= 10:
    for n in range(N):
        user_input = input()
        mobile_no.append(user_input)
        
    for no in mobile_no:
        if re.match(pattern, no) and 2 <= len(no) <= 10:
            print('YES')
        else:
            print("NO")
