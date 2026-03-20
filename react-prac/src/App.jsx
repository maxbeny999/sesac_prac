import { useState, useEffect } from 'react'; // 심장(State)과 마이크(Effect) 둘 다 가져옵니다!
import './App.css';

function App() {
  // 처음 화면이 켜졌을 때는 데이터가 없으니까 "로딩중..." 이라고 띄워둡니다.
  const [menuMessage, setMenuMessage] = useState(
    '데이터를 불러오는 중입니다... 🌀',
  );

  // 화면이 처음 켜지자마자 실행될 행동을 적어줍니다.
  useEffect(
    () => {
      // setTimeout: 특정 시간 뒤에 코드를 실행해주는 JS 기본 타이머입니다.
      setTimeout(() => {
        // 미션 1: 2초가 지났습니다! 지휘봉(setMenuMessage)을 휘둘러서 글자를 "아메리카노, 라떼, 소금빵 준비 완료! ☕" 로 바꿔보세요!
        setMenuMessage('아메리카노, 라떼, 소금빵 준비 완료! ☕');
      }, 2000); // 2000ms = 2초
    },
    [
      /* 미션 2: 화면이 '처음 켜질 때 딱 한 번만' 실행되게 하려면 이 대괄호 안에 뭘 넣어야 할까요? (힌트: 아무것도 안 넣는 게 정답의 핵심!) */
    ],
  );

  return (
    <div style={{ padding: '50px', textAlign: 'center' }}>
      <h2>서버 통신 흉내내기 (useEffect)</h2>

      {/* State 값을 화면에 보여줍니다 */}
      <h3 style={{ color: 'teal' }}>{menuMessage}</h3>
    </div>
  );
}

export default App;
