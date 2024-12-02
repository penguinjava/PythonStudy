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
            print(data)

        elif num == 3:
            print(f"{'[ 3번 검색 ]':-^50}")
            search = input("검색하실 성명을 입력하세요 → ")
            count = 0
            val[count] = data['성명']
            numVal[count] = data['전화번호']
            adVal[count] = data['주소']
            
            data2 = {
                '성명'
            }
            for v in val:
                if search == v:
                    print()
                    break
                else:
                    count+=1

        elif num == 4:
            print(f"{'[ 4번 수정 ]':-^50}")
            search = input("수정하실 성명을 입력하세요 → ")
            count = 0
            val = data['성명']
            for v in val:
                if search == v:
                    print(pd.DataFrame(data).iloc[count].to_string())
                    break
                else:
                    count+=1

        elif num == 5:
            print(f"{'[ 5번 삭제 ]':-^50}")


        else:
            print(f"{'[ 6번 종료 ]':-^50}")
            print("종료하였습니다!")
            break


if __name__=="__main__":
    
    try:
        loop()
    except Exception as e:
        loop()
    
