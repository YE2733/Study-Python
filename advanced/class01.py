#객체지향
class car:
    number = '54라 9538'
    company = '현대자동차'
    gear_mode = 'Autometic'
    fuel = '휘발유'


    def setPower(self):
        print('시동을 겁니다')
    
    def setPark(self):
        self.setGear('p')
        print('주차를 합니다.')

    # r(후진), n(중립), p(파킹), d(드라이브), s(스포츠)
    def setGear(self, gear:str):
        print(f'{gear}모드로 전환합니다.')

    def accerator(self):    
        print('엑셀을 밟습니다.')

    def pushBreak(self):
        print('브레이크를 밟습니다.')

if __name__ == '__main__':
    mycar = car()
    print(f'제조사는 {mycar.company}입니다.')
    mycar.setPower()
    mycar.setGear('d')
    mycar.accerator()
    mycar.pushBreak
    mycar.setPark()