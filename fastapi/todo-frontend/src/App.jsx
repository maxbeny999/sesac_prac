import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [todos, setTodos] = useState([])
  const [task, setTask] = useState('')

  // 1. 목록 가져오기
  useEffect(() => {
    fetch("http://127.0.0.1:8000/todos")
      .then(res => res.json())
      .then(data => setTodos(data))
  }, [])

  // 2. 추가하기
  const addTodo = () => {
    if (!task) return;
    fetch("http://127.0.0.1:8000/todos", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task: task, is_done: false })
    })
    .then(res => res.json())
    .then(newTodo => {
      setTodos([...todos, newTodo]);
      setTask('');
    })
  }

  // 3. [추가] 체크박스 토글 (Update)
  const toggleTodo = (id, currentStatus) => {
    fetch(`http://127.0.0.1:8000/todos/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ is_done: !currentStatus }) // 반대값으로 보냄
    })
    .then(res => res.json())
    .then(updatedTodo => {
      // 화면에 있는 목록 중 해당 아이디만 찾아서 갈아끼우기
      setTodos(todos.map(t => t.id === id ? updatedTodo : t));
    })
  }

  // 4. [추가] 삭제하기 (Delete)
  const deleteTodo = (id) => {
    fetch(`http://127.0.0.1:8000/todos/${id}`, {
      method: "DELETE",
    })
    .then(res => {
      if (res.ok) {
        // 화면 목록에서 해당 아이디를 제외시킴
        setTodos(todos.filter(t => t.id !== id));
      }
    })
  }

  return (
    <div style={{ padding: "20px", fontFamily: "sans-serif" }}>
      <h1>📝 나의 투두 리스트</h1>
      
      <div style={{ marginBottom: "20px" }}>
        <input 
          type="text" 
          value={task}
          onChange={(e) => setTask(e.target.value)}
          placeholder="할 일을 입력하세요"
          style={{ padding: "10px", width: "200px", marginRight: "5px" }}
        />
        <button onClick={addTodo} style={{ padding: "10px" }}>추가</button>
      </div>

      <ul style={{ listStyle: "none", padding: 0 }}>
        {todos.map((todo) => (
          <li key={todo.id} style={{ 
            display: "flex", 
            alignItems: "center", 
            padding: "10px", 
            borderBottom: "1px solid #eee" 
          }}>
            {/* 체크박스: 클릭하면 toggleTodo 실행 */}
            <input 
              type="checkbox" 
              checked={todo.is_done} 
              onChange={() => toggleTodo(todo.id, todo.is_done)}
              style={{ marginRight: "10px", cursor: "pointer" }}
            />
            
            {/* 할 일 텍스트: 완료되면 줄 긋기 */}
            <span style={{ 
              textDecoration: todo.is_done ? "line-through" : "none",
              color: todo.is_done ? "gray" : "black",
              flexGrow: 1
            }}>
              {todo.task}
            </span>

            {/* 삭제 버튼 */}
            <button 
              onClick={() => deleteTodo(todo.id)}
              style={{ marginLeft: "10px", backgroundColor: "#ff4d4d", color: "white", border: "none", padding: "5px 10px", cursor: "pointer", borderRadius: "4px" }}
            >
              삭제
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App