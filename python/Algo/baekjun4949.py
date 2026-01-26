import sys

while True:
    # 1. 한 줄 입력받기 (오른쪽 공백/엔터 제거)
    line = sys.stdin.readline().rstrip()

    # 2. 종료 조건: 점 하나만 들어오면 끝
    if line == ".":
        break

    stack = []
    is_balanced = True

    for char in line:
        # [Case 1] 여는 괄호: 무조건 저장
        if char == "(" or char == "[":
            stack.append(char)
        
        # [Case 2] 닫는 소괄호 )
        elif char == ")":
            # 스택에 뭐가 있고(not empty) AND 맨 위가 내 짝꿍 '(' 라면?
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop() # 성공! 꺼내기
            else:
                is_balanced = False # 실패! (비었거나 짝이 안 맞음)
                break
        
        # [Case 3] 닫는 대괄호 ]
        elif char == "]":
            # 스택에 뭐가 있고(not empty) AND 맨 위가 내 짝꿍 '[' 라면?
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop() # 성공! 꺼내기
            else:
                is_balanced = False # 실패!
                break
        
        # [Case 4] 알파벳, 공백, 점 등: 그냥 무시 (아무 코드도 안 씀)

    # 3. 최종 판결
    # (1) 검사 도중 실패하지 않았고 (True)
    # (2) 검사가 끝났는데 스택이 비어있어야 함 (남은 괄호가 없어야 함)
    if is_balanced == True and len(stack) == 0:
        print("yes")
    else:
        print("no")