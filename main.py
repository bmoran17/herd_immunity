class Student:

  def __init__(self, name, age, gpa):
    self.name = name
    self.age = age
    self.gpa = gpa
  
  def info(self):
    print(f"{self.name}, age {self.age} has a gpa of {self.gpa}.")

student1 = Student("Jack", 12, 4.50)
student2 = Student("Ariel", 10, 3.60)

student1.info()
  