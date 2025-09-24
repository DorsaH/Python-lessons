def test_function():
    print("This is a test function")


test_function()

def test_function1(text):
    print(text)

test_function1("This is a test function1")

# setting a default value for the parameter
def test_function2(text = "Hi test2"):
    print(text)

test_function2()

# you can change the order of parameters but you need to specify
def test_function3(text = "Hi test3", x =2):
    print(text)
    print(x)

test_function3(x =6, text="test3")

# you can have a special parameters, you can give it any parameter. it gives a tuple
def test_function4(*args):
    print(args)

test_function4("test4" , 5, False, [0,1,2])

# allows you to have as many as positional arguments and it creates a dictionary
def test_function5(**args):
    print(args)

test_function5(x ="test5" , y =5, b =False, z =[0,1,2])

# return statment
def difference(num1, num2):
    if num1>num2:
        result = num1 - num2
    else:
        result = num2 - num1
    return (result)

print(difference(10,50))
print(difference(33, 11))


# multiple returns, you can return tuple
def difference2(num1, num2):
    if num1>num2:
        result = num1 - num2
        precentage = (result/num1) * 100
    else:
        result = num2 - num1
        precentage = (result/num2) * 100
    # returns a tuple
    # return (result , precentage)
    return (result , f"{int(precentage)}%")

print(difference2(10,50))
print(difference2(33, 11))

print()
