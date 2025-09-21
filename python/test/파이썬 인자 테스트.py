"""	
위치 인자: 순서대로 넣기 f(1, 2)
키워드 인자: 이름을 지정해 넣기 f(x=1, y=2)

* 몇 개의 인자를 받을지 모르는 경우
가변 위치 인자: *args
가변 키워드 인자: **kwargs

"""


def add_all(*args):
    # args는 (1, 2, 3) 같은 튜플
    return sum(args)

add_all(1, 2, 3)      # 6
add_all(10, 20, 30)   # 60

