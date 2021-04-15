def addition(num1, num2):
    result1 = (float(num1) + float(num2))
    print(result1)

def substraction(num1, num2):
    result2 = (float(num1) - float(num2))
    print(result2)


def multi(num1, num2):
    result3 = (float(num1) * float(num2))
    print(result3)



def division(num1, num2):
    if float(num1) == 0 or float(num2) == 0:
        print("You can't type 0")

    else:
        result4 = (float(num1) / float(num2))
        print(result4)





addition(5 , 6)
substraction(5,7)
multi(9, 5)
division(4 ,8)
