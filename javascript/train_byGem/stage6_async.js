// 파일명: stage6_async.js

// 문제 1. 파이썬의 try...except 문을 자바스크립트의 try...catch 문으로 번역해 주세요.
// try:
//     # 파이썬은 0으로 나누면 에러가 나지만, 
//     # JS 흉내를 내기 위해 존재하지 않는 함수를 호출해 보겠습니다.
//     do_something_wrong()
// except Exception as e:
//     print("에러 발생:", e)

// 여기에 코드를 작성해 주세요.
try { 
    do_something_wrong(); 
} catch (e) {
    // 에러가 발생하면 이쪽으로 넘어옵니다! e 변수 안에 에러 정보가 담겨 있어요.
    // 여기에 console.log를 이용해 "에러 발생:" 과 e를 함께 출력해 보세요.
    console.log("에러발생", e);
}


// 문제 2. 파이썬의 비동기 함수를 자바스크립트의 'async 화살표 함수'로 번역해 주세요.
// async def greet_async():
//     return "비동기 인사!"

// 여기에 코드를 작성해 주세요.
const greet_async = async() => ("비동기 인사!")


// 문제 3. 파이썬의 데이터 패칭을 자바스크립트의 fetch()와 async/await로 번역해 주세요.
// (힌트: fetch()로 응답(response)을 받고, await response.json() 으로 데이터를 추출합니다.)
// async def get_data():
//     response = requests.get("https://api.example.com/data")
//     data = response.json()
//     print(data)

// 여기에 코드를 작성해 주세요.
const get_data = async () => {
    // 1. fetch()를 사용하고, 응답이 올 때까지 await로 기다립니다.
    const response = await fetch("https://api.example.com/data"); 
    
    // 2. json() 함수를 실행하고, 파싱이 끝날 때까지 await로 또 기다립니다.
    const data = await response.json(); 
    
    console.log(data);
};

// 문제 4. [최종 보스] async/await와 try/catch를 결합하여 안전한 비동기 데이터 패칭 함수를 완성해 주세요.
// (힌트: 1번과 3번을 합치면 됩니다!)
// async def fetch_user():
//     try:
//         response = requests.get("https://api.example.com/user")
//         data = response.json()
//         return data["name"]
//     except Exception as e:
//         print("데이터를 가져오지 못했습니다:", e)
//         return "Unknown"

// 여기에 코드를 작성해 주세요.

const fetchUser = async() => {
    try {
        const response = await fetch("https://api.example.com/user")

        const data = await response.json()

        return data.name
    } catch (e) {
        console.log("데이터를 가져오지 못했습니다", e)
        return "Unknown"
    }
}