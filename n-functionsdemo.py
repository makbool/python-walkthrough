'''
Created on 18-Apr-2019

@author: Administrator
'''

from m_squarefunc import squarefun


def sumval(a, b, c=0):
    print("value of a=", a)
    print("value of b=", b)
    print("value of c=", c)
    return a + b + c


a = 10
b = 20
print(sumval(5, 4))
print(sumval(5, 4, 3))
print(sumval(c=100, b=200, a=300))
print(sumval(squarefun(a), squarefun(b)))
