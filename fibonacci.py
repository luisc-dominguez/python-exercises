#Fibonacci exercise using Python

def fibonacci(num):
    if (num < 0 ):
        return print("Please enter a positive number")
    elif (num == 1 or num == 0):
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
  
if __name__ == "__main__":
    i = input("How many Fibonacci numbers do you want to see? ")
    numbers = int(i)
    
    for i in range(numbers):
        res = str(fibonacci(i))
        print(res + ", ")
    