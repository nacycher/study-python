for i in range(10):
    print(i)

print(list(range(10)))

result = 0
for i in range(1, 101):
    result += i
print(result)

# 1! + 2! + 3!.... + n!

def fib(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        i += 1
    return result

def fib_sum(n):
    if n <= 1:
        return 1
    result = 0
    for i in range(1, n + 1):
        result += fib(i)
        i += 1
    return result
print(fib(3))
print(fib_sum(3))