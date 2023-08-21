# N-Queen 3트

def dfs(k, n, lst):
    global count

    if len(lst) > 1:
        for i in lst:


    if k == n:
        count += 1
        return

    for i in range(N):        
        dfs(k+1, n, lst+[i])

N = int(input())
count = 0
dfs(0, N, [])
print(count)