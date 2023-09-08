print("Please enter a whole number: ")
number = int(input())

if number % 2 == 0:
  print("The number", number, "is divisible by 2.")

else:
  print("The number", number, "is not divisible by 2.")


if 100 % number == 0:
  print("The number", number, "is a factor of 100.")

else:
  print("The number", number, "is not a factor of 100.")