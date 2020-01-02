def max_of_three():
    numbers = input("Enter three numbers: ")
    num1, num2, num3 = numbers.split()
    if (num1 > num2) and (num1 > num3):
        largest = num1
    elif (num2 > num1) and (num2 > num3):
        largest = num2
    else:
        largest = num3
    print(largest)


max_of_three()
