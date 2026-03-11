// 파일명: stage2_control_flow.js

// 문제 1. 파이썬의 if / elif / else 문을 자바스크립트로 번역해 주세요.
// score = 85
// if score >= 90:
//     print("A")
// elif score >= 80:
//     print("B")
// else:
//     print("C")

// 여기에 코드를 작성해 주세요.
const score = 85
if (score >= 90) {
    console.log("A")
} else if (score >= 80){
    console.log("B")
} else{
    console.log("C")
}


// 문제 2. 파이썬의 for i in range(5)를 자바스크립트의 기본 for문으로 번역해 주세요.
// for i in range(5):
//     print(i)

// 여기에 코드를 작성해 주세요.
for (let i = 0; i <= 5; i++) {
    console.log(i)
}


// 문제 3. 파이썬의 리스트 순회(for item in list)를 자바스크립트의 for...of 문으로 번역해 주세요.
// fruits = ["apple", "banana", "cherry"]
// for fruit in fruits:
//     print(fruit)

// 여기에 코드를 작성해 주세요.
const fruits = ["apple", "banana", "cherry"]
for (const fruit of fruits){
    console.log(fruit)
}


// 문제 4. 파이썬의 while 문을 자바스크립트로 번역해 주세요.
// count = 0
// while count < 3:
//     print(f"카운트: {count}")
//     count += 1

// 여기에 코드를 작성해 주세요.
let count = 0
while (count < 3){
    console.log(`카운트: ${count}`)
    count += 1
}


// 문제 5. 파이썬의 조건문과 break, continue를 활용한 코드를 번역해 주세요.
// for i in range(10):
//     if i == 5:
//         break
//     if i % 2 != 0:
//         continue
//     print(i)

// 여기에 코드를 작성해 주세요.
for (let i = 0; i < 10; i++){
    if (i === 5){
        break
    } if (i % 2 !== 0){
        continue
    } console.log(i)
}