-- Active: 1774442026165@@127.0.0.1@5432@dvdrental
SELECT 
    c.customer_id, 
    c.first_name, 
    c.last_name, 
    COUNT(r.rental_id) AS rental_count
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
GROUP BY 
    c.customer_id, 
    c.first_name, 
    c.last_name
ORDER BY 
    rental_count DESC
LIMIT 5;