# 기차가 어둠을 헤치고 은하수를
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
train = [[0]*20 for _ in range(N)]
cmds = [list(map(int,input().split())) for _ in range(M)]

for cmd in cmds:
    
