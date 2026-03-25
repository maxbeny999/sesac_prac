-- Active: 1774442026165@@127.0.0.1@5432@postgres
INSERT INTO employees (emp_id, name, email)
VALUES (1, '김철수', 'chulsoo@company.com');
INSERT INTO books(
    book_id,
    title ,
    author ,
    published_date
)
VALUES (101, '파이썬 정복', '박개발', '2024-01-01');

UPDATE employees SET email = 'ironman@company.com' WHERE emp_id = 1;

SELECT * FROM employees;

INSERT INTO employees (emp_id,name,email)
VALUES(999,'스파이','spy@company.com')

DELETE FROM employees WHERE emp_id = 999;

SELECT * FROM employees 

INSERT INTO loans (
    loan_id,
    emp_id,
    book_id,
    loan_date
)
VALUES(1,1,101,'2026-03-25');

UPDATE loans SET return_date = '2026-04-01' WHERE loan_id = 1;
