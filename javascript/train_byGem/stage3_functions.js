// 파일명: stage3_functions.js

// 문제 1. 파이썬의 기본 함수를 자바스크립트의 '화살표 함수(Arrow Function)'로 번역해 주세요.
// def greet(name):
//     return f"안녕하세요, {name}님!"
// print(greet("Max"))

// 여기에 코드를 작성해 주세요.
const greet = name => (`안녕하세요, ${name}님`)
console.log(greet("Max"))


// 문제 2. 파이썬의 매개변수가 여러 개인 함수를 화살표 함수로 번역해 주세요.
// def add_numbers(a, b):
//     return a + b
// print(add_numbers(10, 20))

// 여기에 코드를 작성해 주세요.
const addNumbers = (a,b) => (a+b)
console.log(addNumbers(10,20))


// 문제 3. 파이썬의 기본값 매개변수(Default Parameter)가 있는 함수를 화살표 함수로 번역해 주세요.
// def introduce(name, age=20):
//     return f"이름: {name}, 나이: {age}"
// print(introduce("Max"))

// 여기에 코드를 작성해 주세요.
const introduce = (name, age = 20) => (`이름:${name}, 나이: ${age}`)
console.log(introduce("Max"))

// 문제 4. 본문이 return문 하나뿐인 짧은 함수를 '중괄호{}와 return을 생략한' 형태의 화살표 함수로 번역해 주세요.
// def multiply_by_two(n):
//     return n * 2
// print(multiply_by_two(5))

// 여기에 코드를 작성해 주세요.
const multiplyBytwo = n => (n * 2)
console.log(multiplyBytwo(5))


// 문제 5. 파이썬의 가변 인자(*args)를 자바스크립트의 '나머지 매개변수(Rest Parameter)'로 번역해 주세요.
// (힌트: 자바스크립트에서는 별표(*) 대신 점 세 개(...)를 사용합니다.)
// def sum_all(*args):
//     total = 0
//     for num in args:
//         total += num
//     return total
// print(sum_all(1, 2, 3, 4, 5))

// 여기에 코드를 작성해 주세요.
const sumAll = (...args) => {
   let total = 0;
   for (const num of args){
    total += num
   }
   return total;
}
console.log(sumAll(1,2,3,4,5));