def calculator():
    num1 = float(input("please input a number: "))
    num2 = float(input("please input another number: "))
    operator = input("choose an operator(e.g +, -, *, /):")
    


    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2

            

    if operator == "+":
            print("solution:", num1, '+', num2, '=', add)

    elif operator == "-":
                print("solution:", num1, '-',  num2, '=', sub)
            
    elif operator == "*":
                print("solution:", num1, '*', num2, '=', mul)

    elif operator =="/":
            if num2 == 0:
                print("invalid operation. Change the second number, it can't be 0")
            else:
                div = num1 / num2
                print('solution:', num1, '/', num2, '=', div )
        

    else:
                print('this operator is invalid')
calculator()