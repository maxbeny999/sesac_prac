-- Active: 1769143442347@@127.0.0.1@5432@dvdrental@public

CREATE VIEW actor_with_film AS
SELECT actor.first_name, actor.last_name, film.title
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film.film_id = film_actor.film_id

SELECT * 
FROM actor_with_film
WHERE title ILIKE '%c%'


SELECT * FROM customer

CREATE VIEW simple_customer AS
SELECT first_name, last_name FROM customer

SELECT * FROM simple_customer


SELECT 
    *
FROM film_actor a
JOIN film_actor b ON a.film_id = b.film_id
WHERE a.actor_id < b.actor_id; 


SELECT * 
FROM actor a
JOIN actor b ON a.actor_id = b.actor_id


with something AS (
    (
    SELECT film_id
    FROM film_category
    WHERE category_id = (
        SELECT category_id
        FROM category
        WHERE name = 'Action'
    )
);
)
SELECT title
FROM film
WHERE film_id IN something

SELECT film.title
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'Action'

WITH RECURSIVE cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT * FROM cte_name;