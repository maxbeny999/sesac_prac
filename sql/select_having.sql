---------------------------------------------------------
-- HAVING 수업자료

-- 대륙 별 국가 수가 20개가 넘는 대륙, 국가 수 조회
-- 대륙 별 국가 수 조회
SELECT continent, COUNT(*) 
FROM country
GROUP BY continent
HAVING COUNT(*) >= 20;

-- 인구수가 10000000보다 많은 국가들에 대해,
-- continent별로 그룹핑하여 그 개수가 20개가 넘는 대륙, 국가 수 조회
SELECT continent, COUNT(*) 
FROM country
WHERE population >= 10000000 -- group by보다 where가 먼저 적용된다.
GROUP BY continent
HAVING COUNT(*) >= 20; -- group by를 통해 나온 column인 aggregation function을 기준으로 조건을 건다.

-- Region 별 
-- 평균 인구가 10000000이 넘는 
-- 지역, 평균 인구 조회
SELECT region, AVG(population)
FROM country
GROUP BY region
HAVING AVG(population) > 10000000
ORDER BY AVG(population) DESC;

-- # 아래의 구문은 국가들 중 pop이 천만이 넘는 것들만 골라다가
-- # 다시 region별로 묶어서 avg를 계산한다.
SELECT region, AVG(population)
FROM country
WHERE population > 10000000
GROUP BY region
ORDER BY AVG(population) DESC;

-- 인구가 1000만 이상인 국가의 수가 
-- 10개가 넘는 대륙의 이름과 국가 수 조회
-- 1. 인구의 수가 1000만 이상인 국가만 모을꺼야.
-- 2. 그것의 개수가 10개가 넘는지 확인할꺼야.
SELECT continent, COUNT(*)
FROM country
WHERE population > 10000000 -- country별 필터링 / ` 인구가 1000만 이상인 국가만 고르기
GROUP BY continent
HAVING COUNT(*) >= 10; -- 그룹별 aggregation한 결과에 대해 필터링

-- 평균 인구수가 10000000 이 넘는 대륙 의 국가 수 
SELECT continent, COUNT(*)
FROM country
GROUP BY continent
HAVING AVG(population) > 10000000;


SELECT continent, governmentform, COUNT(*)
FROM country
GROUP BY continent, governmentform
ORDER BY continent, governmentform;

SELECT continent,  COUNT(*)
FROM country
GROUP BY continent
ORDER BY continent;

---------------------------------------------------------
-- HAVING 문제

-- - 각 국가별 도시가 10개 이상인 국가의 CountryCode, 도시 수를 조회하시오.
SELECT countrycode, COUNT(*)
FROM city
GROUP BY countrycode
HAVING COUNT(*) >= 10;


-- District별 
-- 평균 인구가 100만 이상이면서 
-- 도시 수가 3개 
-- 이상인 District,  도시 수, 총 인구를 구하시오
SELECT district, COUNT(*), SUM(population) AS "총인구"
FROM city
GROUP BY district
HAVING AVG(population) >= 1000000
    AND COUNT(*) >= 3;


-- - 아시아 대륙의 국가들 중에서,
--  Region별 평균 GNP가 1000 이상인 
--  Region,  평균 GNP를 조회하시오
SELECT region, AVG(gnp) 
FROM country
WHERE continent = 'Asia'
GROUP BY region
HAVING AVG(gnp) >= 1000;


--- 독립년도가 1900년 이후인 국가들 중에서, 
-- 대륙별 
-- 평균 기대수명이 70세 이상인 
-- Continent, 평균 기대수명을 조회하시오.
SELECT continent, AVG(lifeexpectancy), avg(population)
FROM country
WHERE indepyear >= 1900
GROUP BY continent
HAVING AVG(lifeexpectancy) >= 70;


-- - CountryCode별 도시 평균 인구가 100만 이상이고, 
-- CountryCode별 도시 최소 인구가 50만 이상인 데이터에서 
-- CountryCode, 총 도시수, 총 인구수를 조회하시오. 
SELECT countrycode, COUNT(*), SUM(population)
FROM city
GROUP BY countrycode
HAVING AVG(population) >= 1000000
    AND MIN(population) >= 500000;


-- - 인구가 50만 이상인 city 중 
-- CountryCode별 도시 평균 인구가 100만 이상 인 
-- 국가의 
-- CountryCode, 총 도시수, 총 인구수를 조회하시오.
SELECT countrycode, COUNT(*), SUM(population)
FROM city
WHERE population >= 5000000
GROUP BY countrycode
HAVING AVG(population) >= 1000000;
