#program using a while loop to find the sum of first n natural numbers
n = int(input("Enter a positive integer: "))
sum_n = 0
i = 1
while i <= n:
    sum_n += i
    i += 1
print("The sum of the first", n, "natural numbers is:", sum_n)
