/**
 * [JS Foundation Final Test]
 * 목표: 지금까지 배운 모든 JS 기초 문법 종합 활용
 * 실행 방법: node final_test.js
 */

console.log("=== 1라운드: 변수와 타입 ===");

// [문제 1] 다음 코드에서 에러가 나는 줄을 찾고, 올바르게 수정하세요.
const playerName = "Max";
let level = 1;
// playerName = "Alex";  // TODO: 왜 에러가 날까요? 에러가 안 나게 하려면 어떻게 해야 할까요?
level++;
console.log(`Player: ${playerName}, Level: ${level}`);


console.log("\n=== 2라운드: 동등 비교와 형변환 ===");

// [문제 2] 다음 3개의 console.log 결과를 예측해서 주석으로 적어보세요.
const a = "10";
const b = 10;
console.log(a == b);   // 예측: true
console.log(a === b);  // 예측: false
console.log(a + b);    // 예측: 1010


console.log("\n=== 3라운드: Falsy와 논리 연산자 ===");

// [문제 3] 다음 조건문 중 '실행되는 것'만 골라보세요. (주석으로 O, X 표시)
if ("") { console.log("A"); }        // 예측: X
if (" ") { console.log("B"); }       // 예측: O
if (!null) { console.log("C"); }     // 예측: X
if (undefined) { console.log("D"); } // 예측: X


console.log("\n=== 4라운드: 기본 제어문 (for & if) ===");

// [문제 4] 1부터 10까지의 숫자 중 '홀수(Odd)'만 더한 값을 구하세요. (for문과 if문 사용)
let oddSum = 0;
// TODO: 여기에 for문과 if문을 작성하세요.
for (let i = 1; i < 11; i++)
    if (i % 2 !== 0){
        oddSum+=i
    }

console.log(`[문제 4] 홀수의 합: ${oddSum}`); // 예상: 25

console.log("\n=== 5라운드: 화살표 함수 (한 줄 짜기) ===");

// [문제 5] 숫자를 하나 받아 제곱을 반환하는 화살표 함수 getSquare를 '한 줄'로 작성하세요.
const getSquare = n => (n**2)

console.log(`[문제 5] 5의 제곱: ${getSquare(5)}`); // 예상: 25


console.log("\n=== 6라운드: 매개변수 기본값과 템플릿 리터럴 ===");

// [문제 6] 이름(name)과 소속(team)을 받아 환영 인사를 반환하는 함수를 만드세요.
// 단, 소속이 입력되지 않으면 기본값으로 "Guest"를 사용해야 합니다.
const welcome = (name, team = "Guest") => {
    return `Hello ${name}! Welcome to ${team} team.`};

console.log(welcome("Max", "Engineering")); // 예상: Hello Max! Welcome to Engineering team.
console.log(welcome("Alice"));              // 예상: Hello Alice! Welcome to Guest team.


console.log("\n=== 7라운드: 멀티라인 화살표 함수 (return) ===");

// [문제 7] 나이(age)를 받아 18세 이상이면 "성인", 아니면 "미성년자"를 반환하는 함수를 만드세요.
// 조건: 중괄호 {} 와 return 키워드, 그리고 if/else 문을 반드시 사용할 것!
const checkAdult = (age) => {
    if (age >= 18){
        return "성인"
    } else {
        return "미성년자"
    }
};
console.log(`[문제 7] 20세: ${checkAdult(20)}`); // 예상: 성인


console.log("\n=== 8라운드: 배열 기본 조작 ===");

// [문제 8] 빈 배열 `cart`를 만들고, "Apple"과 "Banana"를 차례대로 추가한 뒤, 
// 마지막 요소를 빼서(pop) `lastItem` 변수에 담으세요.
const cart = [];
cart.push("Apple")// TODO: cart에 Apple 추가 
cart.push("Banana")// TODO: cart에 Banana 추가
const lastItem = cart.pop()// const lastItem = TODO: 마지막 요소 빼기

console.log(`[문제 8] 빼낸 과일: ${lastItem}, 남은 카트: ${cart}`); 


console.log("\n=== 9라운드: Array 메서드 (map, filter) ===");

const scores = [45, 90, 32, 88, 100];

// [문제 9-1] filter: 점수 중 80점 이상인 '합격자 점수'만 걸러내어 새 배열을 만드세요.
const passed = scores.filter(score => score >= 80) // TODO

// [문제 9-2] map: 걸러낸 합격자 점수에 각각 보너스 점수 5점씩을 더해 새 배열을 만드세요.
const finalScores = passed.map(passedScore => passedScore + 5 )  // TODO

console.log(`[문제 9] 최종 합격자 점수: ${finalScores}`); // 예상: 95, 93, 105


console.log("\n=== 10라운드: 🔥 최종 보스 (메서드 체이닝 + forEach) ===");

const words = ["apple", "js", "python", "hi", "react"];

// [문제 10] 위 단어 배열에서:
// 1. 글자 수가 3글자 이상인 단어만 걸러내고 (filter, 힌트: word.length >= 3)
// 2. 그 단어들을 대문자로 변환하고 (map, 힌트: word.toUpperCase())
// 3. 변환된 단어들을 하나씩 출력하세요. (forEach, 힌트: console.log 사용)
const longWord = words.filter(word => word.length >= 3 );
const capWord = longWord.map(word => word.toUpperCase());
capWord.forEach(word => {
    console.log(word)    
});


console.log("[문제 10 출력 결과]");
// TODO: words 배열에 메서드 체이닝( .filter().map().forEach() )을 한 번에 연결해서 작성해보세요!
// 예상 출력: 
// APPLE
// PYTHON
// REACT