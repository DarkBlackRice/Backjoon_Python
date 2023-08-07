# 홀수 홀릭 호석

def count_odd(string):
    cnt = 0
    for n in string:
        if int(n) % 2:
            cnt += 1
    return cnt


def dfs(string, cnt):
    if len(string) == 1:
        global ans
        ans.append(cnt + count_odd(string))
        return
    
    elif len(string) == 2:
        n_str = str(int(string[0]) + int(string[1]))
        dfs(n_str, cnt + count_odd(string))

    elif len(string) >= 3:
        for i in range(1, LENGTH-1):
            for j in range(i+1, LENGTH):
                n_str = str(int(string[:i]) + int(string[i:j]) + int(string[j:]))
                dfs(n_str, cnt + count_odd(string))

N = input()
LENGTH = len(N)

max_v = min_v = 0
ans = []
dfs(N, 0)
print(ans)
