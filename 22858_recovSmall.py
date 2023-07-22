# 원상 복구 (small)
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

result_list =list(map(int,input().split()))
D_list = list(map(int,input().split()))
origin_list = list(range(N)) # 정렬된 origin_list를 주어진 규칙대로 섞어서 결과값과 비교

for k in range(K):
    shuf_list = []
    for d in D_list:
        shuf_list.append(origin_list[d-1])
    origin_list = shuf_list

results = sorted(zip(origin_list,result_list))

for result in results:
    print(result[1], end =' ')
