def checkString(mystring):
    acount = 0
    for x in range(0,len(mystring)):
        if(mystring[x]=="A"):
            acount += 1

    if(acount >=  2 or mystring.find("LLL") > -1):

        print("False")
    else:
        print("True")


mylist = ['PPALLP','PPALLL','PAPALL','PLPALL']

for x in mylist:
    checkString(x)
