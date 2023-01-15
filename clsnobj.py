class Myobj:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        return "My name is "+self.name

p1 = Myobj('Akshay',30)
print('Name : ', p1.name)
print('Age : ', p1.age)

print(p1.myfunc())
