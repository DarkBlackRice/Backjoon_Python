# 열쇠

from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(row, col):
    global ans
    q = deque([(row, col)])
    visited[row][col] = v_count
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = r + dc[i]
            if (0 <= nr < h) and (0 <= nc < w)\
                and room_map[r][c] != '*'\
                and not room_map[r][c].isupper\
                and visited[nr][nc] != v_count:
                q.append((nr, nc))
                visited[nr][nc] = v_count
                if room_map[nr][nc].islower():
                    key_set.add(room_map[r][c])
                elif room_map[nr][nc] == '$':
                    ans += 1



T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    room_map = [list(input()) for _ in range(h)]
    visited = [[-1] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if room_map[r][c] == '.':
                visited[r][c] = 0

    v_count = 0
    ans = 0

    key_set = set(input())
    
    while key_list:
        key_list = list(key_set)
        for key in key_list:
            key_ord = ord(key)
            for r in range(h):
                for c in range(w):
                    if ord(room_map[r][c]) == key_ord - 32:
                        room_map[r][c] = '.'
        key_set = set()
        v_count += 1
        for r in range(h):
            for c in range(w):
                if visited[r][c] != -1 and visited[r][c] != v_count:
                    bfs(r, c)