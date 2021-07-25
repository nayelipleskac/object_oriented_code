#Inheritance.py

class base:
    def init(self):
        self.attr = 'something'
    def display(self):
        print('print funciton in the base class method')

class derived(base):
    pass    #do not create any attributes initially
            #and see how this class inherits the Base class' attributes

obj1 = derived()
print(obj1.attr)
obj1.display()