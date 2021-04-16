from classes.cargo.cargo import Cargo
from classes.my_classes import SpaceShip


class HugeSpaceShip(SpaceShip):
    def flyAway(self):
        print("Wrom wrom flap flap")

ship = HugeSpaceShip("Mike", 22, "Pluto", Cargo("Food", 200))
print(ship)
ship.flyAway()