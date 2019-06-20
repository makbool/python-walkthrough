'''
Created on 14-Apr-2019

@author: Administrator
'''

a = 10

b = 3

print(a + b, a - b, a * b, a / b , a % b)

print (a ** b)  # power

print (a // b)  # floor

a += 5

print(a)

print(a < b, not a < b)

c = 5

print (a < b or b < c, a > b and b > c)

today = 'Monday'

manager_meeting = 'Monday'

print (today == manager_meeting, today is manager_meeting)

a = [1, 2, 3]

b = a[:]  # Make a new copy of list `a` via the slice operator, and assign it to variable `b`

print(b == a, b is a)

courses = ['C', 'JAVA', 'PYTHON']

print('C' in courses, 'ORACLE' not in courses)

