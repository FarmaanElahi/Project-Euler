def natural_number_sum(number):
    return number * (number + 1) // 2


def fibonacci(maxi=4 * 10 ** 16):
    a = 0
    b = 1
    while a + b < maxi:
        a, b = b, a + b
        yield b


def smallest_factor(n):
    for x in range(2, int(n ** 0.5) + 1, 1):
        if n % x == 0:
            return x
    return n


def largest_prime_factor(n):
    while True:

        factor = smallest_factor(n)

        if n > factor:
            n //= factor
        else:
            return n


def generate_prime(start=2, end=100):
    for x in range(start, end):
        if (2 ** x - 2) % x == 0:
            yield x
