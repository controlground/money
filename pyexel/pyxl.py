def say_hello():
    print('안녕하세요!')
    print('hello')

name = '안녕!'
class Kart:
    # 가속도, 이름, 가격, 코너링
    speed = 10
    name = '골든 스톰블레이드X'
    price = 100000
    cornering = 20
    def start(self):
        print(f'{self.name}님이 나가신다!')
    def __init__(self, kartName):
        self.name = kartName

# golden_storm_blade_x = Kart('골든 스톰블레이드X')
# print(golden_storm_blade_x.cornering)
# golden_storm_blade_x.start()

paragon = Kart('파라곤')
paragon.start()

practice = Kart('연습용 카트')
practice.start()

