class Student:
    def __init__(self, registration_number, name):
        self.registration_number = registration_number
        self.name = name

    def __str__(self):
        return(f"registration_number: {self.registration_number}, name: {self.name}")

student1 = Student("RegS23B13/O30","Lubogo Patrick" )
print(student1)
