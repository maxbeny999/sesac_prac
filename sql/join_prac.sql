-- Active: 1769143473833@@127.0.0.1@5432@world@public
-- 어느 나라에 속한 도시인지
SELECT city.name city_name , country.name country_name
FROM city
JOIN country ON city.countrycode = country.code;

-- 국가와 그 국가의 공식 수도 매칭
SELECT country.name country_name, city.name city_name
FROM city
JOIN country ON country.capital = city.id 