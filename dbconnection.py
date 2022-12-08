#lang -> db 

#oracle -> java: python: ruby: .net: 
#java  -> mysql [mysql_connector.jar] [ download buildpath ] 
#python -> mysql [connector]

# driver -> 
# url 
# username 
# password


import mysql.connector 
  

db = mysql.connector.connect(host="localhost",user="root",password="root",database="intern")
print(db)

#ddl query  - autocommit 
# createUser = "create table users (userId integer primary key auto_increment,email varchar(30),password varchar(30))"
# cursor = db.cursor() 
# cursor.execute(createUser)


def addUser():
    #dml - commit
    # insertUser = "insert into users (email,password) values ('ram','ram123')"

    print("enter email and password")
    email = input()
    password = input()

    # insertUser = "insert into users (email,password) values ('"+email+"','"+password+"')"
    insertUser = "insert into users (email,password) values (%s,%s)"
    data =(email,password) 

    cursor =db.cursor() 
    cursor.execute(insertUser,data)
    print(cursor.rowcount," row inserted")
    db.commit() 


def listUsers():
    cursor = db.cursor()
    cursor.execute("select * from users")
    
    users = cursor.fetchall()
    
    print("Total ",len(users)," Users found...")
    print(users)
    
    for user in users:
        print(user)



# listUsers()
addUser()



