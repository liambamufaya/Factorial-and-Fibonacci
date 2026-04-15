def Factorial(x):
    if x == 1:
        return 1
    else:
        return x * Factorial(x-1)
    
def Fibonacci(x):
     if x ==1:
          return 1
     elif x ==0:
          return 0
     else:
          return Fibonacci(x-1) + Fibonacci(x-2)
     
#Get input from the user
number = int(input("Enter number "))

if number <=0 :
    print("Enter positive integer")
else:
        print("Factorial of",number,"is ")
        print(Factorial(number))
        print()
        print("Fibonacci number of",number, "is")
        
        for i in range(number):
            print(Fibonacci(i), end=" ")
print()