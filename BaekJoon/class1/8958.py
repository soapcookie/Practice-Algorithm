# n = int(input())
# score = 0
#
# for i in range(n):
#     answer = list(input())
#     answer.append(i)
#     if answer[i] in "o":
#         score += 1
#     else:
#         score = 0
#
# print(score)

n = int(input())

for _ in range(n):
    answer_list = list(input())
    score=0
    result=0
    for answer in answer_list:
        if answer == "O":
            score +=1
            result += score
        else:
            score=0
    print(result)

