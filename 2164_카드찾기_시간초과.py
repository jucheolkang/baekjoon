import sys
input = sys.stdin.readline
num = int(input())
li1 = []
li2 = []
li3 = []
count = 1

for i in range(1,num+1):
    li1.append(i)
while len(li1)>1:
    for j in li1:
        if count%2 == 0:
            li2.append(j)
        count+=1
    li1 = li2
    li2 = li3
    count = 1

print(li1.pop())
