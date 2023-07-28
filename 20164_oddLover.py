# 홀수 홀릭 호석
import sys
input = sys.stdin.readline

N = input()

num = N

min_value = -1
max_value = -1

for case in range(len(N)*(len(N)-1)//2):

    count = 0
    is_num_unique = False

    while True :

        n_num = 0
        
        for c in num:
            if int(c) % 2:
                count += 1

        if len(num) >= 3:
            for i in range(1,len(num)):
                for j in range(i, len(num)):
                    if i == j :
                        continue
                    n_num += int(num[:i]) + int(num[i:j]) + int(num[j:])
        elif len(num) == 2:
            n_num = int(num[0]) + int(num[1])
        else:
            n_num = int(num) # 이 부분 다시 짜기
            is_num_unique = True

        num = n_num

        if is_num_unique:
            break        

        

