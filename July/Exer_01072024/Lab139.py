


class A:
    def method(self):
        return "Method A"

    def a1_method(self):
        return "Method A1"


class B:
    def method(self):
        return "Method B"

    def b1_method(self):
        return "Method B1"


class C(A, B):
    def method(self):
        return "Method C"

    def c1_method(self):
        return "Method C1"


object_c = C()
print(object_c.method())
print(object_c.c1_method())
print(object_c.b1_method())
print(object_c.a1_method())

