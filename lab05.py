class Point(object):
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'<{self.x}, {self.y}>'

    def move(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y

    @staticmethod
    def distance(x, y):
        return abs(x - y)
      
==========================================

from classes import Point
from namedpoint import NamedPoint
from adresclass import Adres

def main():
    a: Point = Point(5, 9)
    print(f'Utworzony punkt: {a}')
    a.move(-2, 6)
    print(f'Przesuniety punkt: {a}')
    print(f'Wspolrzedna x: {a.x}, wspolrzedna y: {a.y}')
    print(a.__dict__)
    print(a.distance(a.x, a.y))

    b = Point(10, 12)
    b1 = NamedPoint(5, 15, "punkt")
    print(b.distance(b.x, b.y))
    print(b1.distance(b1.x, b1.y))

    adres = Adres(10, "Kowalskiego", "Warszawa", "10-001")
    adres.show()
    adres1 = Adres(12, "Wokalskiego", "Kraków", "40-201", 95)
    adres1.show()

if __name__ == "__main__":
    main()
    
==========================================

class Adres:

    def __init__(self, nrdomu: int, ulica: str, miasto: str, kod: int, nrmieszkania = ' ' ):
        self.nrdomu = nrdomu
        self.ulica = ulica
        self.miasto = miasto
        self.kod = kod
        self.nrmieszkania = nrmieszkania

    def show(self):
        print(f'Adres: {self.ulica} {self.nrdomu}, {self.nrmieszkania} \nMiasto: {self.miasto} Kod pocztowy: {self.kod}')
        
==========================================
        
from classes import Point


class NamedPoint(Point):

    nazwa: str

    def __init__(self, x: float, y: float, nazwa: str) -> None:
        # Point.__init__(self, x, y)
        super().__init__(x, y)
        self.nazwa = nazwa

    def __str__(self) -> str:
        return f'{self.nazwa}: ({self.x}, {self.y})'

    def __del__(self) -> None:
        self.nazwa = ""
