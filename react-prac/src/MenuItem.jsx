// 미션 1: Props 구조 분해 할당으로 name, price, isSoldOut, onAdd 를 받아오세요!
const MenuItem = ({name, price, isSoldOut, onAdd}) => {
  return (
    <div style={{ borderBottom: '1px solid #ddd', padding: '15px 0', display: 'flex', justifyContent: 'space-between' }}>
      <span><strong>{name}</strong> - {price}원</span>

      {/* 미션 2: isSoldOut이 true면 "품절! 😭" 글자를, false면 "주문하기" 버튼이 보이게 삼항연산자(? :)를 써보세요! */}
      { isSoldOut ? (
        <span style={{ color: 'red', fontWeight: 'bold' }}>품절! 😭</span>
      ) : (
        // 미션 3: 버튼을 클릭하면 부모가 물려준 onAdd 함수가 실행되게 하세요!
        <button onClick={ onAdd } style={{ cursor: 'pointer' }}>주문하기</button>
      )}
    </div>
  );
};

export default MenuItem;