def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Example usage
num = int(input("enter number: "))
output = check_odd_even(num)
print(output)
