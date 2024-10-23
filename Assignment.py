
num = int(input("Enter any number to be checked: "))

sum = 0

num1 = num
while num1 > 0:
  digit = num % 10
  
  sum += digit ** 3

  num1 //= 10

if num == sum:
  print(num," is an armstrong number")
else:
  print(num," is not an armstrong number")  
  
