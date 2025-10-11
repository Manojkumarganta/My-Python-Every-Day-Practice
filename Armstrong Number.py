# Check if a number is an Armstrong number

num = int(input("Enter a number: "))

# Find the number of digits
order = len(str(num))

# Initialize sum
sum = 0

# Make a copy of the original number
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Check if the number is equal to the sum
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
