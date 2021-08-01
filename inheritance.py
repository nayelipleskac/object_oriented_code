#Inheritance.py

# class base:
#     def init(self):
#         self.attr = 'something'
#     def display(self):
#         print('print funciton in the base class method')

# class derived(base):
#     pass    
            

# obj1 = derived()
# print(obj1.attr)
# obj1.display()

#a derived class can use the base class's init method only if it doesn't have one of its own


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, studentID, GPA):
        super().__init__(fname, lname)
        self.studentID = studentID
        self.GPA = GPA
    def printname(self):
        print('this is the overriding method!')

class Teacher(Person):
    def __init__(self, fname, lname, studentList):
        super().__init__(fname,lname)
        self.studentList = studentList

s1 = Student('Robi', 'Sharma', 1, '1.0')
s2 = Student('Tiya', 'Sharma', 2, '5.0')
t1 = Teacher('Julian', 'Harriott',[s1,s2])
print(s1.GPA)
print(s2.studentID)
print('inheriting: ',s2.printname(), s1.printname())
for each in t1.studentList:
    print(each.printname())


class Person:
    def __init__(self, first, last, email, DOB):
        self.first = first
        self.last = last
        self.email = email
        self.DOB = DOB

class Student(Person):
    def __init__(self, first, last, email, DOB, studentID, GPA):
        # Person.__init__(self, first, last, email, DOB)
        super().__init__(first, last, email, DOB)
        self.studentID = studentID
        self.GPA = GPA

class Teacher(Person):
    def __init__(self, teacherID, listOfStudents, class_size):
        self.teacherID = teacherID
        self.listOfStudents = listOfStudents
        self.class_size = class_size
    def showStudentInfo():


s1 = Student('Aaron', 'Pleskac', 'apleskac@gmail.com', '12/03/06', 5, '4.0')
s2 = Student('Nick', 'Pleskac', 'npleskac@gmail.com', '10/05/07', 8, '3.0')
s3 = Student('Mark', 'Pleskac', 'mpleskac@gmail.com', '7/03/05', 2, '3.5')
s4 = Student('Laura', 'Pleskac', 'lpleskac@gmail.com', '9/25/06', 9, '2.5')
s5 = Student('Doug', 'Pleskac', 'dpleskac@gmail.com', '8/03/05', 9, '3.0')
studentList = [s1, s2, s3, s4, s5]

t1 = Teacher('1', studentList, len(studentList))

for each in studentList:
    print(each.first, each.last, each.email, each.DOB, each.studentID, each.GPA)
