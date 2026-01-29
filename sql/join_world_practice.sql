-- Active: 1769143442347@@127.0.0.1@5432@world@public
-- 어느 나라에 속한 도시인지

SELECT city.name city_name, country.name coutry_name
FROM city
JOIN country ON city.countrycode = country.code;

-- 국가와 그 국가의 공식 수도를 매칭
SELECT country.name country_name, city.name city_name
FROM city
JOIN country ON country.capital = city.id;

-- 특정 대륙에 속한 도시들 목록
-- city + country를 join / continent 별로 filtering을 해야 겠다.
SELECT ci.name, co.name, co.continent
FROM city ci
JOIN country co ON ci.countrycode = co.code
WHERE co.continent = 'Asia'
ORDER BY co.name

-- 특정 대륙에서 인구가 500만 명 이상인 도시만 조회
SELECT ci.name, co.name, co.continent
FROM city ci
JOIN country co ON ci.countrycode = co.code
WHERE co.continent = 'Asia'
    AND ci.population >= 500000;

-- 국가와 수도, 공식언어 가져오기

SELECT co.name country_name, ci.name capital_name, cl."Language"
FROM country co
JOIN city ci ON ci.id = co.capital
JOIN countrylanguage cl ON cl.countrycode = co.code
WHERE cl.isofficial = 'T'

SELECT co.name country_name, ci.name capital_name, cl."Language"
FROM country co
JOIN city ci ON ci.id = co.capital
JOIN countrylanguage cl ON cl.countrycode = co.code
WHERE countrylanguage.isofficial = 'T'