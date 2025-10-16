# Chapter03-01
# 파이썬 심화
# Special Method(Magic Method) - 클래스안에 정의할 수 있는 특별한(Built-in) 메소드
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 기본형 - 모두 클래스
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))
print()
print()

n = 10

# 사용
print(n + 100)
print(n.__add__(100))
print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price)

    # Greater than or Equal (크거나 같다)
    def __ge__(self, x):
        print('Called >> __ge__ Method.')
        if self._price >= x._price:
            return True
        else:
            return False

    # Less than or Equal (작거나 같다)
    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._price <= x._price:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called >> __sub__ Method.')
        return self._price - x._price
    
    # 두 과일의 가격을 더하는 매직메소드
    # 근데 이렇게 하면 세 개 이상 더하지 못함
    def __add__(self, x):
        print('Called >> __add__ Method.')
        return self._price + x._price  
    
    # 만약 마트에서 과일 합계에서 10% 할인 행사를 한다면?
    # def __add__(self, x):
    #     print('Called >> __add__ Method.')
    #     return (self._price + x._price) * 0.9  # 10% 할인

    # 이런 식으로 내가 정해놓은 수식을 토대로 손쉽게 계산하도록 코드를 작성할 수 있음
    # 중급자 이상이 되기 위해서는 필수

    # # 두 개 이상의 과일 객체를 더하기 위해 int가 아닌 Fruit 객체를 반환하도록 수정
    # def __add__(self, x):
    #     print('Called >> __add__ Method.')
    #     # Fruit 객체를 반환
    #     return Fruit(
    #         f"{self._name}+{x._name}", 
    #         self._price + x._price
    #     )
    
# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)
s3 = Fruit('Mango', 10000)

# 두 과일의 가격을 더한다면
# 일반적인 계산
print(s1._price + s2._price)

# 위 방법은 좋은 코드가 아니라 함.
# private 속성에 직접 접근하기 때문인가?

# 매직메소드를 활용하는 것이 좋다고 언급
print(s1 + s2)
print()

# print(s1 + s2 + s3)

# 매직메소드 출력
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)
