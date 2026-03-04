// 1. 변수 선언 const 와 let
const maxAge = 25; // 파이썬 : MAX_AGE = 25     
let currentStatus = 'learning JS' ; // 파이썬 current_status = 'learning JS'

// maxAge = 26; // <- 주석을 풀면 에러남. const는 재할당 불가
currentStatus = 'mastering JS'; // let은 재할당 가능

// 2. 문자열 템플릿 리터럴 (파이썬의 f-string)
const greeting = `Hello, my name is Max. i am ${currentStatus}.`;

// 3. 불리언 boolean (소문자 주의)
const isPythonExpert = true; // 파이썬: True
const isJsExpert = false; // 파이썬: False

// 4. null vs undefined 
let missingValue; // 할당을 안 함
const emptyValue = null; // 의도적으로 비움

console.log('missingValue', missingValue); // 출력: undefined
console.log(emptyValue, emptyValue); // 출력 : null
console.log(maxAge, currentStatus)
console.log(greeting)