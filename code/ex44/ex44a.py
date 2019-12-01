class Parent(object):

    def implicit(self):
        print("Parent.implicit()が呼ばれた")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
