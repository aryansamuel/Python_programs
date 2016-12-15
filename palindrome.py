def isPalindrome(quote):
    import string
    if not(quote.isalpha()):
        for punc in string.punctuation:
            quote = quote.replace(punc, "")
        quote = quote.replace(" ", "")
        quote = quote.lower()
        print(quote)

    if len(quote) is 1:
        return True
    if len(quote) is 2:
        if quote[0] is quote[1]:
            return True
        else:
            return False
    if quote[0] is quote[-1]:
        print(quote[1:-1])
        return isPalindrome(quote[1:-1])
    else:
        return False

    
def main():
    string = input("Give me something on the next line, and I will determine if it is a palindrome.")
    return isPalindrome(string)
main()
