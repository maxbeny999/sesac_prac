// 파일명: set_map_mission.js

// 문제 1. [Set] 다음 배열에서 중복을 싹 제거한 Set을 만들고, 숫자 4를 추가해 보세요.
const numbers = [1, 1, 2, 2, 3, 3];
const newSet = new Set(numbers)
newSet.add(4)
console.log(newSet)
// 1-1. numbers 배열을 넣어서 중복이 제거된 mySet을 만들어주세요!

// 1-2. mySet에 숫자 4를 추가(add)해 주세요!
/* 빈칸 */;

console.log(mySet); // 예상 출력: Set(4) { 1, 2, 3, 4 }


// 문제 2. [Map] 새로운 Map을 만들고, 정보를 저장한 뒤 꺼내보세요.
const myMap = new Map(); // 빈 Map 생성!

// 2-1. myMap에 키는 "name", 값은 "Max"로 셋팅(set)해 주세요.
myMap.set("name", "Max")

// 2-2. myMap에 키는 "age", 값은 25로 셋팅(set)해 주세요.
myMap.set("age",25)

// 2-3. myMap에서 "name" 키에 해당하는 값을 가져와서(get) 변수에 담아보세요.
const myName = myMap.get("name")

console.log(`내 이름은 ${myName}입니다.`); // 예상 출력: 내 이름은 Max입니다.