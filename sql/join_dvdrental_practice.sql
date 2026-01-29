-- Active: 1769143442347@@127.0.0.1@5432@dvdrental@public
SELECT f.film_id, f.title, i.inventory_id
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL;
# 영화 데이터는 있지만 store에 재고가 없는 경우를 조회


# 배우별 출연 영화 수
SELECT actor.first_name, actor.last_name, count(film.film_id)
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor on actor.actor_id = film_actor.actor_id
GROUP BY actor.actor_id


SELECT COUNT(actor.first_name), film.title
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor on actor.actor_id = film_actor.actor_id
GROUP BY film.title, actor.actor_id
ORDER BY film.title

SELECT actor.first_name, film.title
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor on actor.actor_id = film_actor.actor_id
-- GROUP BY film.film_id
ORDER BY film.title


SELECT 
    f.title,
    c.name as category
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
LEFT JOIN category c ON fc.category_id = c.category_id
ORDER BY f.title;



SELECT a.first_name, a.last_name, count(f.title)
FROM actor a
LEFT JOIN film_actor fa ON fa.actor_id = a.actor_id
LEFT JOIN film f ON fa.film_id = f.film_id
WHERE a.first_name = 'Christian'
GROUP BY a.actor_id ;

SELECT a.first_name, a.last_name, count(f.title)
FROM actor a
JOIN film_actor fa ON fa.actor_id = a.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE a.first_name = 'Christian'

GROUP BY a.first_name, a.last_name
