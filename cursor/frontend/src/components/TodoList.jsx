import { TodoItem } from './TodoItem'

export function TodoList({ todos, onToggle, onUpdate, onDelete, loadingId }) {
  if (!todos.length) {
    return <p style={{ color: '#888' }}>할 일이 없습니다. 위에서 추가해 보세요.</p>
  }
  return (
    <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onToggle={onToggle}
          onUpdate={onUpdate}
          onDelete={onDelete}
          loading={loadingId === todo.id}
        />
      ))}
    </ul>
  )
}
