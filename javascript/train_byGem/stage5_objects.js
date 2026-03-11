// 파일명: stage5_objects.js

// 문제 1. 파이썬의 딕셔너리 생성 및 값 접근을 자바스크립트의 객체와 '점(.) 표기법'으로 번역해 주세요.
// user = {"name": "Max", "age": 25}
// print(user["name"])

// 여기에 코드를 작성해 주세요.
// const user = {"name": "Max", "age": 25}
// console.log(user.name)

// 문제 2. 파이썬의 dict.get()을 자바스크립트의 논리 연산자(||)를 활용한 기본값 처리로 번역해 주세요.
// (힌트: 자바스크립트에서는 객체에 없는 키에 접근하면 undefined가 나옵니다. 이를 || 연산자와 조합해 보세요!)
// user = {"name": "Max"}
// age = user.get("age", 20)
// print(age)

// 여기에 코드를 작성해 주세요.
// const user = {"name": "Max"}
// const age = user.age || 20
// console.log(age)


// 문제 3. 파이썬의 dict.keys()를 자바스크립트의 Object.keys()로 번역해 주세요.
// user = {"name": "Max", "age": 25}
// keys = list(user.keys())
// print(keys)

// 여기에 코드를 작성해 주세요.
// const user = {"name": "Max", "age": 25}
// const keys = Object.keys(user)


// 문제 4. 파이썬의 dict.items() 순회를 자바스크립트의 Object.entries()와 for...of 문으로 번역해 주세요.
// user = {"name": "Max", "age": 25}
// for key, value in user.items():
//     print(f"{key}: {value}")

// 여기에 코드를 작성해 주세요.
// const user = {"name": "Max", "age": 25}
// for (const [key, value] of Object.entries(user)) {
//     `${key}:${value}`
// }


// 문제 5. 파이썬의 변수 할당을 자바스크립트의 모던한 '구조 분해 할당(Destructuring Assignment)'으로 번역해 주세요.
// (힌트: 객체의 키 이름과 똑같은 이름의 변수를 한 번에 선언하고 값을 빼올 수 있습니다. const { ... } = 객체)
// user = {"name": "Max", "age": 25}
// name = user["name"]
// age = user["age"]
// print(name, age)

// 여기에 코드를 작성해 주세요.
const user = {"name": "Max", "age": 25}
const {name, age} = user;
console.log(name, age);