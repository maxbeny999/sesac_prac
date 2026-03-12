import './App.css'

// 1. 나만의 레고 블록(컴포넌트) 만들기!
// 미션 1: 컴포넌트 이름은 무조건 '대문자'로 시작해야 합니다! 'loginBox'를 알맞게 고쳐주세요.
const /* 빈칸 (이름 고치기) */ = () => {
    return (
        <div className="input-group">
            <h1>로그인하세요</h1>
            <input type="text" placeholder="아이디를 입력하세요" />
        </div>
    );
};


// 2. 메인 화면(App)에서 레고 블록 조립하기!
function App() {
    return (
        <>
            <h2>Max님의 멋진 웹사이트</h2>
            
            {/* 미션 2: 위에서 만든 나만의 컴포넌트를 HTML 태그처럼 불러와 보세요! (스스로 닫기 잊지 마세요!) */}
            < /* 빈칸 */ /> 
            
            {/* 💡 똑같은 걸 또 쓰고 싶으면 그냥 태그를 한 번 더 쓰면 됩니다! */}
            < /* 빈칸 */ /> 
        </>
    );
}

export default App