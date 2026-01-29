-- 1. 배우가 출연한 영화의 제목을 조회
SELECT film.title, actor.first_name, actor.last_name
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
    
-- 2. first_name이 `PENELOPE` 인 배우가 출연한 영화의 제목을 조회
SELECT actor.first_name, actor.last_name, film.title
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE actor.first_name ILIKE 'PENELOPE';
    
-- 3. 영화 별 출연 배우의 수를 조회
SELECT film.title, COUNT(actor.actor_id) -- select에는 film의 모든 컬럼들을 사용 가능한데,
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
GROUP BY film.film_id
ORDER BY film.film_id;

SELECT film.title, COUNT(film_actor.actor_id) 
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor ON actor.actor_id = film_actor.actor_id
-- 우리는 actor들의 개수를 세는 것이지, actor 그 자체에 대한 정보가 필요하지 않습니다.
-- film과 연결된 actor의 정보는 film_actor에 들어있습니다.
GROUP BY film.film_id
ORDER BY film.film_id;

-- 4. 영화 별 출연 배우의 수가 
-- 5가 넘는 데이터를 -> having 추가
-- 배우의 수가 큰순으로 조회 -> order by 추가
SELECT film.title, COUNT(film_actor.actor_id) 
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
GROUP BY film.film_id
HAVING COUNT(film_actor.actor_id) >= 5
ORDER BY COUNT(film_actor.actor_id) DESC

-- 5. 고객의 대여 정보 조회
SELECT 
    customer.first_name, 
    customer.last_name,
    rental.rental_date
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
ORDER BY customer.customer_id

-- 6. 고객이 대여한 영화 정보 조회
SELECT 
    cu.first_name,
    cu.last_name,
    f.title
FROM customer cu
JOIN rental r ON cu.customer_id = r.customer_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
ORDER BY f.film_id


-- 7. `YENTL IDAHO` 영화를 대여한 고객 정보 조회
-- customer - rental - inventory - film
SELECT f.title, c.first_name, c.last_name
FROM customer c
JOIN rental r ON  c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE f.title ILIKE 'YENTL IDAHO'


-- 8. 배우별로 출연한 영화의 등급(rating)을 조회
-- -> 문제 수정 : 1. 배우들이 출연한 영화의 등급들의 종류를 확인하자.
-- ->            2. 배우들이 출연한 등급별 영화의 개수를 조회해라
SELECT actor.first_name, actor.last_name, film.rating, count(*)
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
GROUP BY actor.actor_id, film.rating
ORDER BY actor.actor_id

-- 9. 1번 고객이 자주 대여한 카테고리를 찾으시오

SELECT c.customer_id,  COUNT(cat.category_id) category_count
FROM customer c -- customer_id만 쓰기 때문에 rental에서 처리 가능
JOIN rental r ON  c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id -- inventory의 film_id로 처리 가능
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat ON fc.category_id = cat.category_id
WHERE c.customer_id = 1
GROUP BY c.customer_id, cat.category_id
ORDER BY category_count DESC
LIMIT 1;

-- (1번 고객이 자주 대여한 영화의) 카테고리를 찾으시오
-- 일단 1번 고객이 자주 대여한 영화를 가져옴.
WITH top_movie AS(
    SELECT f.title, f.film_id, count(*)
    FROM customer c
    JOIN rental r ON  c.customer_id = r.customer_id
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film f ON i.film_id = f.film_id
    WHERE c.customer_id = 1
    GROUP BY f.film_id
    ORDER BY count(*) DESC
    LIMIT 1
)
-- 해당 영화의 카테고리를 가져옴
SELECT top_movie.title, cat.name, count
FROM top_movie
JOIN film_category fc ON top_movie.film_id = fc.film_id
JOIN category cat ON cat.category_id = fc.category_id


-- 10. 각 직원이 일하는 매장의 주소와 도시를 조회
-- 직원 - 매장 - 주소 - 도시
SELECT staff.first_name, address.address, city.city
FROM staff
JOIN store ON staff.store_id = store.store_id
JOIN address ON store.address_id = address.address_id
JOIN city ON address.city_id = city.city_id

-- 11. 고객별로 대여한 영화 제목과 지불한 금액, 날짜를 조회
SELECT cu.first_name, f.title, p.amount, r.rental_date
FROM customer cu
JOIN rental r ON cu.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON f.film_id = i.film_id
JOIN payment p ON r.rental_id = p.rental_id


-- 12. 국가별 고객 수를 조회
SELECT co.country, COUNT(*) 
FROM country co
JOIN city ci ON ci.country_id = co.country_id
JOIN address ad ON ci.city_id = ad.city_id
JOIN customer cu ON cu.address_id = ad.address_id
GROUP BY co.country_id

-- 13. `Action` 카테고리에 출연한 배우 조회

SELECT DISTINCT actor.first_name, actor.last_name, category.name
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
-- JOIN film ON film.film_id = film_actor.film_id
-- JOIN film_category ON film.film_id = film_category.film_id
JOIN film_category ON film_actor.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
ORDER BY actor.first_name, actor.last_name, category.name

-- 14. 재고(inventory)가 없는 영화 찾기
-- left join을 활용한 방식.
SELECT f.film_id, f.title, i.inventory_id
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL
-- ORDER BY f.film_id

-- 15. 카테고리별 평균 대여료
SELECT cat.name, AVG(f.rental_rate)
FROM category cat
JOIN film_category fc ON cat.category_id = fc.category_id
JOIN film f ON f.film_id = fc.film_id
GROUP BY cat.name
ORDER BY AVG(f.rental_rate) DESC
