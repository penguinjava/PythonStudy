#입력받은 숫자를 실수형으로 변환하여 변수에 저장
num1 = float(input("첫번째 숫자를 입력하세요:"))
num2 = float(input("두번째 숫자를 입력하세요:"))

#3, 4를 입력했다고 가정하면..

#관계연산자
result1 = num1 == num2
print("같은지 비교", result1) #False

result2 = num1 != num2
print("다른지 비교", result2) #True

result3 = num1 >= num2 #False
print("큰지 비교", result3)

result4 = num1 < num2 #True
print("작은지 비교", result4)

result5 = not (num1 > num2) #True
print("관계식 판단의 부정", result5)

#논리연산자
logical1 = result1 and result2 #F and T ==> False
logical2 = result3 or result4 #F or T ==> True
logical3 = not (result3 or result4) #not( True ) ==> False

print('logical1',logical1)
print('logical2',logical2)
print('logical3',logical3)