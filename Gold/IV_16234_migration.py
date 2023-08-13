# 인구 이동

def ally(row, col):
    union = [LAND[row][col],(row,col)]
    stack = [(row,col)]
    while stack:
        r, c = stack.pop()
        visited[r][c] = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0<=nr<N and 0<=nc<N) and not visited[nr][nc]\
                (L<=abs(LAND[r][c] - LAND[nr][nc])<=R):
                stack.append((nr, nc))

                
    return union



N, L, R = map(int,input().split())
LAND = [list(map(int,input().split())) for _ in range(N)]

flag = True
count = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

print('지도 : ')
for country in LAND:
    print(*country)
print()

while flag:

    visited = [[False] * N for _ in range(N)]
    unions = ally()
    
    print('연합 정보 : ')
    for u in unions:
        print(*u)
    
    if unions:
        for u in unions:
            union_num = len(u) - 1
            temp = u[0] // union_num
            for i in range(1, union_num + 1):
                r, c = u[i]
                LAND[r][c] = temp
        count += 1
    else:
        flag = False

    print('지도 : ')
    for country in LAND:
        print(*country)

print(count)

    
