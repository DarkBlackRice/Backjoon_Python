# 배열 돌리기 1

# 함수부

def rotate(row,col,arr):
    temp_arr = [ [0]*col for _ in range(row)]

    for r in range(row//2):
        for c in range(col):
            if c < r:
                temp_arr[r][c] = arr[r-1][c]
            elif c > M-(r+2):
                temp_arr[r][c] = arr[r+1][c]
            else:
                temp_arr[r][c] = arr[r][c+1]
    for r in range(row//2,row):
        for c in range(col):
            if c < M - r:
                temp_arr[r][c] = arr[r-1][c]
            elif c > M-(N-r):
                temp_arr[r][c] = arr[r+1][c]
            else:
                temp_arr[r][c] = arr[r][c-1]

    return temp_arr
    


# 실행부

N, M, R = map(int,input().split())

input_arr = [list(map(int,input().split())) for _ in range(N)]

for r in range(R):
    input_arr = rotate(N,M,input_arr)

for i in range(N):
    print(*input_arr[i])