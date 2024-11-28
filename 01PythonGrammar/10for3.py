'''
시나리오] 연월일을 입력해서 요일 구하는 프로그램을 작성하시오.
#윤년추가규칙 : 지구의 공전주기가 365.2422 이므로 이를 보정하기위한 수식이다.
-4로 나누어 떨어지는 해는 윤년, 그 밖의 해는 평년으로 한다.
-4로 나누어 떨어지지만 100으로도 나누어 떨어지는 해는 평년으로 한다.
-단, 400으로 나누어 떨어지는 해는 윤년으로 한다.(예: 2000년, 2400년)
'''

#숫자형으로 연/월/일을 입력 받는다.
year = int(input("년도를 입력하시오:"))
month = int(input("월을 입력하시오:"))
day = int(input("일을 입력하시오:"))

#서기 1년 1월 1일부터 입력한 날짜까지를 누적하기 위한 변수
total_days = 0
'''
월별 날짜수를 리스트로 정의. 1월을 인덱스로 1로 사용할기
위해 첫번째 요소는 0으로 설정
'''
year_month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

#입력한 이전년도(작년)까지의 전체날짜를 누적해서 더함
for d  in range(1,year):
    if d % 400 == 0: # 400으로 나눠지면 윤년
        total_days = total_days + 366
    elif d % 100 ==0: #100으로 나눠지면 평년
        #4로 나눠지면 윤년
        total_days = total_days + 365
    elif d % 4==0:
        total_days = total_days + 366
    else:
        total_days = total_days +365

'''
입력 년도의 각 월의 날짜수를 누적해서 더해준다. 만약 1월을 입
력했다면 해당 for문은 실행되ㅣ 않는다.
'''
for m in range(1, month):
    total_days = total_days + year_month_days[m]
'''
입력월이 3이상이고, 입력년도가 윤년인 경우 1을 더해줘야한다.
윤년은 2월 29일까지 있기때문이다. 만약1,2월을 입ㄹ
'''
if month >= 3:
    if year % 400 == 0:
        total_days == total_days + 1
    elif year % 100 == 0:
        total_days = total_days + 0
    elif year % 4 == 0:
        total_days = total_days + 1
    else:
        total_days = total_days + 0

#마지마긍로 내가 입력할 날짜를 합산했ㄷ=
total_days += day
print()
print("total_days", total_days)
remainder = total_days % 7

'''
서기 1년1월1일은 월요일이므로 7로 나눈 나머지를 통해 요일을
판단할 수 있다. 나누어 떨어지면 일요일, 1이 남으면 월요일이된다.
'''
if remainder == 0:
    print("일요일입니다.")
if remainder == 1:
    print("월요일입니다.")
if remainder == 2:
    print("화요일입니다.")
if remainder == 3:
    print("수요일입니다.")
if remainder == 4:
    print("목요일입니다.")
if remainder == 5:
    print("금요일입니다.")
if remainder == 6:
    print("토요일입니다.")