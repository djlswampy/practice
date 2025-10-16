t = '안녕하세요!'

# for c in t:
#     print(c)


# while
w = iter(t) # iterable 객체(문자열)를 iterator 객체로 변환

while True:
    try:
        print(next(w)) # next()는 이터레이터에서 다음 값을 가져오는 함수
    except StopIteration:
        break

