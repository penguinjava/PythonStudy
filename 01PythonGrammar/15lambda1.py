'''
람다(lambda)
    :def 키워드를 사용하지 않고, 식 형식으로 되어있다해서
    람다식이라고 부른다. 이름이 없으므로 익명함수로 부르기도한다.
    lambda 키워드를 사용하여 간편하게 작성할 수 있고, 재사용되지
    않는 1회성 함수를 만들때 사용한다.
'''
# 일반 함수 정의
def two_sum(x,y):
    return x + y
print("함수를 통한 두수의 합=", two_sum(10,20))

# 람다식 정의
'''
형식] 람다식이름 = lambda 매개변수1~N : 실행문장
'''
sum = lambda arg1, arg2: arg1 + arg2
print("람다식을 통한 합=", sum(10,20))

sum = lambda arg1, arg2: arg1 + arg2
print("람다식을 통한 합=", sum(10,20))

power = lambda num : num**2
print("5의 제곱은=", power(5))

# 람다식 자체 호출
# : 람다식을 변수에 할당하지 않고, 괄호를 이용해서 식 자체를 호출할 수 있다.
print("람다식 자체호출=", (lambda x,y: x+y)(100,200))