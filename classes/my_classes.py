from classes.cargo.cargo import Cargo, showStuff


class SpaceShip:
    messageToAllInstances = "Have a nice day"

    def __init__(self, captain, fuelpercentage, destination, cargo):
        self.captain = captain
        self.fuelpercentage = fuelpercentage
        self.destination = destination
        self.cargo = cargo

    def __str__(self):
        return "Captain is " + str(self.captain) + \
               ", Fuelpercentage is " + str(self.fuelpercentage) + \
               ", Destination is " + str(self.destination) + \
               ", Cargo is " + str(self.cargo)

    def refuel(self):
        print("Refuelling... Adding 5 perc")
        self.fuelpercentage += 5


ship1 = SpaceShip("Mike", 88, "Mars", Cargo("Iron", 4))
ship2 = SpaceShip("Susan", 78, "Venus", Cargo("Popcorn", 100))
SpaceShip.messageToAllInstances = "Watch out for meteors"

ship1.refuel()
ship2.captain = "Anna"
print(ship2.messageToAllInstances)

print(ship1)
print(ship2)
showStuff()