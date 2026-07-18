# GROUP BY
- 특정 필드(들)을 기준으로 나누어 계산하는 것
- 집계 함수와 함께 사용되어, 그룹을 묶어 계산하게 됨

## 예시
```sql
SELECT Country, COUNT(CustomerID) AS TotalCustomers
FROM Customers
GROUP BY Country;
```
- `Country` 필드를 기준으로, 그룹함
- 각 그룹에 있는 `CustomerID`를 **COUNT**함
- COUNT한 결과를 TotalCustomers라는 필드로 저장함
```
ountry	TotalCustomers
Korea	3
USA	2
Japan	1
```
- 최종 위와 같이 나오게 됨
### 주의
- GROUP BY에서 SELECT에 사용할 수 있는 컬럼
	- GROUP BY에 사용한 컬럼
	- 집계 함수(COUNT, SUM, AVG, MAX, MIN)를 적용한 컬럼

# HAVING
- 그룹에 대한 결과를 필터링함
- WHERE과 달리 GROUP BY 뒤에 실행됨

## 예시
```sql
SELECT department, COUNT(employee_id) AS total_staff
FROM employees
GROUP BY department
HAVING COUNT(employee_id) > 5;
```
- 직원 수가 5명 이상인 그룹만 필터링함
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
WHERE status = 'Full-Time'  -- Filters rows first
GROUP BY department
HAVING AVG(salary) > 70000; -- Filters groups last
```
- 위와 같이 각 직원에 대한 필터링은 WHERE로 수행
- 각 그룹에 대한 필터링은 HAVING으로 수행

# SQL의 실행 순서
```
FROM
→ JOIN
→ WHERE
→ GROUP BY
→ HAVING
→ SELECT
→ DISTINCT
→ ORDER BY
→ LIMIT
```
