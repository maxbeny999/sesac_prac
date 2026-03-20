// 부모가 보낸 내용물을 감싸주는 예쁜 껍데기입니다.
const Container = ({ children }) => {
  return (
    <div style={{ border: '3px solid #333', borderRadius: '15px', padding: '20px', maxWidth: '400px', margin: '0 auto' }}>
      {children}
    </div>
  );
};

export default Container;