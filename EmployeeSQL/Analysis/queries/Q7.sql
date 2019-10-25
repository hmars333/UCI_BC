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