from hello_class import Person,Student,Worker

# dynamic create class from object
def bark(self, voice='silence'):
    return voice

Animal = type('Animal', (object,), dict(bark=bark))
a = Animal()
a.bark()


#dynamic create class from Person
def manage(self):
    print('%s is managing some job' %self.name)

Manager = type('Manager',(Person,),dict(manage=manage))
m = Manager('Robin Li')
m.manage()
print(m)    # called parent class Person's function __str__()


#dynamic create class from metaclass 
def print_resume(self):
    print(self.resume_list)

class WorkerMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add_work_history'] = lambda self,value :self.resume_list.append(value)
        attrs['print_resume'] = print_resume
        return type.__new__(cls, name, bases, attrs)

class WorkerEx(Worker, metaclass=WorkerMetaclass):
    def first_work(self):
        print(self.resume_list[0])


worker_ex = WorkerEx('Lu Qi')
worker_ex.add_work_history('Employed at Yahoo')
worker_ex.add_work_history('Employed at Microsoft')
worker_ex.add_work_history('Employed at Baidu')
worker_ex.first_work()

worker_ex.print_resume()
