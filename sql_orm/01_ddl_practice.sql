-- Active: 1774442026165@@127.0.0.1@5432@postgres
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
)

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    published_date DATE
) ;

CREATE TABLE loans (
    loan_id INT PRIMARY KEY,
    emp_id INT REFERENCES employees(emp_id),
    book_id INT REFERENCES books(book_id),
    loan_date DATE NOT NULL
);

CREATE TABLE reviews (
    review_id INT PRIMARY KEY,
    book_id INT REFERENCES books(book_id),
    emp_id INT REFERENCES employees(emp_id),
    rating INT NOT NULL,
    content VARCHAR(500)
);

ALTER TABLE loans ADD return_date DATE;