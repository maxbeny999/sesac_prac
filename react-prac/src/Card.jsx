// 미션 1: 부모가 태그 사이에 넣은 내용물은 무조건 'children'이라는 이름으로 들어옵니다. 빈칸을 채워주세요!
const Card = ({ children }) => {
  return (
    // 예쁜 그림자(box-shadow)가 있는 카드 액자 스타일입니다.
    <div
      style={{
        border: '1px solid #ddd',
        borderRadius: '8px',
        padding: '20px',
        boxShadow: '2px 2px 8px rgba(0,0,0,0.1)',
        marginBottom: '20px',
      }}
    >
      {/* 미션 2: 부모가 보낸 내용물(children)을 이 자리에 출력해주세요! */}
      {children}
    </div>
  );
};

export default Card;
