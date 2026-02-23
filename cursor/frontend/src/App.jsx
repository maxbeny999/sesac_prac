import { useState, useEffect, useCallback } from 'react'
import { TodoForm } from './components/TodoForm'
import { TodoList } from './components/TodoList'
import * as api from './api/todos'

export default function App() {
  const [todos, setTodos] = useState([])
  const [filter, setFilter] = useState(undefined) // undefined = all, true/false = completed
  const [loading, setLoading] = useState(false)
  const [loadingId, setLoadingId] = useState(null)
  const [error, setError] = useState(null)

  const fetchTodos = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const data = await api.getTodos(filter)
      setTodos(data)
    } catch (e) {
      setError(e.message || '목록을 불러오지 못했습니다.')
    } finally {
      setLoading(false)
    }
  }, [filter])

  useEffect(() => {
    fetchTodos()
  }, [fetchTodos])

  const handleCreate = async (data) => {
    setLoading(true)
    setError(null)
    try {
      const created = await api.createTodo(data)
      setTodos((prev) => [created, ...prev])
    } catch (e) {
      setError(e.message || '추가에 실패했습니다.')
    } finally {
      setLoading(false)
    }
  }

  const handleToggle = async (id) => {
    const todo = todos.find((t) => t.id === id)
    if (!todo) return
    setLoadingId(id)
    setError(null)
    try {
      const updated = await api.updateTodo(id, { completed: !todo.completed })
      setTodos((prev) => prev.map((t) => (t.id === id ? updated : t)))
    } catch (e) {
      setError(e.message || '수정에 실패했습니다.')
    } finally {
      setLoadingId(null)
    }
  }

  const handleUpdate = async (id, data) => {
    setLoadingId(id)
    setError(null)
    try {
      const updated = await api.updateTodo(id, data)
      setTodos((prev) => prev.map((t) => (t.id === id ? updated : t)))
    } catch (e) {
      setError(e.message || '수정에 실패했습니다.')
    } finally {
      setLoadingId(null)
    }
  }

  const handleDelete = async (id) => {
    setLoadingId(id)
    setError(null)
    try {
      await api.deleteTodo(id)
      setTodos((prev) => prev.filter((t) => t.id !== id))
    } catch (e) {
      setError(e.message || '삭제에 실패했습니다.')
    } finally {
      setLoadingId(null)
    }
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Todo</h1>
      <TodoForm onSubmit={handleCreate} loading={loading} />
      <div style={styles.filters}>
        <button
          type="button"
          onClick={() => setFilter(undefined)}
          style={filter === undefined ? styles.filterActive : styles.filterBtn}
        >
          전체
        </button>
        <button
          type="button"
          onClick={() => setFilter(false)}
          style={filter === false ? styles.filterActive : styles.filterBtn}
        >
          미완료
        </button>
        <button
          type="button"
          onClick={() => setFilter(true)}
          style={filter === true ? styles.filterActive : styles.filterBtn}
        >
          완료
        </button>
      </div>
      {error && <p style={styles.error}>{error}</p>}
      {loading && !todos.length ? (
        <p style={{ color: '#888' }}>로딩 중...</p>
      ) : (
        <TodoList
          todos={todos}
          onToggle={handleToggle}
          onUpdate={handleUpdate}
          onDelete={handleDelete}
          loadingId={loadingId}
        />
      )}
    </div>
  )
}

const styles = {
  container: { maxWidth: 560, margin: '0 auto', padding: 24 },
  title: { marginBottom: 24, fontWeight: 700 },
  filters: { display: 'flex', gap: 8, marginBottom: 16 },
  filterBtn: {
    padding: '6px 12px',
    background: '#16213e',
    color: '#aaa',
    border: '1px solid #444',
    borderRadius: 6,
    cursor: 'pointer',
  },
  filterActive: {
    padding: '6px 12px',
    background: '#0f3460',
    color: '#eee',
    border: '1px solid #0f3460',
    borderRadius: 6,
    cursor: 'pointer',
  },
  error: { color: '#f66', marginBottom: 16 },
}
