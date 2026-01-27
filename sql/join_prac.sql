-- Active: 1769143473833@@127.0.0.1@5432@dvdrental
-- 어느 나라에 속한 도시인지
SELECT city.name city_name , country.name country_name
FROM city
JOIN country ON city.countrycode = country.code;

-- 국가와 그 국가의 공식 수도 매칭
SELECT country.name country_name, city.name city_name
FROM city
JOIN country ON country.capital = city.id 

--  배우가 출연한 영화의 제목을 조회
SELECT f.title, a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
ORDER BY a.first_name;

--  first_name이 `PENELOPE` 인 배우가 출연한 영화의 제목을 조회
SELECT f.title
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE a.first_name = 'Penelope';

--  영화 별 출연 배우의 수를 조회
SELECT f.title, Count(a.actor_id)
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE a.first_name = 'Penelope';


--  영화 별 출연 배우의 수가 5가 넘는 데이터를 배우의 수가 큰순으로 조회
SELECT 
    f.title, 
    COUNT(fa.actor_id) AS actor_count
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
GROUP BY f.film_id, f.title     -- 영화별로 그룹을 묶고
HAVING COUNT(fa.actor_id) > 5   -- 그 그룹의 배우 수가 5명 초과인 것만 남겨서
ORDER BY actor_count DESC;      -- 많은 순서대로 정렬
-- -  고객의 대여 정보 조회
SELECT 
    c.first_name, 
    c.last_name, 
    r.rental_date, 
    r.return_date
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id;
-- -  고객이 대여한 영화 정보 조회
SELECT 
    c.first_name, 
    c.last_name, 
    f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id        -- 1. 고객 & 대여 연결
JOIN inventory i ON r.inventory_id = i.inventory_id   -- 2. 대여 & 재고 연결
JOIN film f ON i.film_id = f.film_id;                 -- 3. 재고 & 영화 연결 
-- -  `YENTL IDAHO` 영화를 대여한 고객 정보 조회
SELECT 
    c.first_name, 
    c.last_name,
    f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE f.title = 'YENTL IDAHO';  -- 제목이 이것인 것만 필터링
-- -  배우별로 출연한 영화의 등급(rating)을 조회
SELECT 
    a.first_name, 
    a.last_name, 
    f.title, 
    f.rating
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id  -- 배우 -> 출연목록
JOIN film f ON fa.film_id = f.film_id           -- 출연목록 -> 영화
ORDER BY a.actor_id;
-- -  1번 고객이 자주 대여한 영화의 카테고리를 찾으시오
SELECT 
    cat.name, 
    COUNT(cat.name) AS category_count
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film_category fc ON i.film_id = fc.film_id      -- 영화 -> 영화카테고리 연결
JOIN category cat ON fc.category_id = cat.category_id -- 영화카테고리 -> 카테고리 이름 연결
WHERE c.customer_id = 1                              -- 1번 고객만 조회
GROUP BY cat.name                                    -- 카테고리 별로 묶고
ORDER BY category_count DESC                         -- 제일 많이 빌린 순서로 정렬
LIMIT 1;                                             -- 1등만
-- -  각 직원이 일하는 매장의 주소와 도시를 조회
SELECT 
    s.first_name AS staff_name, 
    ci.city, 
    a.address
FROM staff s
JOIN store st ON s.store_id = st.store_id      -- 직원 -> 매장
JOIN address a ON st.address_id = a.address_id -- 매장 -> 주소
JOIN city ci ON a.city_id = ci.city_id;        -- 주소 -> 도시
-- -  고객별로 대여한 영화 제목과 지불한 금액, 날짜를 조회
SELECT 
    c.first_name, 
    f.title, 
    p.amount, 
    r.rental_date
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN payment p ON r.rental_id = p.rental_id  -- 대여 기록(rental)에 결제 내역(payment)을 연결
ORDER BY c.customer_id, r.rental_date;
-- -  국가별 고객 수를 조회

-- -  `Action` 카테고리에 출연한 배우 조회

-- -  재고(inventory)가 없는 영화 찾기

-- -  카테고리별 평균 대여료