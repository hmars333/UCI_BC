SELECT 
    "Employees".last_name,
    "Employees".first_name
FROM 
	"Employees"
WHERE 
	"Employees".first_name = 'Hercules'
AND
	"Employees".last_name LIKE 'B%';