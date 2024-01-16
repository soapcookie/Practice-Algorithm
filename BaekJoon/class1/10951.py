#예외 발생 시 종료
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
#예외 발생 시 error 출력 후 종료
while True:
    try:
        a,b = map(int, input().split())
    except:
        print('error')

#예외 발생 시 error 출력 후 반복
try:
    while True:
        a,b = map(int, input().split())
        print(a+b)
except:
    print('error')