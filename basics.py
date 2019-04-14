'''
Created on 14-Apr-2019

@author: Administrator
'''

print('Hello')

a = 10.6
b = 20.8

print(a + b)

'''
Mathematically, a complex number is a number of the form A+Bi where i is the imaginary number, equal to the square root of -1.
'''

c = 3 + 5j
d = 2 + 3j

e = d - c

print(e)

print(e.real)

print(e.imag)

'''
Tuple - Immutable
'''
lang = ('English', 'Hindi', 'Telugu')

print(lang)

'''
'tuple' object does not support item assignment
lang[1]='Python'
'''

'''
List - Mutable
'''

courses = ['C', 'C++', 'JAVA', 'ORACLE']

print(courses)

courses[1] = 'DS'

print(courses)

employee = ('Banu', lang, courses)

print(employee) 
print(employee[0])
print(employee[1])
print(employee[2])

empdetails = {'Name':'Banu', 'Languages':lang, 'Courses' : courses}

print(empdetails['Name'])
print(empdetails['Languages'])
print(empdetails['Courses'])

'''
Sets Mutable
Duplicate values are ignored
'''

subjects = {'ENGLISH', 'TELUGU', 'HINDI', 'TELUGU'}

print(subjects)

