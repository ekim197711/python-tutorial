
class Cargo:
    def __init__(self, kind, qty):
        self.kind = kind
        self.quantity = qty

    def __str__(self):
        return "Kind: " + str(self.kind) + ", qty: " + str(self.quantity)

def showStuff():
    print("Hello 1 2 3")

if __name__ == "__main__":
    c = Cargo("Modules", 1)
    print(c)
    print("The module is done")