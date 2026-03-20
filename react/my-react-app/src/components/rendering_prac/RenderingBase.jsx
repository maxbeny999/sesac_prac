import React from "react";
import LoginStatus from "./LoginStatus";
import AdminLink from "./AdminLink";
import TodoItem from "./TodoItem";
import Numbers from "./Numbers";
import Students from "./Students";

const RenderingBase = () => {
  return (
    <>
      <div>RenderingBase</div>
      <div>{"값"}</div>
      <div>{123}</div>
      <div>{"true"}</div>
      <div>{false}</div>
      <div>{null}</div>
      <div>{undefined}</div>
      <LoginStatus isLogin={true} />
      <LoginStatus isLogin={false} />
      <AdminLink isAdmin={true} />
      <AdminLink isAdmin={false} />
      <TodoItem text="내용" isDone={true} />
      <TodoItem text="내용" isDone={false} />
      <br />
      <Numbers />
      <br />
      <Students />
    </>
  );
};

export default RenderingBase;
