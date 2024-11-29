#Function call and same value name
name = "Akif"
def greet():
    name = "akif"
    print("My name is",name) #print inside variable value
greet()
print(name,"is the Global name") #outside



#Using global variable
def MyFun():
    global nam
    nam = "hasas"
    print(nam)
MyFun()
print(nam)



#Without Global Variable
x = "Akif"  #outside variable

def myfunc():
    x = "Ashraful"  #inside variable
    print(x)    #print inside variavle of a function
myfunc()
print(x) #print outside variavle of a function
    
