const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000'

async function request(path, options = {}) {
  const url = `${API_BASE}${path}`
  const res = await fetch(url, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  })
  if (!res.ok) {
    const err = new Error(res.statusText)
    err.status = res.status
    err.body = await res.json().catch(() => ({}))
    throw err
  }
  if (res.status === 204) return
  return res.json()
}

export async function getTodos(completed = undefined) {
  const q = completed !== undefined ? `?completed=${completed}` : ''
  return request(`/todos${q}`)
}

export async function getTodo(id) {
  return request(`/todos/${id}`)
}

export async function createTodo(data) {
  return request('/todos', { method: 'POST', body: JSON.stringify(data) })
}

export async function updateTodo(id, data) {
  return request(`/todos/${id}`, { method: 'PATCH', body: JSON.stringify(data) })
}

export async function deleteTodo(id) {
  return request(`/todos/${id}`, { method: 'DELETE' })
}
