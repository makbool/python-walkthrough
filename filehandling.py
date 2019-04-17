'''
Created on 14-Apr-2019

@author: Administrator
'''

import os

writingfile = open("sample.py", "w+")

print(writingfile.name)

print(writingfile.mode)

writingfile.write("print(\"Hello\")")
writingfile.write("\n")
writingfile.write("print(\"Bye\")")

writingfile.close()

readingfile = open("sample.py", "r")

print(readingfile.read())

readingfile.close();

readingfile = open("sample.py", "r")

print(readingfile.read(5))
print(readingfile.read(5))

readingfile.close();

os.rename("sample.py", "demo.py")

os.remove("demo.py")

