import pymysql


def get_connect():
    conn = pymysql.connect(
        host='127.0.0.1', user='root', password='1234', db='world', charset='utf8')
    if conn:
        print('연결 완료 !!!')
    return conn

# get_connect()


def get_country_list():
    conn = get_connect()

    cursor = conn.cursor()

    cursor.execute('''
    SELECT Code, Name, Continent, Population, GNP FROM country LIMIT 10;
    ''')

    country_list = cursor.fetchall()

    # print(country_list)
    conn.close()
    return country_list


get_country_list()
