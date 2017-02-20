def natural_number_sum(number):
    return number * (number + 1) // 2


def fibonacci(maxi=4 * 10 ** 16):
    a = 0
    b = 1
    while a + b < maxi:
        a, b = b, a + b
        yield b
