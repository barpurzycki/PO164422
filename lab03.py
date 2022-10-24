class Osoba:
    imie:str = ""
    nazwisko: str = ""

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

====

from classes import Osoba

os1 = Osoba("Bartosz", "Purzycki")
print(os1.imie)
print(os1.nazwisko)

====

import random
class Coin:
    def __init__(self)->None:
        strona=random.randint(0, 1)
        if(strona == 0):
            self.side:str="Orzeł"
        else:
            self.side:str="Reszka"

    def throw(self)->None:
        strona = random.randint(0, 1)
        if(strona == 0):
            self.side:str="Orzeł"
        else:
            self.side:str="Reszka"

    def show_side(self)->str:
        return self.side
      
====

from classes import Coin
c1 = Coin()
print(c1.show_side())
c1.throw()
print(c1.show_side())
