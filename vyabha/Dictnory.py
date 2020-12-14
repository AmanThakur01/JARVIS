data = {1:'vyabha', 2:'aman', 4:'pratik' }
print(data)
print(data[1])
print(data.get(1))
print(data.get(3))
print(data.get(3, 'Not found'))
keys = ['priya', 'riya', 'jiya']
values = ['python', 'java', 'js']
data = dict (zip(keys,values))
print(data)
print(data['riya'])
data['monika'] = 'cs'
print(data)
del data['priya']
print(data)
prog = {'js':'atom', 'python':['pycharm','sublime'], 'java':{"JSE":'netbeans', "JEE":'elipse'}}
print(prog)
print(prog["js"])
print(prog['python'][1])
print(prog['java']["JEE"])
a = prog.get(3)
if a == None:
    print("it is true")