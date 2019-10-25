SELECT "Employees".employee_number,
    "Employees".last_name,
    "Employees".first_name,
    "Employees".start_date
   FROM "Employees"
  WHERE date_part('year'::text, "Employees".start_date)