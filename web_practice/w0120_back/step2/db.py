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
    
    temp_list=[]
    for row in country_list:
        temp_dict={}
        temp_dict['Code']=row[0]
        temp_dict['Name']=row[1]
        temp_dict['Continent']=row[2]
        temp_dict['Population']=row[3]
        temp_dict['GNP']=row[4]
        temp_list.append(temp_dict)
    # print(country_list)
    conn.close()
    return temp_list


get_country_list()