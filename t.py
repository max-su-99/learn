import sys
import os
import fileinput
#import Applications.Utilities
print(sys.executable)

import io
files = io.open("t.py")

firstline =files.readline()
while firstline > "" :
    print("----" + firstline)
    firstline =files.readline()


print('1')
def funcname(self, parameter_list):
    raise NotImplementedError
def testfun(para1,parameter):
    print("test fun printing" + para1+ parameter)
testfun("para","para2")
#funcname()
a=1
print(a)

class animal:
    #@staticmethod
    def bark(self, parameter_list):
        print("anmial bark")
    def name(self, arameter_list):
        print("my name is animal")


animal.bark("tets","testPara")
print(os)

#print (944.99 * .75 + 944.99 * 0.13)
#print (319.96 * .13)

testList = [1,2,3,4]

stringTestList =[]

for ite in testList:
    print (ite)
    stringTestList.append(str(ite))
for ite in range(1,5):

    print(ite)
print(",".join(stringTestList))



