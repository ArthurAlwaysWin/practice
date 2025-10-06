print('hello, how r u')

class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def getinformation(self):
        return f"my name is {self.name} and my age is {self.age}"
    

s1 = Student("Mike", 20)
print(s1.getinformation())
