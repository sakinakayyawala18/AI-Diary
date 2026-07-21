#1 Concept:Classes & Objects
class BankAccount():
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, money):
        self.balance = self.balance + money
        print(f"{money} is Successfully deposit in your account")

    def withdraw(self, money):
        self.balance = self.balance - money
        print(f"{money} is Successfully withdraw in your account")
    
    def check_balance(self):
        print(f"Balance in your account = {self.balance}")

b1 = BankAccount(123, "sakina", 10000000)

b1.check_balance()
b1.deposit(500)
b1.check_balance()

#Q2 Concept:Encapsulation
class Book():
    def __init__(self, title, author, review):
        self.title = title
        self.author = author
        self.review = review
    
    def add_review(self, new_review):
        self.review.append(new_review)
    
    def count_review(self):
        print(f"No of review  = {len(self.review)}")
    
    def display_all_review(self):
        for i in self.review:
            print(i)

b1 = Book("Even after you","sakina",["nice", "good","awesone"])
b1.add_review("romantic book")
b1.count_review()
b1.display_all_review()

#3 Concept:Function Overriding
class Student:

    def __init__(self, name, roll_no, marks):
        self.__name = ""
        self.__roll_no = 0
        self.__marks = 0

        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # Setter for Name
    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Name cannot be empty.")

    # Getter for Name
    def get_name(self):
        return self.__name

    # Setter for Roll Number
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100.")

    # Getter for Roll Number
    def get_roll_no(self):
        return self.__roll_no

    # Setter for Marks
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative.")

    # Getter for Marks
    def get_marks(self):
        return self.__marks


# Driver Code
s1 = Student("Sakina", 25, 90)

print("Name :", s1.get_name())
print("Roll No :", s1.get_roll_no())
print("Marks :", s1.get_marks())

# Updating values
s1.set_marks(95)
s1.set_roll_no(50)
s1.set_name("Ayesha")

print("\nAfter Update")
print("Name :", s1.get_name())
print("Roll No :", s1.get_roll_no())
print("Marks :", s1.get_marks())

#4 Function Overriding
class Shape():
    def area(self):
        print("Area of shape")

class Circle(Shape):
    def __init__(self, radius):
        self.pi = 3.14
        self.radius = radius
    def area(self):
        area = self.pi = 3.14 * (self.radius * self.radius)
        print(f"Area of circle = {area}")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area =  self.length * self.width
        print(f"Area of rectangle = {area}")

class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def area(self):
        area =  (self.base * self.height)/2
        print(f"Area of traniagle = {area}")

s1 = Shape()
c1 = Circle(10)
c1.area()
t1 = Triangle(12, 6)
t1.area()
r1 = Rectangle(2,8)
r1.area()


#5 Concept:Inheritance
class Vehicle():
    def __init__(self, model, brand):
        self.model=model
        self.brand=brand
class Car(Vehicle):
    def __init__(self, model, brand, seats):
        super().__init__(model, brand)
        self.seats = seats
class Bike(Vehicle):
    def __init__(self, model, brand, engine_cc):
        super().__init__(model, brand)
        self.engine_cc = engine_cc

v1 = Vehicle("balenon","tata")
c1 = Car("balenon","tata","4")
b1 = Bike("hero","tata","20000")

#Q6 Concept:Abstraction
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):

    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        print(f"Intern Salary = {self.stipend}")


class FullTimeEmployee(Employee):

    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print(f"Full Time Employee Salary = {self.monthly_salary}")


class ContractEmployee(Employee):

    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        salary = self.hours * self.rate
        print(f"Contract Employee Salary = {salary}")

i1 = Intern(10000)
f1 = FullTimeEmployee(50000)
c1 = ContractEmployee(160, 500)

i1.calculate_salary()
f1.calculate_salary()
c1.calculate_salary()

# Q7 Concept:Constructor Overloading (with Default Parameters
class Person:

    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name :", self.name)

        if self.age is not None:
            print("Age :", self.age)

        if self.address is not None:
            print("Address :", self.address)

        print()

p1 = Person("Sakina")
p2 = Person("Ayesha", 21)
p3 = Person("Ali", 25, "Mumbai")

p1.display()
p2.display()
p3.display()

#8 Concept:Instance & Class Attributes
class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    def display(self):
        print("Name:", self.name)
        print("Level:", self.level)


p1 = Player("Sakina", 10)
p2 = Player("Ayesha", 15)
p3 = Player("Ali", 20)

p1.display()
p2.display()
p3.display()

print("Total Players:", Player.player_count)

#Q9 Concept: Multiple Inheritance
class Herbivore:
    def eat_plants(self):
        print("Eats plants")


class Carnivore:
    def eat_meat(self):
        print("Eats meat")


class Omnivore:
    def eat_both(self):
        print("Eats both plants and meat")


class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal:", self.name)


b1 = Bear("Brown Bear")

b1.display()
b1.eat_plants()
b1.eat_meat()
b1.eat_both()

Q10 ... - i will do this lateral by my self
class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, chatroom, text):
        message = Message(self.name, text)
        chatroom.add_message(message)


class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def display(self):
        print(f"{self.sender}: {self.text}")


class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(f"{user.name} joined {self.room_name}")

    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.name} left {self.room_name}")

    def add_message(self, message):
        self.messages.append(message)

    def view_chat_history(self):
        print("\nChat History:")
        for message in self.messages:
            message.display()


room = ChatRoom("General")
user1 = User("Alice")
user2 = User("Bob")

room.join(user1)
room.join(user2)

user1.send_message(room, "Hello Bob!")
user2.send_message(room, "Hi Alice! How are you?")
user1.send_message(room, "I am fine.")

room.view_chat_history()

room.leave(user2)