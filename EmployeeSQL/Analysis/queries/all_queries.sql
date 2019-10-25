ERD:
https://app.quickdatabasediagrams.com/#/d/khYwY6

Q1 CODE:
SELECT "Employees".employee_number,
    "Employees".last_name,
    "Employees".first_name,
    "Employees".gender,
    "Salaries".salary
   FROM "Employees"
     JOIN "Salaries" ON "Employees".employee_number = "Salaries".employee_number;
Q2 CODE:
SELECT
   "Employees".employee_number,
   "Employees".last_name,
   "Employees".first_name,
   "Employees".start_date
FROM
   "Employees"
WHERE EXTRACT(year FROM "start_date") = 1986;
Q3 CODE:
SELECT "Dept_Manager".department_number,
    "Dept_Manager".employee_number,
    "Dept_Manager".start_date,
    "Dept_Manager".end_date,
    "Departments".dept_name,
	"Employees".first_name,
	"Employees".last_name
   FROM "Dept_Manager"    
Join "Departments" on "Dept_Manager".department_number = "Departments".dept_number
Join "Employees" on "Dept_Manager".employee_number = "Employees".employee_number;

Q4 CODE:
SELECT "Employees".last_name,
    "Employees".first_name,
    "Dept_Employees".employee_number,
	"Departments".dept_name
   FROM "Employees"    
Join "Dept_Employees" on "Employees".employee_number = "Dept_Employees".employee_number
Join "Departments" on "Dept_Employees".dept_number = "Departments".dept_number;

Q5 CODE:
SELECT 
    "Employees".last_name,
    "Employees".first_name
FROM 
	"Employees"
WHERE 
	"Employees".first_name = 'Hercules'
AND
	"Employees".last_name LIKE 'B%';









Q6 CODE:
SELECT 
 	"Departments".dept_name,
    "Dept_Employees".employee_number,
    "Employees".first_name,
	"Employees".last_name
FROM
	"Departments”
JOIN "Dept_Employees" ON "Departments".dept_number = "Dept_Employees".dept_number
JOIN "Employees" ON "Dept_Employees".employee_number= "Employees".employee_number
WHERE
	"Departments".dept_name = 'Sales';


Q7 CODE:
SELECT 
 	"Departments".dept_name,
    "Dept_Employees".employee_number,
    "Employees".first_name,
	"Employees".last_name
FROM
	"Departments"
JOIN "Dept_Employees" ON "Departments".dept_number = "Dept_Employees".dept_number
JOIN "Employees" ON "Dept_Employees".employee_number= "Employees".employee_number
WHERE
	"Departments".dept_name = 'Sales' OR
	"Departments".dept_name = 'Development';



Q8 CODE:
SELECT
	"Employees".last_name,
	COUNT(DISTINCT "Employees".last_name)
FROM
	"Employees"
GROUP BY
	"Employees".last_name
ORDER BY
	"Employees".last_name DESC;

