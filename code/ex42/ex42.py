## Animalはobject(is-a)、objectが何かは後で説明する
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Personはpetをもつ(has-a)
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? この暗号みたいなものは何だろう?
        super().__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## roverはDog(is-a)
rover = Dog("ローバー")

## ??
satan = Cat("サタン")

## ??
mary = Person("メアリー")

## ??
mary.pet = satan

## ??
frank = Employee("フランク", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
