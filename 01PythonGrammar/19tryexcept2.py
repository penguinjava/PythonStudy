print('실행6')
try:
    x=int(input('3의 배수를 입력하세요: '))
    #사용자가 입력한 숫가가 3의 배수가 아닌경우 예외를 발생시킴
    if x % 3 != 0:
        raise Exception('[예외메세지] 3의 배수가 아님')
    print(x)
except Exception as e:
    print('예외가 발생했습니다.')

print('실행7')
'''
사용자지정 예외 클래스 만들기
: 예외클래스를 정의 할때 Exception 클래스를 상속하고
생성자에서 예외발생시 출력할 메세지를 정의한다.
'''
class GugudanRangeExcept(Exception):
    #생성자
    def __init__(self):
        #부모클래스인 Exception클래스의 생성자를 호출
        super().__init__('구구단의 범위를 벗어났습니다')

#매개변수로 전달된 숫자만큼의 구구단을 출력하는 함수
def print_gugudan(end_num):
    try:
        if end_num > 9:
            #9를 초과하는 경우 정의한 클래스를 이용해서 예외
            #발생시킨다.
            raise GugudanRangeExcept
        #range()함수는 항상 미만까지만 반복하므로 1을 더해준다.
        end_su = end_num + 1
        for dan in range(2,end_su):
            for su in range(1,10):
                #하나의 단을 줄바꿈없이 출력
                print("%d * %d = %2d" % (dan, su, dan*su),end=' ')
            #단이 완료되면 줄바꿈 처리
            print()
        print()
    except Exception as e:
        print('예외발생',e)

print_gugudan(int(input("출력할 단 수를 입력하세요 : ")))