// 파일명: stage4_array_methods.js

// 문제 1. 파이썬의 리스트 컴프리헨션을 자바스크립트의 map() 메서드로 번역해 주세요.
// nums = [1, 2, 3, 4]
// doubled = [n * 2 for n in nums]
// print(doubled)

// 여기에 코드를 작성해 주세요.
// const nums = [1,2,3,4];
// const doubled = nums.map(n => n*2)
// console.log(doubled)


// 문제 2. 조건이 포함된 파이썬의 리스트 컴프리헨션을 자바스크립트의 filter() 메서드로 번역해 주세요.
// nums = [1, 2, 3, 4, 5, 6]
// evens = [n for n in nums if n % 2 == 0]
// print(evens)

// 여기에 코드를 작성해 주세요.
// const nums = [1,2,3,4,5,6]
// const evens = nums.filter(n => n % 2 === 0)


// 문제 3. 파이썬의 단순 순회 출력을 자바스크립트의 forEach() 메서드로 번역해 주세요.
// (힌트: map과 달리 forEach는 새로운 배열을 반환하지 않고 단순히 반복 작업만 수행합니다.)
// fruits = ["apple", "banana", "cherry"]
// for fruit in fruits:
//     print(fruit)

// 여기에 코드를 작성해 주세요.
// const fruits = ["appple", "banana", "cherry"]
// fruits.forEach(fruit => console.log(fruit))


// 문제 4. 파이썬의 딕셔너리 리스트에서 특정 값만 추출하는 코드를 map()으로 번역해 주세요.
// users = [{"name": "Max", "age": 25}, {"name": "Alice", "age": 30}]
// names = [user["name"] for user in users]
// print(names)

// 여기에 코드를 작성해 주세요.
const users = [{"name": "Max", "age": 25}, {"name": "Alice", "age": 30}]
const names = users.map(user => user.name)
console.log(names);

// 문제 5. 파이썬의 조건과 가공이 모두 들어간 리스트 컴프리헨션을 filter()와 map()을 체이닝(연결)하여 번역해 주세요.
// nums = [3, 5, 7, 9]
// result = [n * 10 for n in nums if n > 5]
// print(result)

// 여기에 코드를 작성해 주세요.
const nums = [3, 5, 7, 9];

// 1. filter로 5보다 큰 수를 먼저 거르고,
// 2. 바로 뒤에 map을 이어서 붙여 10을 곱해줍니다!
const result = nums.filter(n => n > 5).map(n => n * 10);

console.log(result);