x = "hello"

def param():
    global x
    x = "hi!!"
    print(x + "My name is Param")

param()
print(x + "My name is Param")
