roof = int(input())
graph =[list(map(int,input().split())) for _ in range(roof)]
sum = 0
out = 0
visit = [[0] for _ in range(roof)]

for i in range(roof):
    for j in range(roof):
        if visit[i] == 0 and graph[i][j] !=0:
            