'''
Created on 18-Apr-2019

@author: Administrator
'''


def squarefun(a):
    return a * a

# if this file is run directly then
# __name__ is set to main else
# __name__ is set to module name (file name here)

print(__name__)

if __name__ == "__main__" :
    print("This was run directly")
else:    
    print("This was imported")
    
