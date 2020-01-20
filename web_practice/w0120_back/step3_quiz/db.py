import pymysql


def get_connect():
    conn = pymysql.connect(
        host='127.0.0.1', user='root', password='1234', db='sqldb', charset='utf8')
    if conn:
        print('연결 완료 !!!')
    return conn

# get_connect()


def get_user_list():
    conn = get_connect()

    cursor = conn.cursor()

    cursor.execute('''
    SELECT userID, name, birthYear, addr FROM usertbl LIMIT 10;
    ''')

    user_list = cursor.fetchall()
    
    # print(country_list)
    conn.close()
    return user_list


get_user_list()