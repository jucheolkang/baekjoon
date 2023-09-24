n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=False)
w = 0
maxR = 0
for i in range(n) : 
    w = ropes[i] * n
    n-=1
    if maxR < w : 
        maxR = w
print(maxR)