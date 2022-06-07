class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f' Nome {self.name}, e idade e {self.age}'


dog1 = Pet('Max', '1,5')

print(dog1.show())