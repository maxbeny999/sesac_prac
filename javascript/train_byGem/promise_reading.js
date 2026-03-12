// 파일명: promise_reading.js
import axios from 'axios';

// async/await 없이 Promise 방식(.then)으로 짠 코드
const fetchUserOldSchool = () => {
    // 1. 요청을 보냅니다. (await가 없으니 일단 약속 증서만 받음)
    axios.get("https://api.example.com/user")
        // 2. 만약 통신이 성공해서 데이터가 무사히 도착하면(_____) 이쪽으로!
        .then(response => {
            console.log("성공! 이름:", response.data.name);
        })
        // 3. 만약 서버가 죽었거나 에러가 나면(_____) 이쪽으로!
        .catch(e => {
            console.log("에러 발생", e);
        });
};