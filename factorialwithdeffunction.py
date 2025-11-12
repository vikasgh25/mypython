factorial() that finds the factorial of a given number using a loop.
def factorial(a):
  fact = 1
  for i in range(1,a+1):
    fact = fact*i
  return fact
factorial(5)
