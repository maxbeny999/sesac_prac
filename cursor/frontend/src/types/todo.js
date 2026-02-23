/**
 * @typedef {Object} Todo
 * @property {number} id
 * @property {string} title
 * @property {string|null} description
 * @property {boolean} completed
 * @property {string} created_at
 * @property {string} updated_at
 */

/**
 * @typedef {Pick<Todo, 'title'|'description'>} TodoCreate
 */

/**
 * @typedef {Partial<Pick<Todo, 'title'|'description'|'completed'>>} TodoUpdate
 */

export {}
