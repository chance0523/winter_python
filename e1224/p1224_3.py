# indexing & slicing
sen = "Life is too short"
print('sen[3] = ', sen[3])
print('sen[:3] = ', sen[:3])
print('sen[-1] = ', sen[-1])
print('sen[::] = ', sen[::])
print('sen[::2] = ', sen[::2])
print('sen[2::2] = ', sen[2::2])
print('sen[2:11:2] = ', sen[2:11:2])
print('sen[-1:] = ', sen[-1:])
print('sen[-5:-1] = ', sen[-5:-1])

print('len(sen) = ', len(sen))
print('len(sen[:3]) = ', len(sen[:3]))
print('len(sen[-1]) = ', len(sen[-1]))

print('sen[:4], sen[-5:] = ', sen[:4], sen[-5:])

# formatting
# %를 이용한 formatting
# format()를 이용한 formatting
# f'를 이용한 formatting. python version 3.6 ++
today = '화요일'
yesterday = '수요일'
# 오늘은 화요일입니다.
print('오늘은', today, '입니다.')
print('오늘은 %s입니다.' % today)
