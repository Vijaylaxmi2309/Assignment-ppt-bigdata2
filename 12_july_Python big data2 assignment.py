#!/usr/bin/env python
# coding: utf-8

# 1. Write an SQL query to retrieve the names and email addresses of all employees from a table named "Employees".
# 2. Write an SQL query to filter records from a table named "Customers" where the "City" column is 'New York'.
# 3. Write an SQL query to sort records in descending order based on the "DateOfBirth" column in a table named "Users".
# 4. Write an SQL query to sort records in ascending order based on the "RegistrationDate" column in a table named "Users".
# 5. Write an SQL query to find the employee with the highest salary from a table named "Employees" and display their name, position, and salary.
# 6. Write an SQL query to retrieve records from a table named "Customers" where the "Phone" column matches the pattern '+1-XXX-XXX-XXXX'.
# 7. Write an SQL query to retrieve the top 5 customers with the highest total purchase amount from a table named "Orders" and display their names and total purchase amounts.
# 8. Write an SQL query to calculate the percentage of sales for each product category in a table named "Sales" and display the category name, total sales amount, and the percentage of total sales.
# 9. Write an SQL query to find the customers who have made the highest total purchases across all years from a table named "Orders" and display their names, email addresses, and the total purchase amount.
# 
# 
# 

# #1ANS
# SELECT Name, Email
# FROM Employees;
# 

# #2ANS
# SELECT *
# FROM Customers
# WHERE City = 'New York';
# This query selects all columns (*) from the "Customers" table and applies a condition in the WHERE clause to filter the records where the "City" column is equal to 'New York'. You can replace * with specific column names if you only want to retrieve certain columns from the table.
# 

# #3ANS
# SELECT *
# FROM Users
# ORDER BY DateOfBirth DESC;
# 

# #4ANS
# SELECT *
# FROM Users
# ORDER BY RegistrationDate ASC;
# 

# #5ANS
# SELECT Name, Position, Salary
# FROM Employees
# WHERE Salary = (SELECT MAX(Salary) FROM Employees);
# 

# #6ANS
# SELECT *
# FROM Customers
# WHERE Phone LIKE '+1-___-___-____';
# 

# #7ANS
# SELECT CustomerName, SUM(PurchaseAmount) AS TotalPurchaseAmount
# FROM Orders
# GROUP BY CustomerName
# ORDER BY TotalPurchaseAmount DESC
# LIMIT 5;
# 

# #8ANS
# SELECT CategoryName, SUM(SalesAmount) AS TotalSalesAmount, 
#        (SUM(SalesAmount) / (SELECT SUM(SalesAmount) FROM Sales)) * 100 AS PercentageOfTotalSales
# FROM Sales
# GROUP BY CategoryName;
# 
# 

# #9ANS
# SELECT CustomerName, Email, SUM(PurchaseAmount) AS TotalPurchaseAmount
# FROM Orders
# GROUP BY CustomerName, Email
# HAVING SUM(PurchaseAmount) = (SELECT MAX(TotalPurchaseAmount) FROM
#                               (SELECT CustomerName, Email, SUM(PurchaseAmount) AS TotalPurchaseAmount
#                                FROM Orders
#                                GROUP BY CustomerName, Email) AS SubQuery);
# 

# In[ ]:




