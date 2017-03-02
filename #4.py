# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome(limit):
    upper = limit - (limit % 11)
    for x in range(upper, 100000, -11):
        if is_palindrome(x) and is_divisible(x) and x < limit:
            return x


def is_palindrome(x):
    return str(x) == str(x)[::-1]


def is_divisible(n):
    for x in range(110, 1000, 11):
        if x != 0 and n % x == 0 and n / x < 1000:
            return True
    return False


for _ in range(int(input())):
    print(largest_palindrome(int(input())))
