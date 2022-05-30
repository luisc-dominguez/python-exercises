#Palindrome exercise using Python

from string import ascii_letters

def palindrome(userInput):
    formatted = [char.lower() for char in userInput if char in ascii_letters]
    if (formatted == formatted[::-1]):
        res = print("Your phrase/word IS a palindrome\n")
        return res
    else:
        res = print("Your phrase/word IS NOT a palindrome\n")
        return res

if __name__ == "__main__":
    userInput = input("Enter a word/phrase: ")
    palindrome(userInput)