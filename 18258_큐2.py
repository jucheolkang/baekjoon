import sys
from collections import deque
input = sys.stdin.readline
roof = int(input())
b = deque([])
for i in range(roof):
    a = list(input().split())
    if a[0] == "push":
        b.append(a[1])
    elif a[0] == "pop":
        if len(b)>0:
            print(b.popleft())
        else: 
            print(-1)
    elif a[0] == "size":
        print(len(b))
    elif a[0] == "empty":
        if len(b) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(b)>0:
            print(b[0])
        else: 
            print(-1)
    elif a[0] == "back":
        if len(b)>0:
            print(b[-1])
        else: 
            print(-1)
