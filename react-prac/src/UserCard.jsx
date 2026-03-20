// src/UserCard.jsx

const UserCard = ({ name, age, job }) => {
  return (
    <div style={{ border: '1px solid black', margin: '10px', padding: '10px' }}>
      {/* 자바스크립트 변수이므로 중괄호 {} 로 감싸서 출력합니다! */}
      <h3>
        {name} / {age}세 / {job}
      </h3>
    </div>
  );
};

export default UserCard;
