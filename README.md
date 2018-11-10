## introduction

This is Abdulrahman Fantoukh submission for Udacity log analysis project

I used python version 3.7 in this project

## code design

There are 3 functions that execute 3 queries one function execute one query from the database news.

In each query I made the connection to the database and created a cursor object then executed the query using the cursor after that I displayed the result then close the connection.

**Note:** before displaying any query result I had to do some changes for the output before displaying it.
I created 2 view to simplify the third query 
The view E_table it has 2 column the date and the count (the number of rejected requests to the website that have 404 not found error)

View "public.e_table"
 Column |  Type  | Modifiers 
--------+--------+-----------
 date   | text   | 
 count  | bigint | 


The view E_table it has 2 column the date and the count (the number of total requests to the website)
And the the view T_table 

View "public.t_table"
 Column |  Type  | Modifiers 
--------+--------+-----------
 date   | text   | 
 count  | bigint | 

## References

* (https://stackoverflow.com/questions/23276344/like-operator-in-inner-join-in-sql)
To join tow tables that doesn't have common columns. 


* (https://www.postgresql.org/docs/9.1/functions-datetime.html)
To extract only the date from timestamp type columns.

* (https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points)
To round up the float values.

* (https://w3resource.com/PostgreSQL/concat-function.php)
To concat 2 strings in Postgresql.