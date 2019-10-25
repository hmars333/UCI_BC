SELECT "Employees".last_name,
    "Employees".first_name,
    "Dept_Employees".employee_number,
	"Departments".dept_name
   FROM "Employees"    
Join "Dept_Employees" on "Employees".employee_number = "Dept_Employees".employee_number
Join "Departments" on "Dept_Employees".dept_number = "Departments".dept_number;








