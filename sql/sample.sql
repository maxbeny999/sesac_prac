-- Active: 1769143442347@@127.0.0.1@5432@world@public
SELECT *
FROM city 
ORDER BY countrycode

SELECT *
FROM country 
ORDER BY code

SELECT *
FROM country 
JOIN city ON city.countrycode = country.code
-- WHERE country.continent = 'Asia'
ORDER BY country.code   

SELECT Name, Population
FROM city
WHERE Population > (
    SELECT AVG(Population)
    FROM city
);

-- 전체 도시에 대한 평균 인구수에 대해서,
-- 그거보다 인구수가 많은 도시를 조회해줘
SELECT * 
FROM city
WHERE city.population > (
    SELECT AVG(city.population) FROM city
)

    SELECT AVG(city.population) FROM city


SELECT * FROM city