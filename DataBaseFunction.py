import sqlite3


def createTables1():
    connect = sqlite3.connect('./database.db')
    cursor = connect.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS user(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name VARCHAR,
    password VARCHAR,
    personally VARCHAR,
    phone VARCHAR
    )

    '''
    cursor.execute(sql)
    connect.commit()
    connect.close()


createTables1()


def createTables2():
    connect = sqlite3.connect('./database2.db')
    cursor = connect.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS user(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    academicyear INTEGER,
    firstname VARCHAR,
    lastname VARCHAR,
    classname INTEGER,
    gender VARCHAR,
    fathername VARCHAR,
    nationalcode VARCHAR,
    phonenumber VARCHAR,
    address VARCHAR

    )

    '''
    cursor.execute(sql)
    connect.commit()
    connect.close()


createTables2()


def insertUser(user_name, password, personally, phone):
    connect = sqlite3.connect('./database.db')
    cursor = connect.cursor()
    sql = 'INSERT INTO user VALUES (NULL,?, ?, ?, ?);'
    cursor.execute(sql, (user_name, password, personally, phone))
    connect.commit()
    connect.close()


def checkUser():
    connect = sqlite3.connect('./database.db')
    cursor = connect.cursor()
    sql = 'SELECT * FROM user'
    cursor.execute(sql)
    listUsers = []
    allUser = list(cursor)
    for i in allUser:
        listUser = list(i)
        listUsers.append({'name': listUser[1], 'password': listUser[2]})
    connect.commit()
    connect.close()
    return listUsers

def AddUser(academicyear, firstname, lastname , classname, gender, fathername, nationalcode, phonenumber, address):
    connect = sqlite3.connect('./database2.db')
    cursor = connect.cursor()
    sql = 'INSERT INTO user VALUES (NULL,?, ?, ?, ?, ?, ?, ?, ?, ?);'
    cursor.execute(sql, (academicyear, firstname, lastname , classname, gender, fathername, nationalcode, phonenumber, address))
    connect.commit()
    connect.close()

def CheckStudent():
    connect = sqlite3.connect('./database2.db')
    cursor = connect.cursor()
    sql = 'SELECT * FROM user'
    cursor.execute(sql)
    listUsers = []
    allUser = list(cursor)
    for i in allUser:
        listUser = list(i)
        listUsers.append({'firstname': listUser[2], 'lastname': listUser[3], 'nationalcode': listUser[7]})
    connect.commit()
    connect.close()
    return listUsers

def RemoveUser(nationalcode):
    connect = sqlite3.connect('./database2.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM user WHERE nationalcode = ?;',  (nationalcode,))
    connect.commit()
    connect.close()

print(CheckStudent())

