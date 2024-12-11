class MyClass :
    x = 5

demoObj = MyClass()
print(demoObj.x)

class Person:
    def __init__(self, name, age):
     self.name = name 
     self.age = age

    def __str__(self):
     return f"{self.name}({self.age})"
    
    def myFunc(self):
       print("Hello my name is " + self.name)

p1 = Person("John" , 36)

print(p1.name)
print(p1.age)
print(p1)
p1.myFunc()

# del p1.age
# print(p1.age)

# del p1


# class Person:
#    pass

#inheritance

class Student(Person):
   pass

y = Student("Mike" , 50)
print(y.name)
print(y.age)

class Student(Person):
   def __init__(self, name , age , year):
      super().__init__(name, age)
      self.graduationYear = year

   def welcome(self):
      print("Welcome",self.name, "of age" ,self.age, "in year", self.graduationYear)   

z = Student("Peter" , 20 , 1940)
print(z.graduationYear)
z.welcome()

# command to run
# cd basics
# python3 python_class.py



