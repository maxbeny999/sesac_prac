/**
 * [Daily Catch-up Drill 02] 변수, 조건문, 반복문 심화
 * Max, 파이썬 코드를 보고 JS로 완벽하게 번역해보세요.
 */

// ---------------------------------------------------------
// (Part 1) 문법 번역 (Syntax Translation)
// ---------------------------------------------------------

// [문제 1] 논리 연산자 번역
/* 🐍 Python Code:
is_weekend = True
is_holiday = False
# 파이썬은 and, or, not을 쓰지만 JS는 &&, ||, ! 를 씁니다.
if is_weekend or is_holiday:
    print("Can rest!")
if not is_holiday and is_weekend:
    print("Perfect weekend!")
*/

const isWeekend = true;
const isHoliday = false;

// TODO: 위 파이썬 로직을 JS로 번역하세요. (&&, ||, ! 사용)
if (isWeekend || isHoliday){
    console.log("Can rest!");
}
if (!isHoliday && isWeekend){
    console.log("Perfect weekend!");
}

// [문제 2] While 루프 번역
/* 🐍 Python Code:
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
*/

// TODO: 위 파이썬 로직을 JS로 번역하세요. (let 사용 필수)
let count = 5;
while (count > 0){
    console.log(`Countdown: ${count}`);
    count --;
}


console.log("----------------------------------------");

// ---------------------------------------------------------
// (Part 2) 개념 응용 (Logic & Concept)
// ---------------------------------------------------------

// [문제 3] Falsy 값 찾기
// JS에는 false가 아니어도 조건문에서 false처럼 취급되는 값(Falsy)들이 있습니다.
// 다음 중 console.log가 실행 "안 되는" 케이스를 골라 주석을 해제하고 확인해보세요.

if (0) { console.log("이게 보일까요?"); }
if ("") { console.log("빈 문자열은요?"); }
if (undefined) { console.log("undefined는?"); }
if (null) { console.log("null은?"); }
if (NaN) { console.log("NaN(Not a Number)은?"); }




// [문제 4] 증감 연산자의 위치
// i++와 ++i의 차이를 파악하는 문제입니다. 출력 결과를 예측해보세요.
let x = 10;
let y = x++; // x를 먼저 y에 넣고 나서 x를 1 올림
console.log(`[문제 4] x: ${x}, y: ${y}`); // 결과는?


console.log("----------------------------------------");

// ---------------------------------------------------------
// (Part 3) 알고리즘 JS로 풀기 (Algo in JS)
// ---------------------------------------------------------

// [문제 5] 배수의 합 구하기 (백준 브론즈 스타일)
/* 🐍 Python Logic:
# 1부터 20까지의 숫자 중 3의 배수이거나 5의 배수인 숫자의 합을 구하시오.
total_sum = 0
for i in range(1, 21):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i
print(total_sum)
*/

// TODO: 위 로직을 JS로 구현해보세요.
let totalSum = 0;
for (let i =1; i <21; i++){
    if (i % 3 === 0 || i % 5 === 0) {
        totalSum +=i
    }
}

console.log(`[문제 5 결과] Total Sum: ${totalSum}`);

/*
# 🐍 Python
def get_result(score):
    if score >= 60:
        msg = "Pass"
    else:
        msg = "Fail"
    return "Result: " + msg
*/
const getResult = (score) => {
    let msg;
    if ( score>= 60){
        msg = "Pass";
    } else {
        msg = "Fail";
    }
    return `Result : ${msg}`
};

/*
# 🐍 Python
def total_message(prefix="Total is: ", *numbers):
    total = sum(numbers)
    return f"{prefix}{total}"

print(total_message("합계: ", 1, 2, 3)) # "합계: 6"
print(total_message(undefined, 10, 20)) # "Total is: 30"
*/

const totalMessage = (prefix = "Total is", ...numbers) => {
    let total = 0;
    for (let num of numbers) {
        total += num;
    }
    return `${prefix}${total}`;
}