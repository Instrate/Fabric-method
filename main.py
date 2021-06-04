class SystemUser(object):
    def __init__(self) -> None:
        super().__init__(self)
        self.data = None

    def enter(self):
        raise NotImplementedError()

    def exit(self):
        raise NotImplementedError()

class Administrator():
    def __init__(self):
        self.data = ""
        self.count = 0

    def enter(self):
        print("\nLogin: ")
        login = input()
        print("\nPassword: ")
        password = input()
        self.data = login + " " + password
        return self

    def exit(self):
        self = None

    def OrderDetails(self, orders):
        print("\nOrder id: ")
        id = int(input())
        print("\nProduct name: ")
        name = input()
        print("\nPrice: ")
        price = float(input())
        print("\nAmount: ")
        amount = float(input())
        print("\nOrdered ")
        print(name)
        print(" ")
        fprice = price*amount
        print(str(fprice))
        orders[id].AddPrice(fprice)
        orders[id].AddChangeLog("Ordered " + str(amount) + " " + name)
        orders[id].CountPrice(id)

    def AddWorkerToOrder(self, orders):
        print("\nOrder id: ")
        id = int(input())
        print("\nWorker full name: ")
        name = input()
        mes = str(name) + " has been added to order #" + str(id)
        print("\n" + mes)
        orders[id].AddChangeLog(mes + "\n")

class Order():
    def __init__ (self):
        self.price = 0
        self.changeList = ""

    def CountPrice(self,id):
        print("\nOrder #" + str(id))
        print(self.changeList)
        print("\nPrice: "+ str(self.price))

    def AddPrice(self, price_):
        self.price += price_

    def AddChangeLog(self, log):
        self.changeList += log

class User(SystemUser):
    def logIn(self, type_):
        if (type_ == "admin"):
            return Administrator()
        elif (type_ == "customer"):
            print("\nWork in progress")
            return SystemUser()

def main():
    orders = []
    orders.append(Order())
    app = User()
    user = app.logIn("admin").enter()
    user.AddWorkerToOrder(orders)
    user.OrderDetails(orders)
    user.exit()
    
if __name__ == "__main__":
    main()