n,k = map(int, input().split())
a = []
count = 0
for i in range(n):
    b = int(input())
    a.append(b)
a.reverse()
while(k != 0):
    for i in a:
        if(i<=k):
            count = count + int(k/i)
            k = k%i
            
print(count)