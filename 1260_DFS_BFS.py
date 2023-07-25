# DFS와 BFS

# 트리만들기 (노베이스)

node, edge, base = map(int,input().split())
tree = {}

for i in range(1,node+1):
    tree[i] = []

for _ in range(edge):
    n1, n2 = map(int,input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

print(tree)

# 탐색함수 만들기 (경험 있음)\
visited_node = [base]

while visited_node:

    