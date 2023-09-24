n = int(input())
p = list(map(int,input().split()))
add = int()
sum = int()
p.sort()
for i in range(n):
    add = add + p[i]
    sum += add
print(sum)