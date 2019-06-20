'''
Created on 18-Apr-2019

@author: Administrator
'''

employee = {'name':'Raj', 'age':22, 'phone':{'home':8899, 'off':999}}

print(employee)

print(str(employee))

print(employee['age'])

# print(employee['id'])

print(employee.get('age'))

print(employee.get('id', -1))

print(employee.items())
print(employee.keys())
print(employee.values())

print(sorted(employee.keys(), reverse=True))

