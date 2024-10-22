from Person import Person
from Stadium import Stadium


class Contest:
    __date: str
    __stadium: Stadium
    __persons: [Person]

    def __init__(self, date: str, stadium: Stadium):
        self.__date = date
        self.__stadium = stadium
        self.__stadium.addStadium(self)
        self.__persons = []

    @property
    def Date(self) -> str:
        return self.__date

    @property
    def Stadium(self) -> Stadium:
        return self.__stadium

    def __repr__(self):
        return self.__date + " " + self.__stadium.Name

    def addPerson(self, person: Person):
        self.__persons.append(person)

    @property
    def Persons(self) -> list:
        return self.__persons
