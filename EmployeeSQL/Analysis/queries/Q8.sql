 SELECT "Employees".last_name,
    count(DISTINCT "Employees".last_name) AS count
   FROM "Employees"
  GROUP BY "Employees".last_name
  ORDER BY "Employees".last_name DESC;