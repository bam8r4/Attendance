#Same attendance problem solved with regular expressions.
import re

def checkString(mystring):
    absent = re.search(".*A.*A.*", mystring)
    late = re.search("L{3}",mystring)

    if absent or late:
        print("False")
    else:
        print("True")


mylist = ['PPALLP','PPALLL','PAPALL','PLPALL']

for x in mylist:
    checkString(x)
