import sys
from collections import deque

# [1. 입력 받기]

# 한 줄에 숫자 하나만 들어오는 경우 (N 입력)
n = int(sys.stdin.readline())

# [2. 내 로직 작성]

dq = deque(range(1, n + 1))
discarded = []

# popped_dq = dq.popleft()
# discarded.append(popped_dq)
# popped_dqn = dq.popleft()
# dq.append(popped_dqn)

# print(popped_dq)
# print(popped_dqn)

# print(dq)

while len(dq) > 1:
    popped_dq = dq.popleft()
    discarded.append(popped_dq)
    popped_dqn = dq.popleft()
    dq.append(popped_dqn)

dq = list(dq)
print(*discarded + dq)


# [3. 출력 하기]
# 문제에서 원하는 정답을 print()로 찍으면 됩니다.
# 리스트에 있는 걸 공백으로 띄워서 출력하려면 * (별표)를 붙입니다.
# 예: print(*discarded, dq[0])