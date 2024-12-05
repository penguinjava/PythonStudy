data ={
    '성명' : [],
    '전화번호' : [],
    '주소' :[]
}
#딕셔너리 key value[]

def loop():
    while True:
        print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
        num = int(input("선택 : "))

        if num == 1:
            print(f"{'[ 1번 입력 ]':-^50}")
            name = input("성명 → ")
            data['성명'].append(name)
            phone = input("전화번호 → ")
            data['전화번호'].append(phone)
            address = input("주소 → ")
            data['주소'].append(address)
                
        elif num == 2:
            print(f"{'[ 2번 출력 ]':-^50}")
            nameVar = data['성명']
            numVar = data['전화번호']
            adVar = data['주소']
            print(f"{'성명':<5} {'전화번호':<10} {'주소':<10}")
            print("-" * 50)
            for name,num,addr in zip(nameVar,numVar,adVar):
                print(f"{name:<10} {num:<10} {addr:<10}")

        elif num == 3:
            print(f"{'[ 3번 검색 ]':-^50}")
            search = input("검색하실 성명을 입력하세요 → ")
            var = data['성명']
            count = 0
            for v in var:
                if v == search:
                    print(f"{'성명':<5} {'전화번호':<10} {'주소':<10}")
                    print("-" * 50)
                    print(f"{data['성명'][count]:<5} {data['전화번호'][count]:<10} {data['주소'][count]:<10}")
                    break
                else:
                    count += 1

        elif num == 4:
            print(f"{'[ 3번 검색 ]':-^50}")
            search = input("검색하실 성명을 입력하세요 → ")
            var = data['성명']
            count = 0
            for v in var:
                if v == search:
                    data['성명'][count] = input("변경할 이름 입력 → ")
                    data['전화번호'][count] = input("변경할 전화번호 입력 → ")
                    data['주소'][count] = input("변경할 주소 입력 → ")
                    break
                else:
                    count += 1

        elif num == 5:
            print(f"{'[ 5번 삭제 ]':-^50}")
            search = input("검색하실 성명을 입력하세요 → ")
            var = data['성명']
            count = 0
            for v in var:
                if v == search:
                    del data['성명'][count]
                    del data['전화번호'][count]
                    del data['주소'][count]
                    break
                else:
                    count += 1

        else:
            print(f"{'[ 6번 종료 ]':-^50}")
            print("종료하였습니다!")
            break


if __name__=="__main__":
    
    try:
        loop()
    except Exception as e:
        loop()
    
