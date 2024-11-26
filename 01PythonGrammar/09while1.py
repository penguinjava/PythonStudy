'''
반복문
: 파이썬에서의 반복문은 while문과 for문만 있다.
형식]
    초기값
    while 조건문:
        수행할문장
        증감식
    else:
        정상 종료되었을때 진입

단, while문이 완료되지 않은 상태로 탈출하게되면 else구문으로
진입할 수 없다.
'''

treeHit = 0

while treeHit <10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다."%treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

print()
print("="*30)

#파이썬에서는 문장열도 조건식으로 사용할 수 있다.
str = 'python'
#str이 공백이 될때까지 반복, 공백이 아니라면 True.
while str:
    #출력문 끝에 공백을 추가하여 줄바꿈없이 출력
    print(str, end=' ')
    '''
    인덱스 1부터 마지막까지를 슬라이싱한다.
    문자열에서 첫글자를 제거한 후 다시 대입한다.
    '''
    str = str[1:]

str2 = 'python'
while str2:
    print(str2, end=' ')
    str2 = str2[0:-2]

print()
print("="*30)

sum = 0
i = 1
while i<=10:
    sum+= i
    if i<10:
        print(i,end=" + ")
    else:
        #반복의 마지막에는 =을 출력
        print(i, end=" = ")
    i += 1
else:
    #while문이 종료되면 else구문이 실행되어 합의 결과를 출력
    print(sum)

print()
print("="*30)

coffee = 10
while True:
    print("커피 한전을 판매합니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." %coffee)
    
    #판매완료 조건이 되었을 때 break를 통해 while문 타출
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

print()
print("="*30)

import random
#새로운 Set을 생성
lotto = set()
#무한루프 조건으로 while문 생성
while True:
    #1~45사이의 난수 생성
    rndNum = random.randint(1,45)
    #생성된 난수는 Set에 추가(중복은 자동으로 제거됨)
    lotto.add(rndNum)
    #Set의 크기, 즉 6개의 요소가 모두 채워졌다면, while문 탈출
    if len(lotto) == 6:
        break

#오름차순으로 정렬해서 출력
print("로또번호", sorted(lotto))