f = open("day1_input.txt")
num1 = []
num2 = []
for line in f:
    num1.append(int(line[0:5]))
    num2.append(int(line[8:13]))

num1.sort()
num2.sort()

sum = 0
for n1, n2 in zip(num1, num2):
    d = abs(n2 - n1)
    sum = sum + d

print(sum)

# part 2
sum2 = 0
for n in num1:
    n_count = num2.count(n)
    sum2 = sum2 + n * n_count

print(sum2)
