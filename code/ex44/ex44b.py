class Parent(object):

    def override(self):
        print("Parent.override()が呼ばれた")

class Child(Parent):

    def override(self):
        print("Child.override()が呼ばれた")

dad = Parent()
son = Child()

dad.override()
son.override()
