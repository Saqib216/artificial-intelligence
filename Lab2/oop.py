class Student:
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept
    def details(self):
        print(f'I am {self.name}. My age is {self.age} My dept is {self.dept}')

s1 = Student('Saqib', 19, 'CS')
s2 = Student('Adeel', 21, 'IT')
s3 = Student('Husnain', 21, 'CS')

s1.details()
s2.details()
s3.details()