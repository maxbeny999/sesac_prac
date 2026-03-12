// [미션] 서버에서 유저 목록을 가져와서, 성인(20세 이상)의 이름만 뽑아내기!

const getAdultUserNames = async () => {
    try {
        // 1. [Stage 6] 가짜 API에서 데이터를 가져와 박스를 뜯습니다.
        // (힌트: await fetch 와 await response.json() 사용)
        const response = await fetch("https://api.example.com/data");
        const users = await response.json();

        // 아래는 서버에서 users 변수에 들어올 가상의 데이터입니다.
        /*
          [
            { id: 1, name: "Max", age: 25 },
            { id: 2, name: "Alice", age: 17 },
            { id: 3, name: "Bob", age: 30 }
          ]
        */

        // 2. [Stage 4 & 5 종합] 
        // users 배열에서 filter()를 써서 age가 20 이상인 사람만 남기고,
        // 바로 이어서 map()을 써서 name만 있는 배열로 만들어보세요!
        // (힌트: user => user.age 처럼 점 표기법을 쓰면 됩니다!)
        const adultNames = users.filter(user => user.age >= 20).map(user => user.name);
        
        console.log("성인 유저 목록:", adultNames); // 예상 출력: ["Max", "Bob"]
        return adultNames;

    } catch (e) {
        console.log("데이터를 가져오는 중 에러가 발생했습니다.", e);
    }
};

// 함수 실행 테스트
getAdultUserNames();

// [미션] 게시글 목록에서 중복 없는 '태그(tag)' 목록만 배열로 뽑아내기!

const posts = [
    { id: 1, title: "JS 기초", tag: "Frontend" },
    { id: 2, title: "React 시작", tag: "Frontend" },
    { id: 3, title: "파이썬 서버", tag: "Backend" },
    { id: 4, title: "DB 설계", tag: "Backend" }
];

// 1. posts.map(...)을 써서 tag만 있는 배열을 만듭니다.
// 2. 그걸 new Set(...)으로 감싸서 중복을 날려버립니다.
// 3. 마지막으로 전체를 [... ] 로 감싸서 다시 순수한 배열로 만듭니다.
const allTags = posts.map(t => t.tag)
const uniqueTags = new Set(allTags)
const finalTagsArray = [...uniqueTags]


console.log(uniqueTags); 
// 예상 출력: [ 'Frontend', 'Backend' ]