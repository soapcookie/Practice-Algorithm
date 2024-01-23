word = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','z','y','z']

#word의 길이만큼 i 반복
# if word.count(alpha(i)):
# 그 알파벳값이 있는 원소 인덱스 출력
# for i in range(len(word)):
#     if word[i] in alpha:
#         print(alpha.index(word[i]))
#     else:
#         print("-1")

S = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in S:
        print(S.index(i), end =' ')
    else:
        print(-1, end=' ')

# find() 이용
S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')