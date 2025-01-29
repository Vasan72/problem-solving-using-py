import re

for i in range(int(input())):
    s = input().split()
    mail = re.search(r"<([A-Za-z][\w\.-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})>", s[1])
    if mail:
        print(s[0], mail.group())
