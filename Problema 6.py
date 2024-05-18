def fibonacci(hasta):
    a, b = 0, 1
    fibonacci_series = [a]
    while b <= hasta:
        fibonacci_series.append(b)
        a, b = b, a + b
    return fibonacci_series

# Serie de Fibonacci hasta 50
print("Serie de Fibonacci hasta 50:")
print(fibonacci(50))
