class Student:
    nazwa_ucznia: str
    klasa_ucznia: str
    student_id: str

    def __init__(self, nazwa_ucznia: str, klasa_ucznia: str, student_id: str):
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id

    def student_data(self) -> None:
        