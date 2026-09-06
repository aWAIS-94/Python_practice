s=input("Enter a string to check if it's a palindrome: ")
s=s.replace(" ", "").lower()
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
