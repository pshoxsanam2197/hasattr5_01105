 class Simple:
    def info_jon(self):
        print(f"Simple info")

class MyClass:
    def __init__(self,x, y):
        self.__x = x
        self.__y = y

    def method_1(self, obj):
        if hasattr(obj, "info"):
            obj.info()
        else:
            print("Bu method da info method yo'q")

obj = MyClass(40, 30)

s = Simple()
obj.method_1(s)

class Person:
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age

    def show_info(self):
        print(f"Ism: {self.fullname}")
        print(f"Yosh: {self.age}")


class Simple:
    def test(self):
        print("Oddiy method")
#
