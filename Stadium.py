class Stadium:
    __name: str
    __contests: []

    def __init__(self, name: str):
        self.__name = name
        self.__contests = []

    @property
    def Name(self) -> str:
        return self.__name

    def addStadium(self, contest):
        self.__contests.append(contest)

    @property
    def Contests(self) -> []:
        return self.__contests
