{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf100
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Regular;\f2\fnil\fcharset0 LucidaGrande;
\f3\fnil\fcharset178 GeezaPro;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\csgray\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh15420\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs28 \cf0 #Log analysis project\
\
## introduction\
\
This is Abdulrahman Fantoukh submission for Udacity log analysis project\
\
I used python version 3.7 in this project \
\
## code design\
\
There are 3 functions that execute 3 queries one function execute one query from the database news.\
\
In each query I made the connection to the database and created a cursor object then executed the query using the cursor after that I displayed the result then close the connection.\
\
**Note:** before displaying any query result I had to do some changes for the output before displaying it.\
I created 2 view to simplify the third query \
The view E_table it has 2 column the date and the count (the number of rejected requests to the website that have 404 not found error)\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f1\fs26 \cf2 \CocoaLigature0     View "public.e_table"\
 Column |  Type  | Modifiers \
--------+--------+-----------\
 date   | text   | \
 count  | bigint | \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs28 \cf0 \CocoaLigature1 \
The view E_table it has 2 column the date and the count (the number of 
\f2 total
\f3  
\f0 requests to the website)\
And the the view T_table \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f1\fs26 \cf2 \CocoaLigature0     View "public.t_table"\
 Column |  Type  | Modifiers \
--------+--------+-----------\
 date   | text   | \
 count  | bigint | \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs28 \cf0 \CocoaLigature1 \
\
## References  \
\
* (https://stackoverflow.com/questions/23276344/like-operator-in-inner-join-in-sql)\
To join tow tables that doesn't have common columns. \
\
\
* (https://www.postgresql.org/docs/9.1/functions-datetime.html)\
To extract only the date from timestamp type columns.\
\
* (https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points)\
To round up the float values.\
\
* (https://w3resource.com/PostgreSQL/concat-function.php)\
To concat 2 strings in Postgresql.}