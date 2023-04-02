def factorial(n):
    itog_ = 1
    for i in range(1, n + 1):
        itog_ *= i
    return itog_

print(factorial(5))
