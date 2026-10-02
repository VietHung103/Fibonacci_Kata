def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci must be non negative-integer.")
    if n <= 1:
        return n
    a = 0
    b = 1
    for _i in range(n - 1):
        a, b = b, a + b
    return b
