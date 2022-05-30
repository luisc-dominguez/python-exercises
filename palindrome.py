#Palindrome exercise using Python

def palindrome(word):
    if (word == word[::-1]):
        res = print("Your word IS a palindrome\n")
        return res
    else:
        res = print("Your word IS NOT a palindrome\n")
        return res

if __name__ == "__main__":
    word = input("Enter a word: ")
    palindrome(word)