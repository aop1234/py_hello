#----------------------------------------------------------------------
# Class and Object
#----------------------------------------------------------------------

#base class
class Person(object):
    name = 'Person'
    __name = 'Student'
    def __init__(self,name):
        self.name = name
        self._name = name
        self._name_ = name
        self.__name = name
        self.__name_ = name
        self.__name__ = name
        self.resume_list = []

    def __str__(self):
        return 'Hello, I\'m %s.' % self.name

    # call attribute from inner
    def get_name(self):
        print('Class Person.name: ', Person.name)
        print('Object name: ', self.name)
        print('Object _name: ', self._name)
        print('Object _name_: ', self._name_)
        print('Object __name: ', self.__name)
        print('Object __name_: ', self.__name_)        
        print('Object __name__: ', self.__name__)                


#child class inherit from person
class Student(Person):
    name = 'Student'

    def __str__(self):
        return '%s %s' % (Person.__str__(self), 'I like mathmatics.')

    def study(self):
        print('%s is studying hard' %self.name)

    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, birth):
        if(birth<1900):
            raise ValueError('Cannot be borned before 1900')
        else:
            self._birth = birth

    @property
    def age(self):  # readonly attr
        return 2018-self._birth


#child class inherit from person
class Worker(Person):
    name = 'Woker' 

    def __str__(self):
#1        return '%s %s' % (Person.__str__(self), 'I like programing.')
#2        return '%s %s' % (super(Worker,self).__str__(), 'I like programing.')
        return '%s %s' % (super().__str__(), 'I like programing.') #3

    def work(self):
        print('%s is working day and night' %self.name)


#child class multi-inherit from student and worker
class ParttimeStudent(Student,Worker):
    name = 'Parttime Student'

    def __str__(self):
        return '%s %s %s' % (Student.__str__(self), Worker.__str__(self), 'and I\'m fighting!') 
#        return '%s %s %s %s' % (super(ParttimeStudent, self)__str()__, , 'and I\'m fighting!') 

    def doing(self):
        self.study()
        self.work()
        print('%s has no time to sleep.' % self.name)


# call by outer function to get attributes
def get_name(student):
    print('Class Person.name: ', Person.name)
    print('Object name: ', student.name)
    print('Object _name: ', student._name)
    print('Object _name_: ', student._name_)    
    # Error: cannot access __name, __name_
    #print('Object __name: ', student.__name)
    #print('Object __name_: ', student.__name_)
    print('Object __name__: ', student.__name__)       
    print('Object o._Person__name: ', student._Person__name) 


# Instance Initlize
p = Person('Bill Gates')    
p.get_name()
get_name(p)
print(p)

s = Student('Larry Pages')
s.study()
print(s)

w = Worker('Jack Ma')
w.work()
print(w)

sw = ParttimeStudent('Pony Ma')
sw.doing()
print(sw)

# identity the type of instance
isinstance(s, Person) #true
isinstance(s, Student)  #true
isinstance(w, Worker) #true
isinstance(sw, ParttimeStudent) #true
isinstance(sw, Student)
isinstance(sw, Worker)
type(s) == Person #false
type(s) == Student #true

# bind a function to an instance
from types import MethodType
def set_age(self, age):
    self.age = age

w.set_age = MethodType(set_age, w)
w.set_age(20)
print('%s\'s age is %s' % (w.name, w.age))

#bind a function to a class
def set_gender(self, gender):
    self.gender = gender

Student.set_gender = set_gender
s.set_gender('male') 
print('%s is %s' % (s.name, s.gender))   



i=1



