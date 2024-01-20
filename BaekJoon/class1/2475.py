# num1, num2, num3, num4, num5 = map(int,input().split())
#
# result = ((num1*num1)+(num2*num2)+(num3*num3)+(num4*num4)+(num5*num5))%10
# print(result)

nums = map(int, input().split())
result = 0

for i in nums:
    result += i ** 2

print(result%10)

