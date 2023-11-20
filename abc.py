def add_function():
    result=0
    x=int(input("enter the first digit:n"))
    y=int(input("enter the second digit"))
    result=x+y
    return result

def multiply_function():
    result=0
    x=int(input("enter the first digit/"))
    y=int(input("enter the second digit"))
    result=x*y
    return result
def subtract_function():
    result=0
    x=int(input("enter the first digit/"))
    y=int(input("enter the second digit"))
    result=x-y
    return result
def divide_function():
    result=0
    x=int(input("enter the first digit/"))
    y=int(input("enter the second digit"))
    result=x/y
    return result
def switch_function():
    task=str(input("which task you wanna perform"))
    if task=="add" or task=="Add":
        final_result=add_function()
    elif task=="subtract" or task=="Subtract":
        final_result=subtract_function()
    elif task=="multiply" or task=="Multiply":
        final_result=multiply_function()
    elif task=="divide" or task=="Divide":
        final_result=divide_function()
    else:
        print("i cant perform this operation")
    return final_result

print(switch_function())
    
print("Added something new")