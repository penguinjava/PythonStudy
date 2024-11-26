'''
for문
    형식] for 본복변수 in 목록형:
        실행문
    range()함수
        :반복문과 직접적인 연관은 없지만 흔히 반복문과
        연동해서 자주 사용하는 함수
        형식]
            range(10) : 0~9까지
            range(2,10) : 2~9까지
            range(2,10,2) : 0~9까지 2씩 증가

'''
for i in range(5):
    print("i=", i, end=" ")

print()
print("="*30)

list1 = [1,2,3,4,5,6,7,8,9,10]
#for문에 리스트를 사용
sum = 0
#리스트의 원소 갯수만큼 10번 반복
for i in list1:
    #원소를 누적해서 합산
    sum += i
print("1부터 10까지의 합 = ",sum)

print()
print("="*30)

#문자열의 크기만큼 반복
str1 = "파이썬이좋아요"
for ch in str1:
    #문자 사이에 공백을 추가하여 출력
    print(ch, end=" ")

print()
print("="*30)

for dan in range(2,10):
    for su in range(1,10):
        print("%2d *%2d = %2d" %(dan,su,su*dan), end=' ')
    print()

'''
for문도 else구문을 사용할 수 있다.
단, for문이 정상적으로 종료되었을때 만 실행
'''
for i in range(3):
    print(i, end=" ")
else:
    print("for문 종료됨")

print()
print("="*30)
'''
for문이 딱 한번만 실행된 후 탈출하게되므로 else는
실행되지 않음
'''
for i in range(3):
    print(i, end=" ")
    break
else:
    print("break를 통해 for문이 완료되지 않았으므로 출력되지 않음") 

print()
print("="*30)