
// 문제 1. f-string을 모던 자바스크립트의 '템플릿 리터럴'로 번역해 주세요.
// name = "Max"
// age = 25
// print(f"제 이름은 {name}이고, 나이는 {age}살입니다.")

// 여기에 코드를 작성해 주세요.
const name = "Max"
const age = 25
console.log(`제 이름은${name}이고, 나이는${age}살입니다.`)


// 문제 2. 파이썬의 동등 비교(==)를 자바스크립트에서 값과 타입을 모두 엄격하게 비교하는 연산자로 번역해 주세요.
// num1 = 10
// num2 = "10"
// is_same = (num1 == num2)
// print(is_same)

// 여기에 코드를 작성해 주세요.
const num1 = 10
const num2 = "10"
const isSame = (num1 === num2)
console.log(isSame)


// 문제 3. 문자열을 숫자로 변환하는 파이썬 코드를 번역해 주세요. (JS의 Number() 활용)
// str_num = "100"
// actual_num = int(str_num)
// print(actual_num + 50)

// 여기에 코드를 작성해 주세요.
const strNum = "100"
const actualNum = Number(strNum)
console.log(actualNum + 50)


// 문제 4. 숫자를 문자열로 변환하는 파이썬 코드를 번역해 주세요. (JS의 String() 활용)
// year = 2026
// str_year = str(year)
// print(str_year + "년")

// 여기에 코드를 작성해 주세요.
const year = 2026
const strYear = String(year)
console.log(strYear + "년")


// 문제 5. 변수(재할당 가능)와 상수(재할당 불가능)를 구분하여 번역해 주세요. 
// (파이썬은 엄격히 구분하지 않지만, 모던 JS에서는 let과 const를 명확히 구분해야 합니다. var는 사용하지 마세요!)
// city = "Seoul"
// city = "Busan"
// PI = 3.14
// print(city, PI)

// 여기에 코드를 작성해 주세요.
let city = "Seoul"
city = "Busan"
const PI = 3.14
console.log(city, PI)