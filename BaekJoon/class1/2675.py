#첫번째 정수 S입력
#S의 개수만큼 정수값받기
#word(i)값에서 받은 문자들을 각 word(i)값만큼 반복출력

S = int(input())

for i in range(S):
    i, word = input().split()
    for j in word:
        print(j*int(i), end='')  
    print()  