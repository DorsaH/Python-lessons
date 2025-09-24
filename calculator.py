def calculator(num1, num2, operator):
    match operator:
        case "+" :
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "/":
            if num2 != 0 :
                result = num1/num2
            else:
                result= "can not divide by zero!"
        case "*":
            result = num1 * num2
        case "**":
            result = num1 ** num2
        case "%":
            if num2 != 0 :
                result = num1 % num2
            else:
                result= "can not divide by zero!"
        case _:
            result= "wrong operator!"
            # result = None
    return result

print(calculator(-11, 0, "/"))