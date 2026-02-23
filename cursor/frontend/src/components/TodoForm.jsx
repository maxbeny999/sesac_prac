import { useState } from 'react'

export function TodoForm({ onSubmit, loading }) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!title.trim()) return
    onSubmit({ title: title.trim(), description: description.trim() || null })
    setTitle('')
    setDescription('')
  }

  return (
    <form onSubmit={handleSubmit} style={styles.form}>
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="제목"
        disabled={loading}
        style={styles.input}
      />
      <input
        type="text"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="설명 (선택)"
        disabled={loading}
        style={styles.input}
      />
      <button type="submit" disabled={loading} style={styles.button}>
        추가
      </button>
    </form>
  )
}

const styles = {
  form: { display: 'flex', gap: 8, flexWrap: 'wrap', marginBottom: 24 },
  input: {
    padding: '10px 12px',
    border: '1px solid #444',
    borderRadius: 8,
    background: '#16213e',
    color: '#eee',
    minWidth: 160,
  },
  button: {
    padding: '10px 20px',
    background: '#0f3460',
    color: '#eee',
    border: 'none',
    borderRadius: 8,
    cursor: 'pointer',
  },
}
