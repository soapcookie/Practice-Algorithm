numbers = []

for num in range(10):
    num = int(input())
    numbers.append(num%42)

print(len(set(numbers)))