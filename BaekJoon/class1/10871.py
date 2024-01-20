# N, X = map(int, input().split())


# for _ in range(N):
#     i = list(map(int, (input().split())))
#     if i < X:
#         print(i)

N, X = map(int, input().split())
result = list(map(int, input().split()))

for i in range(N):
    if result[i] < X:
        print(result[i], end= " ")


    
