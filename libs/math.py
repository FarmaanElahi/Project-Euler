def natural_number_sum(number):
    return number * (number + 1) // 2


def fibonacci(n):
    a = 0
    b = 1
    while a + b < n:
        a, b = b, a + b
        if b % 2 == 0:
            yield b
