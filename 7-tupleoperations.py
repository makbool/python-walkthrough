'''
Created on 18-Apr-2019

@author: Administrator
'''

directions = ('LEFT', 'RIGHT', 'TOP', 'BOTTOM')

print(directions)

print(len(directions), max(directions), min(directions))

testnum = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

for item in testnum :
    print(item, end='\n')

print(len(testnum))

print(testnum[1])

testnum[1][1] = 50

print(testnum[1])

del(testnum[2][1])

print(testnum[2])

