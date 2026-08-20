v=[]
print(type(v))

v=[1,22,33,4,4,'uday']
print(v)

v=[1,2,33,44,'narendar']
print(v[-1])
print(v[0:4:2])

v=[1,22,33,44,'narendar']
v.append("python")
print(v)

v=[1,22,33,'narendar']
v.extend([5,66,88])
print(v)
v=[1,22,33,44,'narendar']
print(v.count(1))

v=[1,22,33,44,'narendar']
v.remove(22)
print(v)

v=[1,24,1,4,1553,5,'narendar']
v.pop(1)
print(v)

v=[1,24,1,4,1554,5,'kiran']
print(v.index(1554))