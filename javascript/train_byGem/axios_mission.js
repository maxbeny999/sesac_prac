// 파일명: axios_mission.js

// 1. [모듈] 설치된 axios 외부 라이브러리를 가져옵니다. 
// (AI가 React 코드 짤 때 맨 위에 항상 적어두는 코드입니다!)
import axios from 'axios'; 

const fetchUser = async () => {
    try {
        // 미션 1: axios.get()을 써서 한 번에 요청하고 결과를 받으세요. (await는 한 번만 씁니다!)
        const response = await axios.get("https://api.example.com/user");
        
        // 미션 2: 알아서 JSON 변환이 끝난 진짜 알맹이는 무조건 'response.data' 안에 들어있습니다. 
        // 거기서 name만 쏙 뽑아서 바로 return 해보세요!
        return response.data.name;
        
    } catch (e) {
        console.log("에러 발생", e);
    }
};

// 함수 실행 테스트
// fetchUser().then(name => console.log(name));