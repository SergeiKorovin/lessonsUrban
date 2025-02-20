import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 5

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def ger_cord(self):
        cords = self._cords
        return cords


    def move(self, dx, dy, dz):
        list_cord = [dx, dy, dz]
        for i in range(len(self._cords)):
            if list_cord[i] >=0:
                self._cords[i] = list_cord[i] * self.speed
            else:
                print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')


    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0" )


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * (self.speed / 2)



class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8



class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = 'Click-click-click'

    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()