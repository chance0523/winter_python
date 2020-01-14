import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306, user='root', passwd='1234',
                       db='sqldb2', charset='utf8')
print('연결완료')

cursor = conn.cursor()


# 힘수정의
def showBook():
    cursor.execute(
        'SELECT * FROM bookTbl'
    )
    result = cursor.fetchall()
    print('-' * 30)
    print('\t\tBOOK LIST')
    print('-' * 30)
    for row in result:
        print(row)
    print('-' * 30)


def insertBook():
    print('-' * 30)
    print('\t\tINSERT BOOK DATA')
    print('-' * 30)
    sql = '''
          INSERT INTO bookTbl (title, writer, page, price)
          VALUES(%s, %s, %s, %s);
          '''
    cursor.execute(sql, (input('책 제목 : '), input('출판사 이름 : '), int(input('페이지 수 : ')), int(input('가격 : '))))
    conn.commit()


def insertBook2():
    print('-' * 30)
    print('\t\tINSERT BOOK DATA')
    print('-' * 30)
    title = input('책 제목 : ')
    writer = input('출판사 이름 : ')
    page = int(input('페이지 수 : '))
    price = int(input('가격 : '))
    sql = '''
          INSERT INTO bookTbl (title, writer, page, price)
          VALUES(%s, %s, %s, %s);
          '''
    cursor.execute(sql, (title, writer, page, price))
    conn.commit()


def updateBook():
    uID = int(input('수정하려는 책의 번호를 입력하세요. '))
    uCol = input('수정하고 싶은 컬럼을 선택하세요. (title, writer, page, price) : ')
    if uCol == 'title':
        print('title을 선택하셨습니다.')
        uVal = input('책 제목을 입력하세요. ')
        sql = '''
                  UPDATE bookTbl
                  SET title = %s
                  WHERE id = %s;
                  '''
        cursor.execute(sql, (uVal, uID))
    elif uCol == 'writer':
        print('writer을 선택하셨습니다.')
        uVal = input('출판사를 입력하세요. ')
        sql = '''
                    UPDATE bookTbl
                    SET writer = %s
                    WHERE id = %s;
                    '''
        cursor.execute(sql, (uVal, uID))
    elif uCol == 'page':
        print('page를 선택하셨습니다.')
        uVal = int(input('페이지 수를 입력하세요. '))
        sql = '''
                    UPDATE bookTbl
                    SET page = %s
                    WHERE id = %s;
                    '''
        cursor.execute(sql, (uVal, uID))
    elif uCol == 'price':
        print('price를 선택하셨습니다.')
        uVal = int(input('가격을 입력하세요. '))
        sql = '''
                    UPDATE bookTbl
                    SET price = %s
                    WHERE id = %s;
                    '''
        cursor.execute(sql, (uVal, uID))
    else:
        print('title, writer, page, price 중 하나만 입력하세요.')

    conn.commit()
    print('수정이 완료되었습니다.')


def deleteBook():
    print('-' * 30)
    print('\t\tDELETE BOOK DATA')
    print('-' * 30)
    dID = int(input('삭제하려는 책의 번호를 입력하세요. '))
    sql = '''
    DELETE FROM bookTbl WHERE id = %s;
    '''
    cursor.execute(sql, dID)
    conn.commit()
    print('삭제가 완료되었습니다.')


def end():
    print('프로그램을 종료합니다 ...')


# 메인
while True:
    choice = int(input('1. 목록보기 2. 추가 3. 수정 4. 삭제 0. 종료 '))
    if choice == 1:
        showBook()
    elif choice == 2:
        insertBook()
    elif choice == 3:
        updateBook()
    elif choice == 4:
        deleteBook()
    elif choice == 0:
        end()
        break

conn.close()
