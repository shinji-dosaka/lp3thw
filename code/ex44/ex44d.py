class Parent(object):

    def override(self):
        print("Parent.override()が呼ばれた")

    def implicit(self):
        print("Parent.implicit()が呼ばれた")

    def altered(self):
        print("Parent.altered()が呼ばれた")

class Child(Parent):

    def override(self):
        print("Child.override()が呼ばれた")

    def altered(self):
        print("ChildでParent.altered()の呼び出し前")
        super().altered()
        print("ChildでParent.altered()呼び出し後")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
