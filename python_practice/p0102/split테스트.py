# 문자열의 리스트화 (3.8 버전)
message = '4673rksk'
sampleList = message.split()
print(sampleList, len(sampleList))
# ['4673rksk'] 1

def digitPrint(c):
    return c.isdigit()

print(list(filter(digitPrint, message)))
# ['4', '6', '7', '3']