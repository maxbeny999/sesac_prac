import sys
from collections import deque

# 현재: n = int(sys.stdin.readline()) -> 숫자 하나만 받음   
# 한 줄에 숫자 하나만 들어오는 경우 (N 입력)
# 문제: "7 3" 처럼 두 개가 들어옴 (N, K)
# 입력이 공백(띄어쓰기)로 구분되어 들어오면 split() 사용

n, k = map(int, sys.stdin.readline().split())

dq = deque(range(1, n + 1))
result =[]

while len(dq) > 0:
    dq.rotate(-(k-1))
    poped = dq.popleft()
    result.append(poped)

print("<" + ", ".join(map(str, result)) + ">")

