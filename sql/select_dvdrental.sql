-- Active: 1769143442347@@127.0.0.1@5432@dvdrental@public

-- - **`title`**: 영화 제목
-- - **`rental_rate`**: 영화 대여료 (금액)
-- - **`rating`**: 영화 관람 등급 (G, PG, R 등)
-- - **`length`**: 영화 상영 시간 (분 단위)
-- - **`rental_duration`**: 대여 가능 기간 (일 단위)
-- - **`replacement_cost`**: 영화 분실 시 변상 비용

-- 1. 모든 영화의 제목과 대여료를 조회하시오.
-- 1. 모든 영화의 
-- 제목과 대여료를 조회하시오.
SELECT title, rental_rate
FROM film;


-- 2. 대여료가 4달러 이상인 영화의 제목과 대여료를 조회하시오.
-- 2. 대여료가 4달러 이상인 
-- 영화의 
-- 제목과 대여료를 조회하시오.
SELECT title, rental_rate
FROM film
WHERE rental_rate >= 4;


-- 3. 등급별 영화 수를 조회하시오.
-- 3. 등급별 
-- 영화 수를 조회하시오.
SELECT rating, COUNT(*)
FROM film
GROUP BY rating;


-- 4. 상영 시간을 중복 제거하여 내림차순으로 정렬하고, 상위 10개를 조회하시오.
-- 4. 상영 시간을 중복 제거하여 
-- 내림차순으로 정렬하고, 
-- 상위 10개를 조회하시오.
SELECT DISTINCT length
FROM film
ORDER BY length DESC
LIMIT 10;

-- 5. 대여 기간별 영화 수를 대여 기간 내림차순으로 정렬하여 조회하시오.
-- 5. 대여 기간별 영화 수를 
-- 대여 기간 내림차순으로 정렬하여 조회하시오.
SELECT rental_duration, COUNT(*)
FROM film
GROUP BY rental_duration
ORDER BY rental_duration DESC;


-- 6. 대여 기간이 5일 이상이고 대여료가 4달러 이상인 영화의 제목, 대여 기간, 대여료를 조회하시오.
-- 6. 대여 기간이 5일 이상이고 
-- 대여료가 4달러 이상인 
-- 영화의 제목, 대여 기간, 대여료를 조회하시오.
SELECT title, rental_duration, rental_rate
FROM film
WHERE rental_duration >= 5
    AND rental_rate >= 4;

-- 7. 등급이 'R'인 영화 중 처음 10개의 제목과 등급을 조회하시오.
-- 7. 등급이 'R'인 영화 중 
-- 처음 10개의 
-- 제목과 등급을 조회하시오.
SELECT title, rating
FROM film
WHERE rating = 'R'
ORDER BY title
LIMIT 10;

-- 8. 대여료별 영화 수를 영화 수 내림차순으로 정렬하여 조회하시오.
-- 8. 대여료별 영화 수를 
-- 영화 수 내림차순으로 정렬하여 조회하시오.
SELECT rental_rate, COUNT(*)
FROM film
GROUP BY rental_rate
ORDER BY COUNT(*) DESC;

-- 9. 교체 비용별 영화 수와 평균 대여료를 교체 비용 오름차순으로 정렬하여 조회하시오.
-- 9. 교체 비용별 영화 수와 평균 대여료를 
-- 교체 비용 오름차순으로 정렬하여 조회하시오.
SELECT replacement_cost, COUNT(*) AS 영화수, AVG(rental_rate) AS "평균대여료"
FROM film
GROUP BY replacement_cost
ORDER BY replacement_cost;


-- 10. 제목에 'angel'이 포함된 영화의 제목을 조회하시오.
-- 10. 제목에 'angel'이 포함된 영화의 제목을 조회하시오.
SELECT title 
FROM film
WHERE title ILIKE '%angel%';


-- 11. 등급별 평균 대여료가 3달러 미만인 등급과 평균 대여료를 조회하시오.
-- 11. 등급별 평균 대여료가 3달러 미만인 
-- 등급과 평균 대여료를 조회하시오.
SELECT rating, AVG(rental_rate) AS avg_rental_rate
FROM film
GROUP BY rating
HAVING AVG(rental_rate) < 3;

-- 12. 상영 시간이 10번째에서 15번째로 긴 영화의 제목과 상영 시간을 조회하시오. (상영 시간이 같을 경우 제목 오름차순으로 정렬)
-- 12. 상영 시간이 10번째에서 15번째로 긴 영화의
--  제목과 상영 시간을 조회하시오. 
--  (상영 시간이 같을 경우 제목 오름차순으로 정렬)
SELECT title, length
FROM film
ORDER BY length DESC, title
LIMIT 6 OFFSET 9;

-- 13. 등급이 'PG' 또는 'G'이면서 대여 기간이 4일 이하인 영화의 제목, 등급, 대여 기간을 조회하시오.
-- 13. 등급이 'PG' 또는 'G'이면서 
-- 대여 기간이 4일 이하인 
-- 영화의 제목, 등급, 대여 기간을 조회하시오.
SELECT title, rating, rental_duration
FROM film
WHERE rating IN ('PG', 'G')
    AND rental_duration <= 4
ORDER BY rating, rental_duration;

-- 14. 등급별 영화 수와 평균 상영 시간을 조회하시오.
SELECT rating, COUNT(*), AVG(length)
FROM film
GROUP BY rating

-- 15. 상영 시간이 60분 이상 120분 이하인 영화의 
-- 제목과 상영 시간을 
-- 상영 시간 오름차순으로 조회하시오.
SELECT title, length
FROM film
WHERE length BETWEEN 60 AND 120
ORDER BY length;



SELECT a.first_name, 
       a.last_name,
       f.title
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
ORDER BY a.first_name, a.last_name;

SELECT a.first_name, 
       a.last_name
FROM actor a
ORDER BY a.first_name, a.last_name