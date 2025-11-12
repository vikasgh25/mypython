sum_of_n_numbers() that accepts n numbers (entered by the user in a list) and returns their total sum.
def sum_of_n_numbers(a):
  sum = 0
  for i in a:
    sum = sum+i
  return sum
sum_of_n_numbers([1,2,3,4,5])
