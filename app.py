import random

a = random.randint(0,10)

print(a)
while True:
  num = input('guess a number:')
  num = int(num)
  print("try again")
  if a == num:
    break

print("Your guess the right number")