import sys

N = sys.stdin.readline().rstrip()
if int(N) < 10:
    N = "0" + N

tmp = N
cnt = 0

while True:
    sum_num = str(int(tmp[0]) + int(tmp[1]))
    if int(sum_num ) < 10:
        sum_num  = "0" + sum_num 
    tmp = tmp[1] + sum_num[1]

    cnt += 1
    if int(tmp) == int(N):
        break
    
print(cnt)