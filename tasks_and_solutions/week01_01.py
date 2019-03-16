import sys

digit_string = sys.argv[1]

l_sum = 0
for digit in digit_string:
    l_sum += int(digit)

print(l_sum)

# print(sum([int(x) for x in sys.argv[1]]))
