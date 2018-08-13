from collections import namedtuple

# namedtuple
Point = namedtuple('Point', ['x','y'])
p = Point(20,30)
print('p.x = %d, p.y = %d' %(p.x, p.y))

print(isinstance(p, Point))    #true
print(isinstance(p, tuple))   #true

Circle = namedtuple('Circle',['x','y','r'])
c = Circle(20,30,100)
print(c)
 

#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque

q = deque(['b','c','d'])
print(q)  #deque(['b', 'c', 'd'])

q.append('e')
print(q)    #deque(['b', 'c', 'd', 'e'])

q.appendleft('a')   
print(q)    #deque(['a', 'b', 'c', 'd', 'e'])

q.pop()
print(q)    #deque(['a', 'b', 'c', 'd'])

q.popleft()
print(q)    #deque(['b', 'c', 'd'])


#defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['name'] = 'GeorgeZhang'
print(dd['name'])
print(dd['nick-name'])


