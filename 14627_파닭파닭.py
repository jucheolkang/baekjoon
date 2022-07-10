import sys
input = sys.stdin.readline

s, c = map(int,input().split())
cm = []

for i in range(s):
    cm.append(int(input()))

    
end = max(cm)
start = 1
r = 0
while start<= end:
    min = (start+end)//2
    cnt = 0
    
    for x in cm:
        cnt += x//min
        

    if cnt>=c:
        start=min+1
        r = max(r,min)
    else : 
        end = min-1
res = sum(cm) - (c * r)
print(res)