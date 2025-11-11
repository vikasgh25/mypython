# finding largest of three number
x = int(input("enter first number:"))
y = int(input("enter second number:"))
z = int(input("enter third number:"))
if x > y and x > z:
  print(x,"  is greater number")
elif y > x and y >z:
   print(y,"  is greater number")
else:
   print(z,"  is greater number")
