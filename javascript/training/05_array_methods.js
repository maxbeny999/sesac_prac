/**
 * [Daily Catch-up Drill 04] 배열(Array) 메서드 정복
 * 목표: 파이썬의 List 조작을 JS의 map, filter, forEach로 대체하기
 * 실행 방법: 터미널에서 `node practice_04.js` 입력
 */

// ---------------------------------------------------------
// (Part 1) 배열의 기본 (Python List vs JS Array)
// ---------------------------------------------------------
console.log("=== Part 1: 기본 조작 ===");
const fruits = ["Apple", "Banana"];

// Python: fruits.append("Cherry")
fruits.push("Cherry"); 

// Python: len(fruits)
console.log(`과일 개수: ${fruits.length}`); // 3

// Python: fruits.pop()
const lastFruit = fruits.pop(); 
console.log(`꺼낸 과일: ${lastFruit}, 남은 배열: ${fruits}`);
console.log("\n");


// ---------------------------------------------------------
// (Part 2) 실무 3대장 실습 (TODO 미션)
// ---------------------------------------------------------
console.log("=== Part 2: map, filter, forEach 미션 ===");

const prices = [1000, 2500, 500, 3000];
console.log(`원본 가격표: ${prices}`);

// [미션 1] map: 모든 가격을 10% 인상한 새로운 배열을 만드세요.
// 힌트: 요소를 하나씩 받아서 * 1.1을 곱해 반환하는 화살표 함수를 map에 넣습니다.
// Python: raised_prices = [p * 1.1 for p in prices]
const raisedPrices = prices.map(p => p * 1.1);

console.log(`[미션 1] 인상된 가격: ${raisedPrices}`); 
// 예상 결과: [ 1100, 2750, 550, 3300 ]


// [미션 2] filter: 인상된 가격(raisedPrices) 중 2000 이상인 것만 걸러내세요.
// 힌트: 요소를 하나씩 받아서 >= 2000 인지 확인하는 화살표 함수를 filter에 넣습니다.
// Python: expensive_items = [p for p in raised_prices if p >= 2000]
const expensiveItems = raisedPrices.filter(p => p >= 2000);

console.log(`[미션 2] 2000 이상인 비싼 상품: ${expensiveItems}`); 
// 예상 결과: [ 2750, 3300 ]


// [미션 3] forEach: 비싼 상품들(expensiveItems)을 하나씩 예쁘게 출력하세요.
// 힌트: 요소를 하나씩 받아서 console.log(`비싼 상품 가격: ${...}`)를 실행하는 화살표 함수를 forEach에 넣습니다.
// Python: for item in expensive_items: print(f"비싼 상품 가격: {item}")
console.log("[미션 3] 개별 출력 시작:");
expensiveItems.forEach( p => console.log(`비싼 상품 가격 ${p}`));

// 예상 출력:
// 비싼 상품 가격: 2750
// 비싼 상품 가격: 3300

console.log("\n===================================");