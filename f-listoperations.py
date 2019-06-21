'''
Created on 18-Apr-2019

@author: Administrator
'''

courselist = ['C', 'C++', 'JAVA', 'SPRING', 'ORACLE', 'SQL SERVER']

print(courselist[1])
print(courselist[1:3])
print(courselist[-2])
print(courselist + ['PYTHON', 'REACT', 'AI'])

print(courselist * 3)

print('PYTHON' in courselist, 'JAVA' in courselist)

del (courselist[1])
print(courselist)

print(courselist.pop(1))
print(courselist)

courselist.remove('SQL SERVER')
print(courselist)

courselist.append("CSS")

courselist.extend(['HTML', 'JAVASCRIPT'])

courselist.insert(3, 'HIBERNATE')

print(courselist)

print(courselist[::-1])

print(sorted(courselist))

employeenames = [('Ram', 'Robert', 'Rahim'), ('Amar', 'Akbar', 'Anthony', 'Ram', 'Robert', 'Rahim')]

print(employeenames)

print(len(employeenames))

print(employeenames[1][1:3])

print(employeenames[1][2:-1])
