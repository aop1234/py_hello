import pickle
import json
from datetime import datetime 

d1 = dict(name='george', age=50, job='engineer', salary=3000)

# write(save) dict into file
with open('c:\py_json.dat', 'wb') as f:
    pickle.dump(d1,f)

# load dict from file
with open('c:\py_json.dat', 'rb') as f:
    d2=pickle.load(f)   # d2 is dict

print('d2 is %s : %s' % (type(d2), d2))

d3 = json.dumps(d1) # d3 is json string
print('d3 is %s : %s' % (type(d3), d3))


# serialize object to json
class Pig(object):
    def __init__(self, gender, birthday, weight, color):
        self.gender = gender
        self.birthday = birthday
        self.weight = weight
        self.color = color

little_pig = Pig('male', str(datetime(2010, 10, 1, 10, 30)), '300kg', 'black and white')

d4 = json.dumps(little_pig, default=lambda o: o.__dict__) 
print('d4 is %s : %s' % (type(d4), d4)) # json string

# deserialize object from json
def dict2pig(d):
    return Pig(d['gender'], d['birthday'], d['weight'], d['color'])

little_pig_clone = json.loads(d4, object_hook=dict2pig)
print(little_pig_clone)

