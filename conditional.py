'''
Created on 14-Apr-2019

@author: Administrator
'''

a = 10

b = 5

if a > b :
    print("A greater than B")
elif a < b :
    print ("A less than B")
else:
    print("A is equal to b")
    


c = 12

if a > c :
    print("A greater than C")
    if a > b :
        print ("A is greater than C & B")



if a > c :
    print("A greater than C")
if a > b :
    print ("A is greater than B")
