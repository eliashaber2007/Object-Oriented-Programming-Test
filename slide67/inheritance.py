# Problem 1
class Vehicle:
    def drive(self):
        return "Driving a vehicle"


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"


# Problem 2
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return f"Hi, I'm {self.name}, I'm {self.age} and I live in {self.address}."


class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        super().__init__(name, age, address)
        self.field_of_study = field_of_study

    def introduce(self):
        return f"Hi, I'm {self.name}, I'm {self.age} and I study {self.field_of_study}."


class Employee(Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return f"Hi, I'm {self.name}, I'm {self.age} and I work at {self.company}."


# Problem 3
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def transfer(self, destination, amount):
        if amount > self.balance:
            return False
        self.withdraw(amount)
        destination.deposit(amount)
        return True


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    for vehicle in [Vehicle(), Car(), Bicycle()]:
        print(vehicle.drive())

    people = [
        Person("Elias", 18, "Paris"),
        Student("Elias", 18, "Paris", "AI and Data Science"),
        Employee("Sara", 25, "Lyon", "Airbus"),
    ]
    for person in people:
        print(person.introduce())

    checking = BankAccount("FR001", 500)
    savings = SavingsAccount("FR002", 1000, interest_rate=0.03)
    savings.add_interest()
    print("Savings after interest:", savings.check_balance())
    print("Transfer 200 ok:", checking.transfer(savings, 200))
    print("Transfer 1000 ok:", checking.transfer(savings, 1000))
    print("Checking:", checking.balance, "| Savings:", savings.check_balance())
