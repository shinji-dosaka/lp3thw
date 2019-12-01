class Other(object):

    def override(self):
        print("Other.override()が呼ばれた")

    def implicit(self):
        print("Other.implicit()が呼ばれた")

    def altered(self):
        print("Other.altered()が呼ばれた")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Child.override()が呼ばれた")

    def altered(self):
        print("ChildでOther.altered()の呼び出し前")
        self.other.altered()
        print("ChildでOther.altered()の呼び出し後")

son = Child()

son.implicit()
son.override()
son.altered()
