def add(x,y):
    return x+y

def subtract(x,y):
    return x-y


def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y
operations = {
    "+" :add,
    "-" :subtract,
    "*" :multiply,
    "/" :divide
}

def calculator():
    num1 = int(input("enter first number"))
    for i in operations:
        print(i)
    print("pick any operation symbol")
    operation_symbol = input()
    num2 = int(input("enter another number"))
    function_calculator = operations[operation_symbol]
    answer = function_calculator(num1,num2)
    print(f"answer is:{answer}")

calculator()
