import sys

sys.argv

print(sys.argv[2], sys.argv[1], int(sys.argv[3]))

if sys.argv[1] == "+":
    sum1 = int(sys.argv[2]) + int(sys.argv[3])

if sys.argv[1] == "-":
    sum1 = int(sys.argv[2]) - int(sys.argv[3])

if sys.argv[1] == "*":
    sum1 = int(sys.argv[2]) * int(sys.argv[3])

if sys.argv[1] == "/":
    sum1 = int(sys.argv[2]) / int(sys.argv[3])

print(sum1)
