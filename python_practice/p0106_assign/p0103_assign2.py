# 과제2
#    quiz5_2의 마지막 문제(8) 완성  : 파일입출력
#    - 단어 추가 여부
# 위의 퀴즈7에서 단어를 추가할때 입력에 따라 여러개 단어를 추가할 수 있도록 프로그램을 수정하여라.

def addWord():
    print('\n[단어 추가]')
    with open('data\wordResult.txt', 'a', encoding='utf-8') as f:
        while True:
            word = input('두 글자로 구성된 단어를 입력하세요').strip()
            if len(word) == 2:
                f.write(word + '\n')
                print('단어가 입력되었습니다.\n')
                yn = input('단어를 계속 추가하시겠습니다? (y/n)...')
                if yn == 'y':
                    continue
                else:
                    print('단어 추가를 종료합니다.')
                    break
            else:
                print('두글자가 아닙니다.')


def readWord():
    print('\n[단어 모두 출력]')
    with open('data\wordResult.txt', 'r', encoding='utf-8') as f:
        dataList = f.readlines()
        print(f'\n\n추가된 단어는 총 {len(dataList)} 입니다.')
        for i in dataList:
            print(i)
        print('\n')


def clearWord():
    print('\n[파일 내용 모두 삭제]')
    with open('data\wordResult.txt', 'w', encoding='utf-8') as f:
        f.write('')
        print(f'단어 목록을 모두 삭제하였습니다.\n')


print('\n\n** 퀴즈7 **\n')
print('-' * 30)
while True:
    ans = input('메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   ')
    if ans == '1':
        addWord()
    elif ans == '2':
        readWord()
    elif ans == '3':
        clearWord()
    elif ans == '4':
        print('\n\n프로그램을 종료합니다.')
        break
