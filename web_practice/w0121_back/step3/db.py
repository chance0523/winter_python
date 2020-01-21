import pymysql


def get_connect():
    conn = pymysql.connect(
        host='127.0.0.1', user='root', password='1234', db='employees', charset='utf8')
    if conn:
        # print('연결 완료 !!!')
        pass
    return conn


def get_emp_list():
    conn = get_connect()

    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM employeesTbl;
    ''')

    result_list = cursor.fetchall()

    dict_list = []
    for row in result_list:
        temp_dict = {}
        temp_dict['emp_no'] = row[0]
        temp_dict['first_name'] = row[1]
        temp_dict['last_name'] = row[2]
        temp_dict['gender'] = row[3]
        dict_list.append(temp_dict)

    conn.close()
    return dict_list

# 테이블의 전체 레코드 수를 반환


def get_total_count():
    conn = get_connect()

    cursor = conn.cursor()

    cursor.execute('''
    SELECT COUNT(*) FROM employeesTbl;
    ''')

    total_count = cursor.fetchone()

    conn.close()
    return total_count[0]


def get_page_list(n, m):  # n = start index, m = amount
    conn = get_connect()

    cursor = conn.cursor()

    sql = ''' 
    SELECT * FROM employeesTbl 
    LIMIT %s,%s;
    '''
    # ORDER BY emp_no DESC 

    cursor.execute(sql, (n, m))

    result_list = cursor.fetchall()

    dict_list = []
    for row in result_list:
        temp_dict = {}
        temp_dict['emp_no'] = row[0]
        temp_dict['first_name'] = row[1]
        temp_dict['last_name'] = row[2]
        temp_dict['gender'] = row[3]
        dict_list.append(temp_dict)

    conn.close()
    return dict_list


# 전체 페이지 수 산출하기 : (전체 레코드 수/페이지 당 레코드 수) + 1
print('총 레코드 수 :', get_total_count())
totRecord = get_total_count()
totPage = int((totRecord/5))+1
print('전체 페이지 수 :',totPage)
