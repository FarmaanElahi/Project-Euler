# Work out the first ten digits of the sum of N 50 digit numbers.


total = 0
for x in range(int(input())):
    total += int(input().rstrip())
print(str(total)[:10])
