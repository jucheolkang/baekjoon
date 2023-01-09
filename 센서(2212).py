import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
arr = list(map(int,input().split()))
arr.sort()
if k >= n:
    print(0)
    sys.exit()

a = []
for i in range(1,n):
    a.append(arr[i]-arr[i-1])
a.sort(reverse=True)
for _ in range(k-1):
    a.pop(0)

print(sum(a))
