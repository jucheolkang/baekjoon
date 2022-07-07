import sys
a = int(input())
b=[]
for i in range(a):
    b .append(int(sys.stdin.readline()))
b.sort(reverse=True)
for i in b:
    print(i, end='\n')