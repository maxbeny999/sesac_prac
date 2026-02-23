import { useState } from 'react'

export function TodoItem({ todo, onToggle, onUpdate, onDelete, loading }) {
  const [editing, setEditing] = useState(false)
  const [title, setTitle] = useState(todo.title)
  const [description, setDescription] = useState(todo.description || '')

  const handleSave = () => {
    if (title.trim()) {
      onUpdate(todo.id, { title: title.trim(), description: description.trim() || null })
      setEditing(false)
    }
  }

  return (
    <li style={{ ...styles.item, opacity: loading ? 0.6 : 1 }}>
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={() => onToggle(todo.id)}
        disabled={loading}
        style={styles.checkbox}
      />
      <div style={styles.content}>
        {editing ? (
          <>
            <input
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              style={styles.editInput}
              autoFocus
            />
            <input
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="설명"
              style={styles.editInput}
            />
            <button type="button" onClick={handleSave} style={styles.smallBtn}>
              저장
            </button>
            <button type="button" onClick={() => setEditing(false)} style={styles.smallBtn}>
              취소
            </button>
          </>
        ) : (
          <>
            <span style={{ textDecoration: todo.completed ? 'line-through' : 'none', color: todo.completed ? '#888' : 'inherit' }}>
              {todo.title}
            </span>
            {todo.description && (
              <span style={styles.desc}>{todo.description}</span>
            )}
            <button type="button" onClick={() => setEditing(true)} style={styles.smallBtn}>
              수정
            </button>
            <button type="button" onClick={() => onDelete(todo.id)} style={{ ...styles.smallBtn, color: '#f66' }}>
              삭제
            </button>
          </>
        )}
      </div>
    </li>
  )
}

const styles = {
  item: {
    display: 'flex',
    alignItems: 'flex-start',
    gap: 12,
    padding: '12px 16px',
    background: '#16213e',
    borderRadius: 8,
    marginBottom: 8,
  },
  checkbox: { marginTop: 4, cursor: 'pointer' },
  content: { flex: 1, display: 'flex', flexDirection: 'column', gap: 4 },
  desc: { fontSize: 14, color: '#aaa' },
  editInput: {
    padding: 6,
    background: '#1a1a2e',
    border: '1px solid #444',
    borderRadius: 4,
    color: '#eee',
    marginBottom: 4,
  },
  smallBtn: {
    marginTop: 4,
    marginRight: 8,
    padding: '4px 10px',
    background: 'transparent',
    color: '#7eb',
    border: '1px solid #444',
    borderRadius: 4,
    cursor: 'pointer',
    fontSize: 12,
  },
}
