# Python program that checks whether a number is:


num = float(input("Enter a number: "))


if num > 0:
    if num % 2 == 0:
        print("The number is Even and Positive.")
    else:
        print("The number is Odd and Positive.")
elif num < 0:
    if num % 2 == 0:
        print("The number is Even and Negative.")
    else:
        print("The number is Odd and Negative.")
else:
    print("The number is zero, which is Even but neither Positive nor Negative.")

