#Prime Numbers exercise using Python
import math

def isPrime(number):
    if (number > 1):
        for i in range(2, int(math.sqrt(number)) + 1):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    isPrime(number)