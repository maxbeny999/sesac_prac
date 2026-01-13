# 7 

# number = int(input())

# 4 2 10  # n / w / L 
# 7 4 5 6 # list
# input_value = input()
input_value = "4 2 10"
input_value = input_value.split() # ['4', '2', '10']
input_value = map(int, input_value)
# map(fun, list) => list의 가각의 원소에 func을 통과시켜 결과를 반환한다
# [x, y, z ] => [f(x), f(y), f(z) ]

n, w, L = input_value

n, w, L = map(int, input().split())
lst = list(map(int, input().split()))

# n, w, l, lst를 쓰는 로직
# 로직을 만들어서 실행한 후 백준에서 데이터를 복사해서 결과값에 넣기

# 입력시간을 줄일때 사용 함.
# 로직의 맨 위에 작성
import sys
input = sys.stdin.readline
# 백준 풀 때 사용

#출력
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep="/")