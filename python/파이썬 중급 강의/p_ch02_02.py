# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

class Car():
    """
    Car Class
    Author : Lee
    Date : 2025.10.07
    """

    ''' 참고
    클래스 변수 : 모든 인스턴스가 공유하는 변수
    '''
    car_count = 0


    def __init__(self, company, details):
        ''' 참고
        생성자 : 인스턴스가 생성될 때 자동으로 호출되는 메서드
        인스턴스 변수 초기화 담당 (초기화 메서드에서 self가 붙어있는 변수들을 인스턴스 변수라고 함)
        인스턴스 변수 : 인스턴스마다 별도로 존재하는 변수

        
        -! "인스턴스 변수 이름 앞에 _를 붙이는 것이 관례" 강의에서는 이렇게 언급하는데
        _는 단순히 private(비공개)를 의미하는 것 아닌가?
        인스턴스 변수는 private으로 선언해서 getter, setter 메서드를 통해 접근하는 것이 좋다는 의미인가??
        '''
        self._company = company
        self._details = details
        # self.car_count = 10 # 동일한 이름의 인스턴스 변수와 클래스 변수를 설정하면 어떻게 될까??
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
    def __del__(self):
        print("del 메서드 호출!~!")
        Car.car_count -= 1
    
    def testmethod(self):
        print('testmethod called!')

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

'''
참조변수 self

self는 "나 자신(객체 자신)"을 가리키는 참조변수
id(self)를 출력해보면 self가 가리키는 객체의 메모리 주소를 확인할 수 있음

'''

car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})


# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

'''
비교 연산자 == vs is

==는 대상끼리의 값을 비교하는 연산자. 즉, 값이 같으면 True, 다르면 False를 반환
is는 대상끼리의 실제 메모리 주소를 비교하는 연산자. 즉, 동일한 객체를 참조하면 True, 그렇지 않으면 False를 반환
'''
print(car1._company == car2._company)
print(car1 is car2)


# dir() - 객체가 가진 모든 속성과 메서드의 이름 목록을 보여주는 함수
print(dir(car1))
print(dir(car2))

print()
print()

# __dict__ - 객체의 namespace를 딕셔너리로 보여주는 속성
'''
namespace는 "변수/함수 이름이 저장되는 공간"
쉽게 말해 "이름과 값을 매핑해놓은 저장소"

- 클래스.__dict__ : 클래스 namespace (메서드, 클래스 변수)
- 인스턴스.__dict__ : 인스턴스 namespace (인스턴스 변수만)
'''
print("=== 클래스 namespace ===")
print(Car.__dict__)

print("\n=== car1 인스턴스 namespace ===")
print(car1.__dict__)

print("\n=== car2 인스턴스 namespace ===")
print(car2.__dict__)


# Docstring
# 클래스, 함수, 모듈의 설명을 담은 문자열 (문서화)
print(Car.__doc__)
print()



# 인스턴스의 클래스 정보
# __class__ : 인스턴스가 어떤 클래스로부터 생성되었는지
print(car1.__class__, car2.__class__)


'''
클래스 id, 인스턴스 id

클래스와 인스턴스는 메모리에서 "별개의 객체"로 존재
따라서 id 값도 서로 다름
'''
# id값을 비교해보면 값이 동일함
# 클래스의 id 값을 비교했기 때문
print(id(car1.__class__), id(car2.__class__))

# 인스턴스의 id 값은 서로 다름
print(id(car1))
print(id(car2))


# 메서드 호출

# 인스턴스로 메서드 호출 => 인자에 self가 필요없음. 자동으로 self를 넘겨줌
car1.detail_info()
car2.detail_info()
print()

# 클래스로 메서드 호출
# Car.detail_info() => error. "Car.detail_info() missing 1 required positional argument: 'self'"
# 인스턴스 없이 호출 불가. 즉, 클래스 변수는 인스턴스를 통해서만 접근 가능

# 이건 가능. 인자로 인스턴스를 넘겨주기 때문.
Car.detail_info(car1)
Car.detail_info(car2)


# 클래스 변수
# car1,2,3인스턴스를 이미 초기화 한 상태에서 car_count를 출력한 결과 모두 같은 값을 가짐
# 즉, 클래스 변수는 모든 인스턴스가 공유하는 변수인 것
print(car1.car_count)
print(car2.car_count)
print(car3.car_count)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 클래스 변수까지 확인하려면 dir() 함수 사용
print(dir(car1))
print()

# 클래스 변수 접근
print(Car.car_count) # 정석
print(car1.car_count)

# del 실험
del car2

# ! 동일한 이름의 인스턴스 변수와 클래스 변수를 설정하면 어떻게 될까??
# 인스턴스 네임스페이스애 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
print(Car.car_count)
print(car1.car_count)

# 마지막에 del 메서드 로그가 두 번출력되는 이유는 프로그램 종료 시 모든 객체가 자동으로 삭제