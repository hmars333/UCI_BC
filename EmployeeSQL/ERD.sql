-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/khYwY6
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "Departments" (
    "dept_number" VARCHAR   NOT NULL,
    "dept_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "dept_number"
     )
);

CREATE TABLE "Dept_Employees" (
    "employee_number" INTEGER   NOT NULL,
    "dept_number" VARCHAR   NOT NULL,
    "start_date" DATE   NOT NULL,
    "end_date" DATE   NOT NULL,
    CONSTRAINT "pk_Dept_Employees" PRIMARY KEY (
        "dept_number"
     )
);

CREATE TABLE "Dept_Manager" (
    "department_number" VARCHAR   NOT NULL,
    "employee_number" INTEGER   NOT NULL,
    "start_date" DATE   NOT NULL,
    "end_date" DATE   NOT NULL,
    CONSTRAINT "pk_Dept_Manager" PRIMARY KEY (
        "department_number"
     )
);

CREATE TABLE "Employees" (
    "employee_number" INTEGER   NOT NULL,
    "birthdate" DATE   NOT NULL,
    "first_name" VARCHAR   NOT NULL,
    "last_name" VARCHAR   NOT NULL,
    "gender" CHAR(1)   NOT NULL,
    "start_date" DATE   NOT NULL,
    CONSTRAINT "pk_Employees" PRIMARY KEY (
        "employee_number"
     )
);

CREATE TABLE "Salaries" (
    "employee_number" INTEGER   NOT NULL,
    "salary" INTEGER   NOT NULL,
    "start_date" DATE   NOT NULL,
    "end_date" DATE   NOT NULL,
    CONSTRAINT "pk_Salaries" PRIMARY KEY (
        "employee_number"
     )
);

CREATE TABLE "Titles" (
    "employee_number" INTEGER   NOT NULL,
    "title" VARCHAR   NOT NULL,
    "start_date" DATE   NOT NULL,
    "end_date" DATE   NOT NULL,
    CONSTRAINT "pk_Titles" PRIMARY KEY (
        "employee_number"
     )
);

ALTER TABLE "Departments" ADD CONSTRAINT "fk_Departments_dept_number" FOREIGN KEY("dept_number")
REFERENCES "Dept_Manager" ("department_number");

ALTER TABLE "Dept_Employees" ADD CONSTRAINT "fk_Dept_Employees_employee_number" FOREIGN KEY("employee_number")
REFERENCES "Employees" ("employee_number");

ALTER TABLE "Dept_Employees" ADD CONSTRAINT "fk_Dept_Employees_dept_number" FOREIGN KEY("dept_number")
REFERENCES "Dept_Manager" ("department_number");

ALTER TABLE "Employees" ADD CONSTRAINT "fk_Employees_employee_number" FOREIGN KEY("employee_number")
REFERENCES "Titles" ("employee_number");

ALTER TABLE "Salaries" ADD CONSTRAINT "fk_Salaries_employee_number" FOREIGN KEY("employee_number")
REFERENCES "Titles" ("employee_number");

