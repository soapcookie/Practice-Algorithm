# word = input() //단어 입력받기
# words = list(word.apper()) // 입력받은 단어를 대문자로 리스트에 넣기
#
# 각 리스트의 같은 원소 구하기
# words[i][0:]]  ?
#
# 같은 원소 개수는 cnt에 저장
# cnt +=
# 같은 원소가 있을 때마다 cnt값 증가
#
# cnt값이 가장 많았던 원소 출력
# print(max(cnt)))?
#
# 예외
# 가장 많은 cnt값을 가진 원소가 2개 이상이라면 ? 출력
# if cnt >=2:
# print("?")

words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])