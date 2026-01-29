---------------------------------------------------------
-- GROUP BY 문제
-- 대륙별 
-- 총 인구수를 구하시오.
-- asia : 인구수의 합
-- africa : 인구수의 합
SELECT continent, SUM(population)
FROM country
GROUP BY continent;

-- 대륙별 
-- 평균 GNP와 
-- 평균 인구를 구하시오.
SELECT 
    continent, 
    AVG(gnp) AS avg_gnp, 
    AVG(population) AS avg_pop
FROM country
GROUP BY continent;

-- 인구가 50만에서 100만 사이인 
-- 도시들에 대해, 
-- District별 
-- 도시 수를 구하시오.
SELECT district, count(*) 
FROM city
WHERE population BETWEEN 500000 AND 1000000
GROUP BY district
ORDER BY count(*) DESC;

-- 아시아 대륙(contient가 asia인)
-- 국가들의 
-- Region별 
-- 총 GNP를 구하세요.
SELECT region, sum(gnp)
FROM country
WHERE continent = 'Asia'
GROUP BY region;

--- 대륙 별 
-- 국가 수가 많은 순서대로 -> ORDER BY
-- Continent, 국가 수를 조회하시오.
SELECT continent, COUNT(*) as country_count
FROM country
GROUP BY continent
-- ORDER BY COUNT(*);
ORDER BY country_count;


-- - 독립년도가 있는 -> WHERE
-- 국가들의 
-- 대륙 별 평균 기대수명이 높은 순서대로 
-- Continent, 평균 기대수명을 조회하시오.
SELECT continent, AVG(lifeexpectancy)
FROM country
WHERE indepyear IS NOT NULL
GROUP BY continent
ORDER BY AVG(lifeexpectancy) DESC;


-- - GNP가 가장 높은 Region를 찾으시오.(GNP : 국민 총 생산)-
-- region별 gnp의 합계 순으로 정렬하시오. 그것들 중에서 1등을 찾으시오.
SELECT region, SUM(gnp)
FROM country
GROUP BY region
ORDER BY SUM(gnp) DESC
LIMIT 1;