# 트리의 지름
from collections import deque

# 다음 노드와 가중치를 q에 튜플로 묶어 넣어 관리하자
def bfs(n):
    global ans
    q = deque([(n, 0)])
    vst[n] = 0
    while q:
        # v는 현재노드, vw는 n에서 v까지 가는 누적거리
        v, vw = q.popleft()
        # u는 v의 인접노드, uw는 v에서 u까지 넘어가는 거리
        for u, uw in graph[v]:
            if vst[u] == -1:
                # nw는 n에서 w까지 가는 누적거리
                nw = vw + uw
                vst[u] = nw
                q.append((u, nw))



N = int(input())

# 그래프 만들기
graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    arr = list(map(int, input().split()))
    j = 1
    while arr[j] != -1:
        # 0번 원소는 도착노드, 1번 원소는 가중치
        arrived, weight = arr[j], arr[j+1]
        graph[i].append((arrived, weight))
        j += 2

# 전체 노드를 대상으로 bfs탐색을 하자. <-- 이거 안 쓸거임 ㅋㅋ
ans = 0
node1 = -1
vst = [-1] * (N+1)

# 지름 구하는 알고리즘 : 
# 임의의 점에서 가장 먼 점이 1번 지름노드가 되고,
# 1번 지름노드에서 가장 거리가 먼 노드가 2번 지름노드, 해당 거리가 지름이 된다.
bfs(0)
for i in range(1, N+1):
    if ans < vst[i]:
        node1 = i
        ans = vst[i]

vst = [-1] * (N+1)
bfs(node1)
print(max(vst))