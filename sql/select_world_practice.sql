-- Active: 1769143473833@@127.0.0.1@5432@world@public

SELECT * FROM city

SELECT * FROM country;

SELECT country.name, country.population FROM country;
-- 위와 아래 같은 내용의 코드 뒤의 c 로 앞의 country 줄임 가능 변수명 처럼
SELECT c.name, c.population FROM country c;

SELECT name, population FROM country;

SELECT name AS 국가명, population AS 인구수 FROM country;

SELECT DISTINCT continent FROM country;

-- 인구가 800만 이상인
-- 도시의
-- name, population을 조회하시오

SELECT c.name, c.population
FROM city c 
WHERE c.population >= 8000000;

-- 한국(KOR)에 있는 도시의 name, countrycode를 조회하시오

SELECT c.name, c.countrycode
FROM city c
WHERE countrycode in ('KOR')
-- 유럽 대륙에 속한 나라들의 name과 region을 조회하시오

SELECT c.name, c.region
FROM country c
WHERE continent IN ('Europe');

-- 이름이 'San'으로 시작하는 도시의 name을 조회하시오
SELECT c.name
FROM city c
WHERE name LIKE 'San%';

-- 독립 연도(IndepYear)가 1900년 이후인 나라의 name, indepyear를 조회하시오.
SELECT c.name, c.indepyear
FROM country c
WHERE c.indepyear > 1900;

-- 인구가 100만에서 200만 사이인 한국 도시의 name을 조회하시오
SELECT c.name 
FROM city c
WHERE countrycode IN ('KOR')
AND c.population >= 1000000
AND c.population <= 2000000;

-- 인구가 500만 이상인 한국, 일본, 중국의 도시의 name, countrycode, population 을 조회하시오

SELECT name, countrycode, population
FROM city c 
WHERE countrycode IN ('KOR', 'JPN', 'CHN')

-- 도시 이름이 'A'로 시작하고 'a'로 끝나는 도시의 name을 조회하시오.

SELECT name
FROM city c 
WHERE name LIKE 'A%'
AND name LIKE '%a'

-- 동남아시아(Southeast Asia) 지역(Region)에 속하지 않는 아시아(Asia) 대륙 나라들의 name, region을 조회하시오.

SELECT name
FROM country c
WHERE region IN ('Asia')
AND region NOT IN ('Southeast Asia')

-- 오세아니아 대륙에서 예상 수명의 데이터가 없는 나라의 name, lifeexpectancy, continent를 조회하시오.

SELECT name, lifeexpectancy, continent
FROM country c
WHERE lifeexpectancy IS NULL
AND continent IN ('Oceania')


---------------------------------------------------------------------------------

-- city 테이블에서 
-- 인구수가 가장 적은 
-- 도시 5개를 조회하시오.


-- country 테이블에서 
-- 기대수명이 높은 순서대로 
-- 1위부터 5위까지의 국가를 조회하시오. 



#- 대륙별 총 인구수를 구하시오.

SELECT continent, SUM(population) as max_pop
FROM country
GROUP BY continent

#- 대륙별 평균 GNP와 평균 인구를 구하시오.
SELECT continent,
AVG(population) as avg_pop,
AVG(GNP) as avg_gnp
FROM country
GROUP BY continent

#- 인구가 50만에서 100만 사이인 도시들에 대해, District별 도시 수를 구하시오.
SELECT district,
COUNT(*) as district_count
FROM city c
WHERE population >= 500000
AND population <= 10000000
GROUP BY district;
#- 아시아 대륙 국가들의 Region별 총 GNP를 구하세요.
SELECT region,
SUM(gnp) as avg_gnp
FROM country
WHERE continent in ('Asia')
GROUP BY region;

#- GNP가 가장 높은 Region를 찾으시오.(GNP : 국민 총 생산)
SELECT region,
SUM(gnp) as total_gnp
FROM country
GROUP BY region;

-- - 각 국가별 도시가 10개 이상인 국가의 CountryCode, 도시 수를 조회하시오.
SELECT countrycode,
COUNT(*)  as coun_code 
FROM city
GROUP BY countrycode
HAVING COUNT(*) >= 10;

-- - District별 평균 인구가 100만 이상이면서 도시 수가 3개 이상인 District,  도시 수, 총 인구를 구하시오
SELECT district, COUNT(*), SUM(population) AS "총인구"
FROM city
GROUP BY district
HAVING AVG(population) >= 1000000
    AND COUNT(*) >=3;
-- - 아시아 대륙의 국가들 중에서, Region별 평균 GNP가 1000 이상인 Region,  평균 GNP를 조회하시오
SELECT region, AVG(gnp)
FROM country
WHERE continent = 'Asia'
GROUP BY region
HAVING AVG(gnp) >= 1000;
-- - 독립년도가 1900년 이후인 국가들 중에서,
--대륙별 평균 기대수명이 70세 이상인
--Continent, 평균 기대수명을 조회하시오.
SELECT continent, AVG(lifeexpectancy)
FROM country
WHERE indepyear >= 1900
GROUP BY continent
HAVING AVG(lifeexpectancy) >= 70

-- - CountryCode별 도시 평균 인구가 100만 이상이고, CountryCode별 도시 최소 인구가 50만 이상인 데이터에서 CountryCode, 총 도시수, 총 인구수를 조회하시오. - city
SELECT countrycode, COUNT(*), SUM(population)
FROM city
GROUP BY countrycode
HAVING AVG(population) >= 1000000
AND MIN(population) >= 500000;
-- - CountryCode별 인구가 50만 이상인
-- city의 평균 인구가 100만 이상 인 국가의
--  CountryCode, 총 도시수, 총 인구수를 조회하시오.

SELECT countrycode,
COUNT(*) as city_count,
SUM(population) as total_pop 
FROM city 
WHERE population >= 500000
GROUP BY countrycode
HAVING AVG(population) >= 1000000