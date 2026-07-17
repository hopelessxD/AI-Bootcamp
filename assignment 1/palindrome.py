def palindrome(num):
    print("original number", num)
    original = str(num)
    reversed = original[::-1]
    
    if original == reversed:
        return True
    else:
        return False

num = input("Enter a number: ")
if(palindrome(num)):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")