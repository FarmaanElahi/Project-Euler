from libs.math import smallest_factor


#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(n):
    while True:

        factor = smallest_factor(n)

        if n > factor:
            n //= factor
        else:
            return n


def main():
    for _ in range(int(input())):
        print(str(largest_prime_factor(int(input()))))


if __name__ == '__main__':
    main()
