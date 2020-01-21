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

def delete_record(c_code):
    conn=get_connect()

    sql='''
    DELETE FROM countryTb WHERE code=%s;
    '''

    cursor=conn.cursor()

    cursor.execute(sql,c_code)

    conn.commit()

    conn.close()

# 특정 레코드  검색 함수
def view_record(c_code):
    # 레코드 출력 sql 명령문
    sql = ''' SELECT * FROM countryTb
                WHERE code=%s; '''
    # db 연결
    conn = get_connect()
    # 작업변수 생성
    cursor = conn.cursor()
    # sql 명령 실행함수
    cursor.execute(sql, (c_code))
    result_record = cursor.fetchone()
    # db 종료
    conn.close()
    return result_record


# print(get_country_list())
# print(view_record('ALB'))



# 레코드 수정 함수
def update_record(c_name, c_continent, c_population, c_gnp, c_code):
    # 레코드 수정 sql 명령문
    sql = ''' UPDATE countryTb
                SET  Name = %s ,
                     Continent =  %s,
                     Population =  %s,
                     GNP =  %s
                WHERE Code = %s; '''
    # db 연결
    conn = get_connect()
    # 작업변수 생성
    cursor = conn.cursor()
    # sql 명령 실행함수
    cursor.execute(sql, (c_name, c_continent, c_population, c_gnp, c_code))
    # db 반영
    conn.commit()
    # db 종료
    conn.close()

print(view_record('COM'))

# 수정함수 호출
# Continent 값은 아래중 하나로 넣어야함
# 'Asia','Europe','North America',
# 'Africa','Oceania','Antarctica','South America'
# update_record('new', 'South America', '0', '0', 'COM')
# print(view_record('COM'))
# add_record('GIN', 'Guinea', 'Africa', '7430000', '2352.00')
# print(get_country_list())
# delete_record('GIN')