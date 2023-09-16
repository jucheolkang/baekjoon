a,b = map(int, input().split())

for i in range(a):
    if a % i == 0:
        b-=1
        if b == 1:
            print(i)