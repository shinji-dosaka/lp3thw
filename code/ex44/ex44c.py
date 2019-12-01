class Parent(object):

    def altered(self):
        print("Parent.altered()が呼ばれた")

class Child(Parent):

    def altered(self):
        print("ChildでParent.altered()の呼び出し前")
        super().altered()
        print("ChildでParent.altered()の呼び出し後")

dad = Parent()
son = Child()

dad.altered()
son.altered()
