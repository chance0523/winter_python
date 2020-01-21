import pymysql


def get_connect():
    conn = pymysql.connect(
        host='127.0.0.1', user='root', password='1234', db='sqldb', charset='utf8')
    if conn:
        # print('연결 완료 !!!')
        pass
    return conn


def get_list():
    conn = get_connect()

    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM memberTbl ORDER BY joinDate DESC;
    ''')

    result_list = cursor.fetchall()

    dict_list = []
    for row in result_list:
        temp_dict = {}
        temp_dict['useId'] = row[0]
        temp_dict['password'] = row[1]
        temp_dict['email'] = row[2]
        temp_dict['joinDate'] = row[3]
        dict_list.append(temp_dict)

    conn.close()
    return dict_list


# print(get_list())

# userId, password를 매개변수로 받은 후 DB에 있는지 확인
def login_result(userId, password):
    conn = get_connect()

    cursor = conn.cursor()

    sql = ('''
    SELECT * FROM memberTbl WHERE userId=%s AND password=%s;
    ''')

    cursor.execute(sql, (userId, password))
    login_result = cursor.fetchone()

    conn.close()
    if login_result:
        return True
    else:
        return False

print(login_result('melon','1234'))
print(login_result('melon','4321'))
print(login_result('cherry','4321'))
