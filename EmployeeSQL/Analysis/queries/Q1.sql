 SELECT "Employees".employee_number,
    "Employees".last_name,
    "Employees".first_name,
    "Employees".gender,
    "Salaries".salary
   FROM "Employees"
     JOIN "Salaries" ON "Employees".employee_number = "Salaries".employee_number;