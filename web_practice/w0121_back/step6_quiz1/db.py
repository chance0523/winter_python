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

def join(userId,password,email):
    # db 연결
    conn=get_connect()
    
    sql='''
    INSERT INTO memberTbl (userId, password, email)
    VALUES (%s, %s, %s);
    '''

    cursor=conn.cursor()

    cursor.execute(sql, (userId, password, email))

    conn.commit()

    conn.close()

def view(userId):
    sql = ''' SELECT * FROM memberTbl
                WHERE userId=%s; '''
    # db 연결
    conn = get_connect()
    # 작업변수 생성
    cursor = conn.cursor()
    # sql 명령 실행함수
    cursor.execute(sql, (userId))
    result_data = cursor.fetchone()
    # db 종료
    conn.close()
    return result_data

def update_record(password, email, userId):
    # 레코드 수정 sql 명령문
    sql = ''' UPDATE memberTbl
                SET  password = %s ,
                     email =  %s,
                WHERE userId = %s; '''
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute(sql, (password, email, userId))
    conn.commit()
    conn.close()
