import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database=""
)
def query_function(question,quary):
    print(f"\n {question} \n")
    cur.execute(quary) 
    row=cur.fetchall()
    for i in row:
        print(i)

if mydb.is_connected():
    print("The database is connected Successfully!!")
cur=mydb.cursor()
query_function("1. Show all data from the giet table.","select * from giet2")
query_function("2. Display only the name column","select Name from giet2")
query_function("3. Display name and address of all employees","select Name, Address from giet2")
query_function("4. Show roll and salary of all employees","select Rollno, Salary from giet2")
query_function("5. Display all employees whose name is 'aman'","select * from giet2 where Name='aman'")
query_function("6. Show employees who live in 'delhi'","select * from giet2 where Address='delhi'")
query_function("7. Display all employees whose gender is 'M","select * from giet2 where Gender='M'")
query_function("8. Show employees whose designation is 'doctor'","select * from giet2 where Desig='doctor'")
query_function("9. Display employees having salary 15000.","select * from giet2 where Salary=15000")
query_function("10. Show employees with salary greater than 20000.","select * from giet2 where Salary>20000")
query_function("11. Display employees with salary less than 30000","select * from giet2 where Salary<30000")
query_function("12. Show employees who are male AND have salary > 20000.","select * from giet2 where Salary>20000 and Gender='M'")
query_function("13. Display employees who are female OR live in 'raipur'.","select * from giet2 where Address='raipur' or Gender='F'")
query_function("14. Show employees whose name starts with 'a'." ,"select * from giet2 where Name like 'a%'")
query_function("15. Display employees whose name ends with 'h'.","select * from giet2 where Name like '%h'")
query_function("16. Show employees whose address contains 'pur'","select * from giet2 where Address like '%pur'")
query_function("17. Display all employees sorted by name in ascending order.","select * from giet2 ORDER BY Name asc")
query_function("18. Show all employees sorted by salary in descending order.","select * from giet2 ORDER BY Salary desc")
query_function("19. Count total number of employees in the table","select count(Name) from giet2 ")
query_function("20. Count number of employees whose gender is 'M'","select count(Name) from giet2 where Gender='M'")
# #1. Show all data from the giet table.
# cur.execute("select * from giet2") 
# row=cur.fetchall()
# for i in row:
#     print(i)

# #2. Display only the name column
# print("  Display only the name column    ")
# cur.execute("select Name from giet2")
# res=cur.fetchall()
# for x in res:
#     print(f"Name: {x[0]}")

# #3. Display name and address of all employees
# print(      "Display name and address of all employees"     )
# cur.execute("select Name, Address from giet2")
# result=cur.fetchall()
# for i in result:
#     print(f"Name: {i[0]} and Address: {i[1]}")
# #4. Show roll and salary of all employees5. Display all employees whose name is 'aman'
# print("\n Display all employees whose name
# print(" \nShow roll and salary of all employees     ")
# cur.execute("select Rollno, Salary from giet2")
# roll=cur.fetchall()
# for i in roll:
#     print(f"Roll-No: {i[0]} and Salary: {i[1]}")

# # is 'aman'")
# cur.execute("select * from giet2 where Name='aman'")
# name=cur.fetchall()
# for i in roll:
#     print(f"Roll-No: {i[0]} and Salary: {i[1]}")
cur.close()
mydb.close()