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
    SELECT Code, Name, Continent, Population, GNP FROM countryTb;
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

    # print(temp_list)
    conn.close()
    return temp_list

# 데이터베이스에 레코드 추가 함수
def add_record(c_code, c_name, c_continent, c_population, c_gnp):
    # db 연결
    conn=get_connect()
    
    sql='''
    INSERT INTO countryTb (Code, Name, Continent, Population, GNP)
    VALUES (%s, %s, %s, %s, %s);
    '''

    cursor=conn.cursor()

    cursor.execute(sql, (c_code, c_name, c_continent, c_population, c_gnp))

    conn.commit()

    conn.close()

# add_record('GIN', 'Guinea', 'Africa', '7430000', '2352.00')
# print(get_country_list())