import sys
input = sys.stdin.readline

num = int(input())
money = list(map(int, input().split()))
total = int(input())

money.sort()
start = 0
end = money[len(money)-1]

while start <= end:
    min = (start + end)//2
    n = 0
    
    for i in money:
        if i >= min: 
            n += min
        else: n += i
    
    if n <= total: 
        start = min + 1
    else: end = min - 1
print(end)