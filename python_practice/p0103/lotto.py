import random

def lottoNum(n) :
    lottoList = []
    while True:
        if len(lottoList)>= n:
            break
        else:
            data = random.randint(1,46)
            if data not in lottoList:
                lottoList.append(data)
    print(lottoList)

if __name__ =="__main__":
    print('Main 으로  실행되었음')