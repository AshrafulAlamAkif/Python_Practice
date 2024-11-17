#Function call and same value name
name = "Akif"
def greet():
    name = "akif"
    print("My name is",name) #print inside variable value
greet()
print(name,"is the Global name") #outside