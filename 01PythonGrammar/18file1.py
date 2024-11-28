'''
open()
    : 파일을 다룰때 사용하는 내장함수로 첫번째 인자인 file결로
    만 필수사항이고 나머지는 옵션이다.
    형식] open(파일경로, mode,buffering, encoding)

    mode : 파일열기 모드로 w(쓰기), r(읽기), a(추가)가 있고,
        b(2진모드), t(텍스트모드)로 파일의 형식을 지정할 수 있다.
'''

print("="*30)
print("내파일01.txt")
print("="*30)
'''
새로운 파일을 생성하여 반복문으로 내용을 입력한다. wt이므로
쓰기/텍스트 모드로 파일을 오픈한다.
'''
f_open = open("./saveFiles/내파일01.txt",mode='wt', encoding='utf-8')
for i in range(1, 21):
    data = "%d번째 줄입니다.\n" % i
    f_open.write(data)
#반복문을 통해 입력한 후 파일 객체를 닫아준다.
f_open.close()

#파일을 읽기/텍스트 모드로 오픈한다.(만약 파일이 없으면 에러발생됨)
f_read = open("./saveFiles/내파일01.txt",mode='rt',encoding='utf-8')
#파일의 길이를 알수 없으므로 무한루프로 구성
while True:
    #파일의 내용을 한줄씩 읽음
    line = f_read.readline()
    #더 이상 읽을 내용이 없다면 반복문 탈출
    if not line: break
    #내용 출력
    print(line)
#작업을 마쳤다면 자원해제
f_read.close()

#기존 파일에 내용을 추가하기 위해 추가/텍스트 모드로 오픈
f_add = open('./saveFiles/내파일01.txt', mode='at', encoding='utf-8')
f_add.write("추가하는 내용입니다.")
#필요한 경우 개행문자(\n)를 추가해야한다.
f_add.writelines(["줄바꿈은 되나요?\n", "안되면 개행문자를 넣어주세요."])
f_add.write("마지막 라인입니다.")
f_add.close

print("="*30)
print("내파일02.txt")
print("="*30)

#자동으로 파일객체를 open/close 할 수 있게 with~as를 사용한다.
with open("./saveFiles/내파일02.txt", mode='wt',
          encoding='utf-8') as myfile:
    
    #15줄의 문장을 입력하면 자동으로 close 된다.
    for i in range(1,16):
        data = "%d라인 입력합니다.\n" % i
        myfile.write(data)

#앞에서 생성된 파일을 읽기모드로 open한 후 내용을 출력한다.        
with  open("./saveFiles/내파일02.txt",mode='rt',
           encoding='utf-8') as myfile:
    line = None
    while line != '':
        line = myfile.readline()
        print(line.strip('\n'))