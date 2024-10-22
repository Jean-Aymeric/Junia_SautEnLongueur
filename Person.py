from abc import ABC, abstractmethod


class Person(ABC):
    __firstName: str
    __lastName: str

    def __init__(self, firstName: str, lastName: str):
        self.__firstName = firstName
        self.__lastName = lastName

    @property
    def FirstName(self) -> str:
        return self.__firstName

    @property
    def LastName(self) -> str:
        return self.__lastName

    @abstractmethod
    def jump(self, contest) -> float:
        pass

    def __repr__(self):
        return self.__firstName + " " + self.__lastName
