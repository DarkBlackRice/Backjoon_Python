# N-Queen

def promising_lst(k,lst):

    if k < 1:
         return list(range(N))

    result = []
    for num in range(N):
        for i in range(1, len(lst)):
            for j in [-1, 0 ,1]:
                if num != lst[k-1-i] + j*i:
                     result.append(num)
    return result

def dfs(k, n, lst):
    global count
    if k == n:
        count += 1
        return

    for i in promising_lst(k, lst):        
        dfs(k+1, n, lst+[i])



N = int(input())
count = 0
dfs(0, N, [])
print(count)