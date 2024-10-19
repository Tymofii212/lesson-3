print("lesson 3")

class Student:
    def __init__(self, Name, Surname, Age):
        self.Name = Name
        self.Surname = Surname
        self.Age = Age
        print("Create Succesfull")
    def print_student(self):
        print("Surname:",self.Surname,"\tName:", self.Name,"\tAge:",self.Age)



Student1 = Student("Vitalii", "Oxygen", 42)

Student2 = Student("Boris", "Brytva", 24)

Student1.print_student()

Student2.print_student()
