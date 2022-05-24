#Fibonacci exercise using Python

def fibonacci(num):
    if (num == 0 or num == 1):
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
  
i = input("How many Fibonacci numbers do you want to see? ")
max_num = int(i)
  
for number in range(max_num):
    print(fibonacci(number ), end = ", ")