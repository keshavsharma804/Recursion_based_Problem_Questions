# def factorial(n):
#     
#     if n == 0 or n == 1:
#         return 1
#     
#     return n * factorial(n - 1)

# n = int(input("Enter a number: "))
# print("Factorial:", factorial(n))


# def sum_of_natural_numbers(n):
   
#     if n == 0:
#         return 0
#     return n + sum_of_natural_numbers(n - 1)

# n = int(input("Enter a number: "))
# print("Sum of first", n, "natural numbers:", sum_of_natural_numbers(n))


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Enter a number: "))
# print(f"Fibonacci({n}) =", fibonacci(n))


# ## Print numbers 1 to n
# def num(n):
#     if n<= 1:
#         return 
#     num(n-1)
#     print(n)
# n = int(input("ENter the number"))
# num(n)



# ## print numbers n to 1
# def num(n):
#     if n<= 1:
#         return
#     print(n) 
#     num(n-1)   
# n = int(input("ENter the number"))
# num(n)