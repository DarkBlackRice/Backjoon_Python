# 인구 이동

def ally():
    unions = []
    temp = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for i in range(2):
                nr = r + dr[i]
                nc = c + dc[i]
                if (nr<N and nc<N) and (L<=abs(LAND[r][c] - LAND[nr][nc])<=R):
                    
    return 


N, L, R = map(int,input().split())
LAND = [list(map(int,input().split())) for _ in range(N)]

flag = True
count = 0
dr = [0, 1]
dc = [1, 0]

print('지도 : ')
for country in LAND:
    print(*country)
print()

while flag:

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

    
