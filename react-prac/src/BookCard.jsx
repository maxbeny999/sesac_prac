// 부모가 'bookData'라는 통짜 객체(딕셔너리)를 보냈습니다!
const BookCard = ({ bookData }) => {
  return (
    <div style={{ border: '1px solid green', margin: '10px', padding: '10px' }}>
      {/* 미션 2: bookData 안에서 점(.)을 찍어서 title, author, price를 꺼내보세요! */}
      <h3>제목: {bookData.title}</h3>
      <p>저자: {bookData.author}</p>
      <p>가격: {bookData.price}원</p>
    </div>
  );
};

export default BookCard;
