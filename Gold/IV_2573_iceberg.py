# 빙산
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(row, col):
    pass


N, M = map(int,input().split())
iceberg = []
visited = []
for r in range(N):
    temp = list(map(int,input().split()))
    visited.append([0]*M)
    for c in range(M):
        if temp[c]:
            visited[r][c] += 1
    


for r in range(1, N-1):
    for c in range(1, M-1):
        pass