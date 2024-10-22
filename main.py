from Contest import Contest
from DopedPerson import DopedPerson
from FairPerson import FairPerson
from Stadium import Stadium

myStadium = Stadium("Parc des princes")
print(myStadium.Name)
print(myStadium.Contests)

myLeague1 = Contest("01/02/2024", myStadium)
print(myLeague1.Date, myLeague1.Stadium.Name)
print(myStadium.Contests)

myCompetition: Contest("02/03/2000", myStadium)
print(myStadium.Contests)

ted = FairPerson("Thomas", "Legrand")
tod = DopedPerson("Louis", "Francis")

print(ted.jump(myLeague1))
print(tod.jump(myLeague1))

print(myLeague1.Persons)
