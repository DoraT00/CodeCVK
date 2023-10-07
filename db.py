import pymysql

from config import db_name, host, password, user

# "CREATE TABLE `order`(id int AUTO_INCREMENT, name varchar(32), description varchar(255), time_order date, deadline varchar(32), message varchar(127), status varchar(32), PRIMARY KEY (id) ) "

def connect():
    try:    
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        #print("successfully connected...")
        return connection
    except Exception as ex:
        print("Connection refused...")
        print(ex)

def create():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "CREATE TABLE `orders`(id int AUTO_INCREMENT, id_player varchar(128), name varchar(32), description varchar(255), time_order date, deadline varchar(32), status varchar(32), PRIMARY KEY (id) ) "
            cursor.execute(sql)
            connection.commit()
    finally:
            connection.close()


