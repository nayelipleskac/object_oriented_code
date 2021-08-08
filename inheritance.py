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


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, studentID, GPA):
#         super().__init__(fname, lname)
#         self.studentID = studentID
#         self.GPA = GPA
#     def printname(self):
#         print('this is the overriding method!')

# class Teacher(Person):
#     def __init__(self, fname, lname, studentList):
#         super().__init__(fname,lname)
#         self.studentList = studentList

# s1 = Student('Robi', 'Sharma', 1, '1.0')
# s2 = Student('Tiya', 'Sharma', 2, '5.0')
# t1 = Teacher('Julian', 'Harriott',[s1,s2])
# print(s1.GPA)
# print(s2.studentID)
# print('inheriting: ',s2.printname(), s1.printname())
# for each in t1.studentList:
#     print(each.printname())


# class Person:
#     def __init__(self, first, last, email, DOB):
#         self.first = first
#         self.last = last
#         self.email = email
#         self.DOB = DOB

# class Student(Person):
#     def __init__(self, first, last, email, DOB, studentID, GPA):
#         # Person.__init__(self, first, last, email, DOB)
#         super().__init__(first, last, email, DOB)
#         self.studentID = studentID
#         self.GPA = GPA

# class Teacher(Person):
#     def __init__(self, teacherID, listOfStudents, class_size ):
#         # super().__init__(first, last, email, DOB, GPA)
#         self.teacherID = teacherID
#         self.listOfStudents = listOfStudents
#         self.class_size = class_size
#     def showStudentInfo(self):
#         for each in self.listOfStudents:
#             print(self.teacherID, each.first, each.last, each.email, each.DOB, each.GPA)
#     def add_students(self):
#         s6 = Student(firstName, lastName, studemail, studDOB, studID, studGPA)
#         self.listOfStudents.append(s6)
#     def remove_students(self):
     
        
#         for each in self.listOfStudents:
#             if fname == each.first:
#                 print('checking first name')
#                 print(each)
#                 self.listOfStudents.remove(each)

    
# s1 = Student('Aaron', 'Pleskac', 'apleskac@gmail.com', '12/03/06', 5, '4.0')
# s2 = Student('Nick', 'Pleskac', 'npleskac@gmail.com', '10/05/07', 8, '3.0')
# s3 = Student('Mark', 'Pleskac', 'mpleskac@gmail.com', '7/03/05', 2, '3.5')
# s4 = Student('Laura', 'Pleskac', 'lpleskac@gmail.com', '9/25/06', 9, '2.5')
# s5 = Student('Doug', 'Pleskac', 'dpleskac@gmail.com', '8/03/05', 9, '3.0')
# studentList = [s1, s2, s3, s4, s5]

# t1 = Teacher('teacher', studentList, len(studentList))
# t2 = Teacher('teacher', [s3, s4], len(studentList))
# t3 = Teacher('teacher', [s5], len(studentList))

# # t2 = t1.showStudentInfo()

# openinginput = input('Add or remove a student?')

# if openinginput == 'add':
#     print('Enter in all fields of a student obj!')
#     firstName = input('fname: ')
#     lastName = input('lname: ')
#     studemail = input('studemail: ')
#     studDOB = input('DOB: ')
#     studID = input('id: ')
#     studGPA = input('GPA: ')
#     # t1.add_students()
#     # t1.showStudentInfo()
#     t2.add_students()
#     t2.showStudentInfo()

# if openinginput == 'remove':
#     print('Enter in the name of the student you want to remove')
#     fname = input('fname: ')
#     lname = input('lname: ')
#     # t1.remove_students  ()
#      # t1.showStudentInfo()
#     t3.remove_students()
#     t3.showStudentInfo()


import random, pygame, time
screen = pygame.display.set_mode((600, 600))
pygame.init()
pygame.display.set_caption("Inheritance")
from pygame.constants import KEYDOWN, K_c, K_r, K_s, QUIT
clock = pygame.time.Clock()


black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (200, 200, 0)

colors = [red, green, blue, white, yellow]


class shapes:
    def __init__(self, x, y, color ):
        self.x = x
        self.y = y
        self.color = color
       
        # self.size = size

class rect(shapes):
    def __init__(self, x, y, color, length, width):
        super().__init__(x, y, color, )
        self.length = length
        self.width = width
        self.shape = 'rectangle'
    def draw_rect(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.length, self.width), 0)

class circle(shapes):
    def __init__(self,x, y, color):
        super().__init__(x, y, color)
        self.shape = 'circle'
    def draw_circle(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 20, 0)


obj_list = []

while True:
    # screen.fill(black)
    clock.tick(60)

    for obj in obj_list:
        if obj.shape == 'rectangle':
            obj.draw_rect()
        if obj.shape == 'circle':
            obj.draw_circle()
        if obj.shape == 'square':
            obj.draw_rect()

      

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                rectangle_obj = rect(random.randint(50, 550), random.randint(50,550), random.choice(colors), 100, 200)
                
                obj_list.append(rectangle_obj)
            if event.key == K_c:
                circle_obj = circle(random.randint(50, 550), random.randint(50,550), random.choice(colors))
                
                obj_list.append(circle_obj)
            if event.key == K_s:
                square_obj = rect(random.randint(50, 550), random.randint(50,550), random.choice(colors), 150, 150)
                
                obj_list.append(square_obj)

    pygame.display.update()





   


