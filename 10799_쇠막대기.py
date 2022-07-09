import sys
input = sys.stdin.readline
a = list(input())
b = []
count = 0
for i in a:
    if i == "(":
        b.append(i)
    elif i == ")":
        b.pop()
        count+=1
print(count)
