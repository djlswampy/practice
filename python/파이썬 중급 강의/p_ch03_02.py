# Chapter03-02
# 파이썬 심화
# Special Method(Magic Method)
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 클래스 예제2
# class Vector(object):의 object는 **부모 클래스(상속받을 클래스)를 의미. 안 써도 됨
class Vector(object):
    def __init__(self, *args):
        # args로 패킹해서 넘겨주고 언패킹한다??
        '''Create a vector, example : v = Vector(5,10)'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Returns the vector infomations'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Returns the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))

print()
print()


# 참고 : 파이썬 바이트 코드 실행
import dis
dis.dis(v2.__add__)