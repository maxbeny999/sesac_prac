// 멘토의 메시지: Max, 아래 Python 코드들을 가장 세련된 JS(ES6+) 코드로 번역해 보세요.
console.log("=== 🚀 [Level 1] Python to JS: Object Advanced ===\n");

// -----------------------------------------------------------------------------
// [문제 1] 객체 메서드와 this (Python의 class와 self 대체하기)
// -----------------------------------------------------------------------------
/* 🐍 Python:
class Car:
    def __init__(self):
        self.owner = "Max"
        self.distance = 0
    
    def drive(self):
        self.distance += 10
        print(f"{self.owner}님이 10km 주행했습니다.")

my_car = Car()
my_car.drive()
*/

// 🎯 Mission 1: 위 파이썬 클래스를 JS의 단일 객체 리터럴(Object Literal)로 만드세요.
// `drive` 메서드를 작성할 때 `function` 키워드를 생략하는 '메서드 축약형'을 사용해 보세요.
const myCar = {
  owner: "Max",
  distance: 0,
  drive () {
    this.distance +=10
    console.log(`${this.owner}님이 10km 주행했습니다.`)
  },
};


// -----------------------------------------------------------------------------
// [문제 2] 값만 추출하기 (Python의 dict.values())
// -----------------------------------------------------------------------------
/* 🐍 Python:
scores = {"math": 80, "english": 90, "science": 100}
total_score = sum(scores.values())
*/

const scores = { math: 80, english: 90, science: 100 };

// 🎯 Mission 2: Object.values()를 사용해 점수만 뽑아낸 배열을 만들고, 
// 그 합계를 totalScore 변수에 할당하세요. 
// TODO: JS 코드로 번역하세요.
const totalScore = Object.values(scores).reduce((total, score) => total + score, 0)

// Python의 `for in` 대신 JS는 `for...of`를 사용합니다.
// 값이 계속 더해지며 변해야 하므로 const가 아닌 let을 사용합니다!
let totalScoreForOf = 0; 

for (const score of Object.values(scores)) {
  totalScoreForOf += score;
}

// -----------------------------------------------------------------------------
// [문제 3] 딕셔너리 순회 (Python의 dict.items())
// -----------------------------------------------------------------------------
/* 🐍 Python:
grades = {"math": "A", "english": "B"}
for key, value in grades.items():
    print(f"{key} 성적은 {value}입니다")
*/

const grades = { math: "A", english: "B" };

// 🎯 Mission 3: Object.entries()와 for...of 문, 그리고 구조 분해 할당을 결합하여
// 위 파이썬의 print문과 똑같이 동작하도록 JS로 번역하세요. (백틱 ` 활용)
// TODO: JS 코드로 번역하세요.



// -----------------------------------------------------------------------------
// [문제 4] 동적 키 할당 (Computed Property Names)
// -----------------------------------------------------------------------------
/* 🐍 Python:
input_key = "email"
input_value = "max@example.com"
form = {
    input_key: input_value
}
*/

const inputKey = "email";
const inputValue = "max@example.com";

// 🎯 Mission 4: 대괄호 `[]`를 사용하여 변수 inputKey의 값이 
// 객체의 키(Key)가 되도록 form 객체를 완성하세요.
// TODO: JS 코드로 번역하세요.
const form = {
  
};


// -----------------------------------------------------------------------------
// [문제 5] 중첩 딕셔너리 값 추출 (React 필수)
// -----------------------------------------------------------------------------
/* 🐍 Python:
user_profile = {
    "id": 1,
    "info": {
        "nickname": "JS-Master",
        "address": {
            "city": "Seoul",
            "zip": "12345"
        }
    }
}
city = user_profile["info"]["address"]["city"]
*/

const userProfile = {
  id: 1,
  info: { nickname: "JS-Master", address: { city: "Seoul", zip: "12345" } }
};

// 🎯 Mission 5: 점 표기법(userProfile.info...)을 쓰지 말고,
// '중첩 구조 분해 할당'을 사용해 단 한 줄로 city 변수를 뽑아내세요.
// (Hint: const { 깊은구조... } = userProfile;)
// TODO: JS 코드로 번역하세요.