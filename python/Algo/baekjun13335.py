import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().split())
trucks = deque(list(map()))

# 다리 라는 정보를 가지고 있습니다.
# 길이 w 짜리 더미 데이터를 만들 것. 0 : 트럭이 올라갈 수 있는 곳
bridge = deque([0] * w)

# bridge 위의 트럭이 움직입니다.
# 왼쪽 트럭이 성공적으로 이동
exit_truck = bridge.popleft()
weight -= exit_truck 
# 트럭에서 빼다가 bridge로 이동시킵니다
    # 무게가 가능할때만 이동합니다.
if weight + trucks[0] <= L:
    bridge.append(trucks)

