from libs.math import natural_number_sum


def main():
    T = int(input().rstrip())
    for _ in range(T):
        N = int(input().rstrip())
        print(3 * natural_number_sum((N - 1) // 3) +
              5 * natural_number_sum((N - 1) // 5) - 15 *
              natural_number_sum((N - 1) // 15))


if __name__ == '__main__':
    main()
