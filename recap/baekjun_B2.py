def solution(quiz_result):
    total_score = 0  # 전체 총점
    current_score = 0 # 현재 연속 정답 점수 (O가 나올 때마다 커짐)
    
    # 여기서부터 코드를 작성하세요 (for문 사용)
    # 힌트: 'O'면 current_score를 1 늘리고 total_score에 더한다.
    #       'X'면 current_score를 0으로 만든다.
    
    
    return total_score

# 테스트
print(solution("OOXXOXXOOO"))       # 예상: 10
print(solution("OXOXOXOXOXOXOX"))   # 예상: 7
print(solution("OOOOO"))            # 예상: 15 (1+2+3+4+5)
print(solution("XXXXX"))            # 예상: 0