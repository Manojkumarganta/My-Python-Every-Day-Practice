def is_palindrome_number(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False
num = int(input("Enter a number: "))
if is_palindrome_number(num):
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")
