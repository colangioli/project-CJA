#program calculates the mean
# Program calculate the mean
import sys

sum = 0
n = 0
# This line indicates that your partner has been here.
for number in sys.stdin:
   sum += float(number)
   n += 1

print "the mean is", (sum / n)
