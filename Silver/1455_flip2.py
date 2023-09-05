# 뒤집기 2

def flip(row, col):
    for r in range(row+1):
        for c in range(col+1):
            arr[r][c] = arr[r][c] ^ 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(i+1):
        if arr[N-1-j][M-1-i+j] == 1:
            cnt += 1
            flip(N-1-j, M-1-i+j)
for i in range(N-2,-1,-1):
    for j in range(i+1):
        if arr[i][j] == 1:
            cnt += 1
            flip(i, j)
for a in arr:
    print(*a)
print(cnt)