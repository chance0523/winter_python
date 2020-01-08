# 관련 모듈 임포트
import sqlite3

# DB 연결변수 : 없는 경우에는 새로 생성
conn = sqlite3.connect('data/book2.db')
# 작업변수(cursor 생성)
cursor = conn.cursor()
# 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "book2" (
	    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	    "title" TEXT NOT NULL,
	    "writer" TEXT NOT NULL,
	    "page" INTEGER NOT NULL,
	    "price"	INTEGER NOT NULL
    );
''')

conn.commit()


def print_row():
    print('-' * 30)
    print('\t*** PRINT MODE ***')
    print('-' * 30)
    cursor.execute("SELECT * FROM book2")
    data_list = cursor.fetchall()
    if len(data_list) == 0:
        print('레코드가 없습니다 !!!')
    else:
        for row in data_list:
            print(row)


def insert_row():
    print('-' * 30)
    print('\t*** INSERT MODE ***')
    print('-' * 30)
    title = input('책 제목 : ')
    writer = input('출판사 : ')
    page = input('페이지 수 : ')
    price = input('가격 : ')

    insert = '''INSERT INTO book2 (title, writer, page, price)
                VALUES (?,?,?,?)'''
    cursor.execute(insert, (title, writer, page, price))
    conn.commit()
    print(f'책 제목 : {title}\n출판사 : {writer}\n페이지 수 : {page}\n가격 : {price}')
    print(f'데이터가 추가되었습니다!!!')


def delete_row():
    print('-' * 30)
    print('\t*** DELETE MODE ***')
    print('-' * 30)
    # 레코드 모두 출력하기
    cursor.execute("SELECT * FROM book2")
    data_list = cursor.fetchall()
    if len(data_list) == 0:
        print('레코드가 없습니다 !!!')
    else:
        print('현재 레코드 목록')
        for row in data_list:
            print(row)
    # 입력문으로 삭제할 레코드 번호 받기
    del_num = int(input('삭제할 레코드 번호를 입력하세요 : '))
    # SQL 명령 실행하기
    delete = '''DELETE FROM book2 WHERE id = ?'''
    cursor.execute(delete, [del_num])
    # 레코드 정상 삭제 메세지
    conn.commit()
    print('레코드가 정상적으로 삭제 되었습니다 !!!')


def print_selected_data(select, up_num, data_info):
    select = "SELECT * FROM book2 WHERE id = ?"
    cursor.execute(select, [up_num])
    data_info = cursor.fetchone()
    print(data_info)
    pass


def update_row():
    print('-' * 30)
    print('\t*** UPDATE MODE ***')
    print('-' * 30)
    # 레코드 모두 출력하기
    cursor.execute("SELECT * FROM book2")
    data_list = cursor.fetchall()
    if len(data_list) == 0:
        print('레코드가 없습니다 !!!')
    else:
        print('현재 레코드 목록')
        for row in data_list:
            print(row)
    # 입력문으로 수정할 레코드 번호 받기
    up_num = int(input('수정할 레코드 번호를 입력하세요 : '))
    # 선택한 레코드 번호에 대한 데이터 출력
    select = "SELECT * FROM book2 WHERE id = ?"
    cursor.execute(select, [up_num])
    data_info = cursor.fetchone()
    print('-' * 50)
    print('수정할 레코드 :', data_info)
    print('-' * 50)
    # 입력문으로 수정할 필드 번호 받기
    sel_field = input('수정할 필드를 선택하세요. (title, writer, page, price) ')
    # SQL 명령 실행하기
    if sel_field == 'title':
        update = '''UPDATE book2 SET title = ? WHERE id = ?'''
        cursor.execute(update, (input('변경할 title을 입력하세요 : '), up_num))
        conn.commit()
        print('수정이 완료되었습니다 !!!')
        print_selected_data(select, up_num, data_info)
    elif sel_field == 'writer':
        update = '''UPDATE book2 SET writer = ? WHERE id = ?'''
        cursor.execute(update, (input('변경할 writer를 입력하세요 : '), up_num))
        conn.commit()
        print('수정이 완료되었습니다 !!!')
        print_selected_data(select, up_num, data_info)

    elif sel_field == 'page':
        update = '''UPDATE book2 SET page = ? WHERE id = ?'''
        cursor.execute(update, (int(input('변경할 page를 입력하세요 : ')), up_num))
        conn.commit()
        print('수정이 완료되었습니다 !!!')
        print_selected_data(select, up_num, data_info)

    elif sel_field == 'price':
        update = '''UPDATE book2 SET price = ? WHERE id = ?'''
        cursor.execute(update, (int(input('변경할 price를 입력하세요 : ')), up_num))
        conn.commit()
        print('수정이 완료되었습니다 !!!')
        print_selected_data(select, up_num, data_info)

    else:
        print('title, writer, page, price 중에서 입력하세요 !!!')
    # 레코드 정상 수정 메세지


while True:
    choice = input('''메뉴 선택\n(1. print all 2. insert 3. delete 4. update 5. quit) ... ''')
    if choice == '1':
        print_row()
    elif choice == '2':
        insert_row()
    elif choice == '3':
        delete_row()
    elif choice == '4':
        update_row()
    elif choice == '5':
        print('종료합니다 !!!')
        break
    else:
        print('1 ~ 5의 숫자만 입력하세요')

# DB 종료
conn.close()
