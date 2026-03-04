/**
 * [Daily Catch-up Drill] 1단계: 변수와 제어문
 * 실행 방법: 터미널에서 `node training.js` 입력
 */

// ---------------------------------------------------------
// (Part 1) 문법 번역 (Syntax Translation)
// ---------------------------------------------------------

// [문제 1] 조건문과 문자열 포매팅 (Max 정답 반영 완료!)
/* 🐍 Python Code:
user_score = 85
if user_score >= 90:
    grade = 'A'
elif user_score >= 80:
    grade = 'B'
else:
    grade = 'C'
print(f"Your grade is {grade}")
*/
const userScore = 85;
let grade;

if (userScore >= 90) {
    grade = 'A';
} else if (userScore >= 80) {
    grade = 'B';
} else {
    grade = 'C';
}
console.log(`[문제 1 결과] Your grade is ${grade}`);
console.log("----------------------------------------");


// [문제 2] 기본 반복문
/* 🐍 Python Code:
total = 0
for i in range(1, 6):
    total += i
print(total)
*/

// ☕ JavaScript Translation:
let total = 0;
// TODO: 파이썬의 for문을 JS의 for (초기화; 조건식; 증감식) 구조로 번역해보세요.
for (let i = 1; i <=5; i++){
    total += i
}

console.log(`[문제 2 결과] Total: ${total}`); // 예상 결과: 15
console.log("----------------------------------------");


// ---------------------------------------------------------
// (Part 2) 개념 응용 (Logic & Concept)
// ---------------------------------------------------------

// [문제 3] 동등 비교 (== vs ===)
/* 🐍 Python Code:
a = "5"
b = 5
print(a == b) # 파이썬은 타입이 다르면 False를 반환하죠.
*/

// ☕ JavaScript Translation:
const a = "5";
const b = 5;
// JS의 == 와 === 는 결과가 다릅니다. 실행해보고 이유를 생각해보세요!
console.log("[문제 3-1] a == b 결과:", a == b);   // 예측: ?
console.log("[문제 3-2] a === b 결과:", a === b); // 예측: ?
console.log("----------------------------------------");


// [문제 4] 암시적 형변환
/* 🐍 Python Code:
result = "Max" + 22
print(result) # TypeError: can only concatenate str (not "int") to str
*/

// ☕ JavaScript Translation:
// 파이썬은 에러를 내지만, JS는 문법 에러 없이 작동합니다. 결과가 어떻게 나올까요?
const result = "Max" + 22;
console.log("[문제 4 결과]", result); // 예측: ?
console.log("----------------------------------------");


// ---------------------------------------------------------
// (Part 3) 알고리즘 JS로 풀기 (Algo in JS)
// ---------------------------------------------------------

// [문제 5] Even/Odd 판별
/* 🐍 Python Code:
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
*/

// ☕ JavaScript Translation:
console.log("[문제 5 시작]");
// TODO: 위 파이썬 코드를 완벽한 JS 코드로 번역해보세요. (let, for, if, === 사용)

for (let num = 1; num <= 10; num++) { // 조건을 <= 로 수정!
    if (num % 2 === 0) {
        console.log(`${num} is Even`); // 띄어쓰기 추가
    } else {
        console.log(`${num} is Odd`);
    }
}