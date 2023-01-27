class Animal(object):
    pass
##Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ##class dog has a init with self and name parameters
        self.name = name

##cat is-a animal
class Cat(Animal):
    def __init__(self,name):
        ##class cat has-a init with self and name par
        self.name = name

##class person is-a object
class Person(object):
    def __init__(self, name):
        ##class person has-a init that takes self and name para
        self.name = name
        ##person has a pet of some kind
        self.pet = None

##class employee is a person
class Employee(Person):
    def __init__(self, name, salary):
        ##class employee has-a init that  takes self, name and salary par
        super(Employee, self).__init__(name) ##what??
        ##from self, get the salary attribute and set it to salary
        self.salary = salary

class fish(object):
    pass

class salmon(fish):
    pass

class Halibut(fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 12000)

frank.pet = rover

flipper = fish()

crouse = salmon()

harry = Halibut()
