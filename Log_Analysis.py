#!/usr/bin/env python3
import psycopg2

db_Name = "news"

def Query1():
    connection = psycopg2.connect(database=db_Name)
    cursor = connection.cursor()
    query = '''select title, count(*) as views
       from log join articles
       on log.path = concat('/article/', articles.slug)
       group by title
       order by views desc
       limit 3;'''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    print("--------------------------------------------------------------")
    print("The most popular three articles of all time")
    for i in result:
        h = '"' + i[0] + '"' + ' - ' + str(i[1]) + ' views'
        print(h)
    connection.close()


def Query2():
    connection = psycopg2.connect(database=db_Name)
    cursor = connection.cursor()
    query = '''select name,views
    from authors join (select author,count(path) as views
    from log join articles on log.path = concat('/article/', articles.slug)
    where status = '200 OK'
    group by author) as t on authors.id = t.author
    order by views desc;'''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    print("--------------------------------------------------------------")
    print("The most popular article authors of all time")
    for i in result:
        h = i[0] + ' - ' + str(i[1]) + ' views'
        print(h)
    connection.close()


def Query3():
    connection = psycopg2.connect(database=db_Name)
    cursor = connection.cursor()
    query = '''select er,date from
    (select ((E_table.count * (1.0) / T_table.count) / 0.01 )
    as er,T_table.date from E_table join T_table
    on E_table.date = T_table.date) as ER where er >1 ;'''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    print("--------------------------------------------------------------")
    print("Days have more than 1" + '%' + " of error requests")
    for i in result:
        er = str(round(i[0], 2)) + " %"
        s = str(i[1])
        display = s + ' - ' + er + 'error'
        print(display)
    connection.close()


if __name__ == '__main__':
    Query1()
    Query2()
    Query3()
