# 사람객체를 위한 클래스 Person
from weakref import WeakValueDictionary


class Person:
    __name = ''  #이름속성
    age = 0   # 나이속성
    height = 100  # 키
    weight = 30  # 몸무게

    # 생성자 재정의
    def __init__(self, name = None) -> None:
        if name == None:
            self.__name = '홍길동'
        else:
            self.__name = name

        print(f'{self.__name}탄생!!')

    # #매직매서드 __str__사용 재정의
    def __str__(self) -> str:
        value = f'''객체 : {self.__name}
나이 : {self.age}
  키 : {self.height}'''
        return value
        

    def walk(self, speed):
        print(f'{self.__name}이(가) {speed}km/h로 걷는다.')
        return

    def run(self, speed):
        print(f'{self.__name}이(가) {speed}km/h로 뛴다.')
        return




p = Person('전아영')  #객체 생성
# p.__name = '전아영'
p.age = 25
p.height = 165
p.weight = 65

p.walk(2)
p.run(10)

# print(type.(p))
print(p)

