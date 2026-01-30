# practice_day1_algo.py
# [Day 1] Part 3: 오늘의 알고리즘 (Algorithm Drill)
# 목표: 배운 문법을 조합해서 '논리적인 문제'를 해결합니다.

# ----------------------------------------------------------------------
# [문제 1] 자릿수 더하기 https://school.programmers.co.kr/learn/courses/30/lessons/12931
# ----------------------------------------------------------------------
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 함수를 만드세요.
# 예: N = 123  -> 1 + 2 + 3 = 6
# 예: N = 987  -> 9 + 8 + 7 = 24
#
# [힌트]
# 1. 숫자는 for문을 돌릴 수 없습니다. 문자열(str)로 바꾸면 가능합니다.
# 2. 문자열 하나하나를 꺼낸 뒤에는 다시 계산을 위해 정수(int)로 바꿔야 합니다.


def solution_1(n):
    answer = 0
    n = str(n)
    for number in n:
        number = int(number)
        answer += number
    
    return answer
print(solution_1(123))

# ----------------------------------------------------------------------
# [문제 2] 없는 숫자 더하기 https://school.programmers.co.kr/learn/courses/30/lessons/86051
# ----------------------------------------------------------------------
# 0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하세요.
#
# 예: numbers = [1,2,3,4,6,7,8,0]
#     -> 5, 9가 없음
#     -> 5 + 9 = 14
#
# [힌트]
# 방법 A: 0부터 9까지 for문을 돌면서 numbers 안에 있는지(if i not in numbers) 확인한다.
# 방법 B: 수학적 사고! 0부터 9까지 다 더하면 45입니다. 여기서 numbers의 합을 빼면...?

# def solution_2(numbers):
#     answer = 0
#     for i in range(0,10):
#         if i not in numbers:
#             answer += i
    
#     return answer

def solution_2(numbers):
    answer = 0
    for i in range(1,10):
        answer +=i
    answer = answer - sum(numbers)
    return answer


# ----------------------------------------------------------------------
# [테스트 실행]
# 아래 코드는 수정하지 말고 실행해서 결과를 확인하세요.
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("--- [문제 1] 자릿수 더하기 테스트 ---")
    res1_1 = solution_1(123)
    res1_2 = solution_1(987)
    
    print(f"입력: 123 | 정답: 6  | 내 결과: {res1_1} | {'PASS' if res1_1 == 6 else 'FAIL'}")
    print(f"입력: 987 | 정답: 24 | 내 결과: {res1_2} | {'PASS' if res1_2 == 24 else 'FAIL'}")

    print("\n--- [문제 2] 없는 숫자 더하기 테스트 ---")
    res2_1 = solution_2([1,2,3,4,6,7,8,0])
    res2_2 = solution_2([5,8,4,0,6,7,9])
    
    print(f"입력: [1,2,3,4,6,7,8,0] | 정답: 14 | 내 결과: {res2_1} | {'PASS' if res2_1 == 14 else 'FAIL'}")
    print(f"입력: [5,8,4,0,6,7,9]   | 정답: 6  | 내 결과: {res2_2} | {'PASS' if res2_2 == 6 else 'FAIL'}")