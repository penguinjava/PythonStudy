#표준 입출력 장치

#3개의 변수 생성 및 초기화
i, j, k = 7,8,9
#출력값 사이에 스페이스가 하나씩 추가된다.
print(i,j,k)
#출력값 사이에 스페이스가 하나씩 추가된다.
print(i,j,k,sep='-')
#값을 줄바꿈 없이 출력할 수 있다.
print(i,j,k,end=', ')
print(i,end=', ')
print(k)

#format 함수
#실수 출력시 전체8자리, 소수3자리 표현
print("원주율 =",format(3.14159, "8.3f"))
#정수 출력시 전체 10자리
print('맥주 =',format(5000, "10d"))
#정수 출력시 세자리마다 컴마 표시
print('노트북 =',format(1580000, "3,d"))

#서식문자 : 문자열%s, 정수 %d, 실수 %f
name = "성유겸"
age = 13
price = 123.456
print("이름 : %s,  나이 : %d, 용돈 : %.2F % (name, age, price)")

#format()함수 : 인덱스 혹은 변수명을 지정하여 출력.
#변수명 = "값" 과 같이 디폴트값을 지정할 수 있다.
menu1 = "치킨"
menu2 = "맥주"
print("오늘 {str}은 {0}로 {1}로 정했다"
      .format(menu1,menu2,str="저녁"))
print("오늘 {str}과 {0}로 {1}을 시작하겠다"
      .format(menu1,menu2,str="아침"))

#입력받기 : 키보드를 통해 입력받는 값은 항상 '문자형(str)'이된다.
num = input('숫자를 입력하세요 : ')
print('입력한 숫자는 ', num,'이고, 타입은', type(num))

#문자+숫자 => 에러발생
# result_error = num +10
#연산을 위해 정수형으로 변환 후 처리할 수 있다.
result1 = int(num)+10
print('덧셈결과', result1)

#입력 및 정수변환 : 일반적으로 동시에 처리한다.
result2 = int(input('숫자1 : ')) *int(input('숫자2 : '))
print('곱셈결과', result2)

#실수변환
result3 = float(input('원주율 : ')) *\
    (float(input('원의반지름 : ')) ** 2)
print("원의넓이", result3)