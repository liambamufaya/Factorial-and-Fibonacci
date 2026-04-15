def Factorial(x):
    if x == 1:
        return 1
    else:
        return x * Factorial(x-1)


#Get input from the user
number = int(input("Enter number "))
print(Factorial(number))