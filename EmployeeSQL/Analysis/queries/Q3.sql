SELECT "Dept_Manager".department_number,
    "Dept_Manager".employee_number,
    "Dept_Manager".start_date,
    "Dept_Manager".end_date,
    "Departments".dept_name,
    "Employees".first_name,
    "Employees".last_name
   FROM "Dept_Manager"
     JOIN "Departments" ON "Dept_Manager".department_number::text = "Departments".dept_number::text
     JOIN "Employees" ON "Dept_Manager".employee_number = "Employees".employee_number)