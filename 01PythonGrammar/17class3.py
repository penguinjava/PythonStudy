'''
멤버변수의 정보은닉은 위해 private 대신 __를 사용
한다. 정보은닉이란 멤버변수의 외부 접근을 차단하고,
클래스 내부에서만 접근하도록 처리하는 것을 말한다.
'''

class Compiter:
    # 생성자
    def __init__(self, name, passwd):
        #외부 접근 허용(public)
        self.name = name
        #외부 접근 차단(private): 변수 앞에 __를 추가한다.
        self.__passwd = passwd
    def hitkeyboard(self):
        return f'{self.name}로 키보드 작업을 합니다.'
    def clickMouse(self):
        print(f'{self.name}에서 마우스로 클릭합니다.')

    #정보은닉 처리된 멤버변수의 접근을 위한 getter/setter메서드 정의
    def getPasswd(self):
        return self.__passwd
    def setPasswd(self, passwd):
        self.__passwd = passwd

#인스턴스 생성
myCom = Compiter('LG Gram', 'qwer1234')

#멤버메서드 호출
print(myCom.hitkeyboard())
myCom.clickMouse()

print("컴퓨터이름",myCom.name)
# print(myCom.__passwd)

#private이므로 접근할 수 없어 에러 발생
#따라서 getter를 통해 접근 후 출력해야 한다.
print('패스워드',myCom.getPasswd())

#변경을 위해 setter를 호출
myCom.setPasswd('abcd9876')
print('패스워드 변경후1',myCom.getPasswd())

'''
맹글링 규칙에 의해 정보은닉 처리된 멤버변수는
이름이 변경되므로 아래와 같이 작성했을 때
값을 변경할 수 없다.
'''
myCom.__passwd = "xxxxXXXX"
print('패스워드 변경후2',myCom.getPasswd())

#권장되지 않음
#print("맹글링규칙", myCom._Computer__passwd)