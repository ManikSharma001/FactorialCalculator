def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print("What number would you like to factorial?")
num = int(input())

facto = factorial(num)
print(facto)
