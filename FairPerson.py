from random import randint

from Person import Person


class FairPerson(Person):
    def jump(self, contest) -> float:
        contest.addPerson(self)
        return randint(400, 895) / 100

    def __init__(self, firstName: str, lastName: str):
        super().__init__(firstName, lastName)
