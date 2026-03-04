/**
 * [Daily Catch-up Drill 03] 함수(Function) 실전 번역
 * 목표: 파이썬의 def를 JS의 화살표 함수로 완벽하게 맵핑하기
 * 실행 방법: 터미널에서 `node practice_03.js` 입력
 */

// ---------------------------------------------------------
// (Part 1) 기본 화살표 함수와 암시적 반환(Implicit Return)
// ---------------------------------------------------------

// [문제 1] 온도 변환기 (한 줄로 줄여보세요!)
/* 🐍 Python Code:
def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
*/

// TODO: 위 파이썬 코드를 JS 화살표 함수로 번역하세요. (return 생략 도전!)
const convertToFahrenheit = celsius => (celsius * 9/5) + 32 ;

console.log(`[문제 1] 30도 -> 화씨: ${convertToFahrenheit(30)}`); // 예상: 86
console.log("----------------------------------------");


// [문제 2] 짝수 판별기
/* 🐍 Python Code:
def is_even(num):
    return num % 2 == 0
*/

// TODO: num을 받아 짝수면 true, 아니면 false를 반환하는 화살표 함수를 만드세요.
const isEven = num => (num % 2 === 0)

console.log(`[문제 2] 10은 짝수인가? ${isEven(10)}`); // 예상: true
console.log(`[문제 2] 7은 짝수인가? ${isEven(7)}`);  // 예상: false
console.log("----------------------------------------");


// ---------------------------------------------------------
// (Part 2) 매개변수 기본값과 템플릿 리터럴
// ---------------------------------------------------------

// [문제 3] 자기소개 문자열 만들기
/* 🐍 Python Code:
def introduce(name, age=20):
    return f"Hello, I am {name} and I am {age} years old."
*/

// TODO: 파이썬의 기본값(age=20)과 f-string을 JS 스타일로 번역하세요.
const introduce = (name, age=20) => `Hello, I am ${name} and I am ${age} years old`

console.log("[문제 3]", introduce("Max", 25)); // 예상: Hello, I am Max and I am 25 years old.
console.log("[문제 3]", introduce("Guest"));   // 예상: Hello, I am Guest and I am 20 years old.
console.log("----------------------------------------");


// ---------------------------------------------------------
// (Part 3) 로직이 포함된 함수 (멀티 라인)
// ---------------------------------------------------------

// [문제 4] 학점 계산기 (중괄호 {} 와 return 필수!)
/* 🐍 Python Code:
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"
*/

// TODO: 위 로직을 JS 화살표 함수로 번역하세요. (else if 사용)
const getGrade = score => {
    if (score >= 90) {
        return "A"
    } else if (score >= 80) {
        return "B"
    } else {
        return "C"
    }
}

console.log(`[문제 4] 85점의 학점: ${getGrade(85)}`); // 예상: B
console.log("----------------------------------------");


// ---------------------------------------------------------
// (Part 4) 🚀 보너스: 함수를 부품처럼 쓰기 (콜백 맛보기)
// ---------------------------------------------------------

// JS에서는 만든 함수를 다른 함수의 재료로 쏙 넣을 수 있습니다.
const scores = [45, 80, 60, 100, 30];

// TODO: score를 받아서 60점 이상이면 true를 반환하는 checkPass 함수를 만드세요.
const checkPass = score => (score >= 60)

// Array.filter()는 배열 안의 요소를 하나씩 checkPass 기계에 넣고, 
// true가 나온 애들만 모아서 새 배열을 만듭니다.
const passedScores = scores.filter(checkPass); 
console.log(`[보너스] 합격자 점수 목록: ${passedScores}`); // 예상: 80,60,100