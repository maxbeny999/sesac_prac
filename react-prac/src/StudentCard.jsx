// 미션 1: grade와 classNum에 기본값 1을 설정해 보세요! (파이썬 기본값 문법과 똑같습니다)
const StudentCard = ({ name, grade = 1, classNum = 1 }) => {
  return (
    <div style={{ border: '1px solid blue', margin: '10px', padding: '10px' }}>
      <h3>
        이름: {name} / 학년: {grade} / 반: {classNum}
      </h3>
    </div>
  );
};

export default StudentCard;
