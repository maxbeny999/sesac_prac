# DailyAlgo 문제 1번 https://dailyalgo.kr/ko/problems/157
def solution(n):
    answer = 0
    while n != 1:
        answer += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1  
    return answer

# DailyAlgo 문제 2번 https://dailyalgo.kr/ko/problems/158
def solution(n):
    nums = str(n) 
    r_nums = nums[:: -1]
    if nums == r_nums:
        answer = True
    else:
        answer = False
    return answer

print(solution(565))


# DailyAlgo 문제 3번 https://dailyalgo.kr/ko/problems/168
def solution(n):
    answer = 0
    for number in range(1, n+1):
        nums = str(number)
        for target_number in nums:
            if target_number == "3" or target_number == "6" or target_number == "9":
                answer += 1 
                break
    return answer

print(solution(36))


# # DailyAlgo 문제 4번 https://dailyalgo.kr/ko/problems/169

def solution(n):
    answer = 0
    for number in range(1, n+1):
        nums = str(number)
        for target_number in nums:
            if target_number == "3" or target_number == "6" or target_number == "9": 
            # if target_number in {'3', '6', '9'}: 바로 위의 코드와 같은데 더 짧은식
                answer += 1 
    return answer

print(solution(36))

# DailyAlgo 문제 5번 https://dailyalgo.kr/ko/problems/171

def solution(numbers):
    # 1. 점수판 만들기 (숫자별 등장 횟수 세기)
    count_dict = {}
    
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1  # 이미 있으면 +1
        else:
            count_dict[num] = 1   # 처음 보면 1로 등록
            
    # count_dict 결과 예시: {1: 2, 3: 5, 4: 2} (3이 5번 나옴)

    # 2. 가장 많이 나온 횟수(최고 기록) 찾기
    # 딕셔너리의 값(Value)들 중에서 가장 큰 수를 찾습니다.
    max_frequency = max(count_dict.values())
    
    # 3. 최고 기록을 가진 숫자들(후보)만 모으기
    candidates = []
    for num, count in count_dict.items():
        if count == max_frequency:
            candidates.append(num)
            
    # 4. 후보들 중 가장 작은 수 찾기
    # 문제 조건: "최빈값이 여러 개면 가장 작은 수를 반환"
    candidates.sort() # 오름차순 정렬 (작은 게 맨 앞으로)
    
    return candidates[0] # 맨 앞의 숫자 반환


#collections Counter 사용
from collections import Counter

def solution(numbers):
    # 1. 개수 세기 (끝!)
    counter = Counter(numbers) 
    
    # 2. 최빈값 가져오기 (가장 많은 순으로 정렬해서 줌)
    # .most_common()은 [(값, 횟수), (값, 횟수)...] 형태로 줍니다.
    most_common = counter.most_common()
    
    # 최빈값이 여러 개일 때 처리 (방금 푼 문제 로직)
    # 만약 첫 번째(1등) 횟수와 두 번째(2등) 횟수가 같다면?
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        # 최빈값 후보들을 다 모아서 가장 작은 수 리턴 (여기는 로직 필요)
        candidates = [num for num, count in most_common if count == most_common[0][1]]
        return sorted(candidates)[0]
    else:
        return most_common[0][0]
# for num_counter in number:

# DailyAlgo 문제 6번

def solution(numbers, window):
    answer = []
    
    # 1. [초기 세팅] 첫 번째 창문의 합은 직접 구해야 합니다.
    current_sum = sum(numbers[:window])
    answer.append(current_sum)
    
    # 2. [슬라이딩] 창문을 한 칸씩 옆으로 밉니다.
    # 전체 길이에서 창문 크기만큼 뺀 횟수만큼만 이동하면 됩니다.
    for i in range(len(numbers) - window):
        
        # 3. [핵심 로직] (기존 합) - (나가는 놈) + (들어오는 놈)
        # numbers[i] : 창문 맨 왼쪽에서 빠지는 숫자 (나가는 놈)
        # numbers[i + window] : 창문 맨 오른쪽으로 새로 들어오는 숫자 (들어오는 놈)
        current_sum = current_sum - numbers[i] + numbers[i + window]
        
        answer.append(current_sum)
        
    return answer

solution([9,5,1,5,0,10],3)

print(f"{solution([9,5,1,5,0,10],3) }")