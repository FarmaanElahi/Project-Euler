from libs.math import natural_number_sum


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    t = int(input().rstrip())
    for _ in range(t):
        N = int(input().rstrip())
        print(3 * natural_number_sum((N - 1) // 3) +
              5 * natural_number_sum((N - 1) // 5) - 15 *
              natural_number_sum((N - 1) // 15))


if __name__ == '__main__':
    main()
