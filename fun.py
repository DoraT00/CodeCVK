from config import channel_id, roles_id, roles_id_of
from db import connect

# fun database

def insert(id_player, name, description, deadline, time_order, status):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO `orders` (id_player, name, description, deadline, time_order, status) VALUES ('{id_player}', '{name}', '{description}', '{deadline}', '{time_order}', '{status}')"
            cursor.execute(sql)
            connection.commit()
    finally:
            connection.close()


def update(id, newstatus = "Не выполнено",): #id, newstatus
    connection = connect()
    try:
        with connection.cursor() as cursor:
            if(type(id) is int):
                sql = f"UPDATE `orders` SET status = '{newstatus}' WHERE id = '{id}'"
                cursor.execute(sql)
                connection.commit()

    finally:
        connection.close()



def find(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            if(type(id) is int):
                sql = f"SELECT id_player FROM `orders` WHERE id = '{id}'"
                cursor.execute(sql)
                member = cursor.fetchall()
                if(member != ()):
                    return list(member[0].values())[0]      
                else:
                    return None 
            else:
                return None
    finally:
        connection.close()
def get_status(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
                if(type(id) is int):
                    sql = f"SELECT status FROM `orders` WHERE id = '{id}'"
                    cursor.execute(sql)
                    member = cursor.fetchall()
                    if(member != ()):
                        return list(member[0].values())[0]      
                    else:
                        return None 
                else:
                    return None
    finally:
        connection.close()

def get_description(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
                if(type(id) is int):
                    sql = f"SELECT description FROM `orders` WHERE id = '{id}'"
                    cursor.execute(sql)
                    member = cursor.fetchall()
                    if(member != ()):
                        return list(member[0].values())[0]      
                    else:
                        return None 
                else:
                    return None
    finally:
        connection.close()

def get_name(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
                if(type(id) is int):
                    sql = f"SELECT name FROM `orders` WHERE id = '{id}'"
                    cursor.execute(sql)
                    member = cursor.fetchall()
                    if(member != ()):
                        return list(member[0].values())[0]      
                    else:
                        return None 
                else:
                    return None
    finally:
        connection.close()

def lowid():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id FROM `orders`"
            cursor.execute(sql)
            lowidd = cursor.fetchall()
            if(lowidd != ()):
                return list(lowidd[-1].values())[0]+1
            else:
                return 1
    finally:
        connection.close()

def get_warns_player(name):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT warns FROM `warns` WHERE name = '{name}'"
            cursor.execute(sql)
            warns = cursor.fetchall()
            if(warns != ()):
                return list(warns[0].values())[0]
            else:
                return 0
    finally:
        connection.close()



def add_warn(name, id_player = None):
    connection = connect()
    count_warns = get_warns_player(name)  
    try:
        if(count_warns != 0):
            with connection.cursor() as cursor:
                warns = count_warns+1  
                sql = f"UPDATE `warns` SET warns = '{warns}' WHERE name = '{name}'"
                cursor.execute(sql)
                connection.commit()
        else:
            with connection.cursor() as cursor: 
                warns = 1
                sql = f"INSERT INTO `warns` (name, id_player, warns) VALUES ('{name}', '{id_player}', '{warns}')"
                cursor.execute(sql)
                connection.commit()
    finally:
        connection.close()

def remove_warn(name):
    connection = connect()
    count_warns = get_warns_player(name)  
    try:
        if(count_warns != ()):
            with connection.cursor() as cursor:
                warns = count_warns-1
                if(warns > 0):  
                    sql = f"UPDATE `warns` SET warns = '{warns}' WHERE name = '{name}'"
                    cursor.execute(sql)
                    connection.commit()
                else: 
                    sql = f"DELETE FROM `warns` WHERE name = '{name}'"
                    cursor.execute(sql)
                    connection.commit()
        else:
            return None
    finally:
        connection.close()

def remove_warns(name):
    connection = connect()
    count_warns = get_warns_player(name)
    try:
        if(count_warns != ()):
            with connection.cursor() as cursor:
                sql = f"DELETE FROM `warns` WHERE name = '{name}'"
                cursor.execute(sql)
                connection.commit()
        else:
            return None
    finally:
        connection.close()

# fun list roles and channel

def get_roles_of_index(index):
    return list(roles_id_of.values())[index]

def get_roles_index(index):
    return list(roles_id.values())[index]

def get_roles_namelist():
    return list(roles_id.keys())

def get_index_user_id_role(user_role):
    return list(roles_id.values()).index(find_roles(user_role, 'next'))



def find_roles(id_role, perwornext):
    count = 0
    list_roles = list(roles_id.values())
    for i in list_roles: 
        if(id_role == i):
            if(count-1 >= 1 and perwornext == 'prew'):
                return get_roles_index(count-1)
            elif(count+1 < len(list_roles) and count+1 > 1 and perwornext == 'next'):
                return get_roles_index(count+1)
            else:
                return "Error"
        count += 1 


def find_id_roles_namelist(name_: list):
    for i in range(len(name_)):
        for j in range(len(get_roles_namelist())):
            if(name_[i] == get_roles_namelist()[j] and name_[i] != 'Солдат'):
                return get_roles_index(j)

def get_channel(index):
    return list(channel_id.values())[index]