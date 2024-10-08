
class student:

    class_year = 2024
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.num_students +=1

student1 = student("Emanuel",30)
student2 = student("Juri",18)

print(student1.name, student1.age)
print(student2.name, student2.age)

print(student1.class_year)
print(student2.class_year)

print(student.num_students)




