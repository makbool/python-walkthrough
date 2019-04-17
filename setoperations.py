'''
Created on 18-Apr-2019

@author: Administrator
'''

result1 = {11, 33, 44, 66, 77, 99}

result2 = {22, 66, 88, 99}

result3 = result1 | result2
result4 = result1 & result2
result5 = result1 - result2

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
B = {2, 4, 6, 8, 0}

print(A)

print(B)

print(A.issuperset(B))

print(B.issubset(A))

A.clear()

print(A)

