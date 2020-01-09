# 클래스 구조의 커피 자판기 프로그램
# 속성 :  메뉴, 가격, 이름
# 메소드
# : 메뉴 표시
# : 금액 투입
# : 메뉴 선택과 선택한 메뉴 배달 완료
# : 남은 금액 표시

class Vending_machine():
    def __init__(self, v_name):
        self.v_name = v_name
        self.product = ('아메리카노', '라떼', '마끼아또')
        self.price = (500, 700, 1000)
    # 메뉴 표시
    def show_menu(self, v_name):
        print(f'\n\n\t\t {self.v_name} ')
        # print(f'메뉴1 : {self.product[0]} 가격 {self.price[0]}')
        for i in range(0, len(self.product)):
            print(f'메뉴{i+1} : {self.product[i]} 가격 {self.price[i]}')

    # 금액 투입
    def input_money(self):
        while True:
            self.in_money = input('주문하실 메뉴의 금액을 삽입구에 넣어주세요')
            # 숫자만 입력되는 확인
            if self.in_money.isdigit():
                # 자료형 변경
                self.in_money = int(self.in_money)
                print(f'투입 금액 : {self.in_money}원')
                break
            else:
                print('투입한 금액이 올바르지 않습니다.')

    # : 메뉴 선택과 선택한 메뉴 배달 완료
    def get_drink(self):
        # 메뉴 선택 변수
        sel = input('메뉴를 선택하세요 1.아메리카, 2.라떼, 3. 마끼아또')
        if sel == '1':
            print(f'주문하신 {self.product[0]}가 나왔습니다.')
        elif sel == '2':
            print(f'주문하신 {self.product[1]}가 나왔습니다.')
        elif sel == '3':
            print(f'주문하신 {self.product[2]}가 나왔습니다.')
        else:
            print('선택한 번호의 메뉴가 없습니다. 1~3 입력해주세요')

# vmtest = Vending_machine('역삼점')
# vmtest.show_menu('역삼점')
# vmtest.input_money()
# vmtest.get_drink()

# 메인
vm = Vending_machine('강남점')
while True:
    # 메뉴 표시
    vm.show_menu('강남점')
    # 금액 삽입 메세지
    vm.input_money()
    # 투입금액이 가장 낮은 메뉴의 가격보다 큰지 확인
    if vm.in_money >= int(min(vm.price)):
        print('주문이 가능합니다.')
        # 메뉴 선택과 주문 완료
        vm.get_drink()
        break
    else:
        print('투입 금액이 부족하여 주문이 불가능합니다.')

print('주문이 모두 완료 되었습니다.')

