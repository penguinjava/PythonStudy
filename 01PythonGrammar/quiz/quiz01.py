'''
문제 1: 숫자의 합 구하기
사용자로부터 양의 정수를 입력받아 각 자릿수의 합을 계산하는 함수를 작성하세요.
함수 이름: sum_of_digits
입력: 정수 n (예: 1234)
출력: 각 자릿수의 합 (예: 10)
'''
def sum_of_digits(str):
    sum = 0
    for s in str:
        sum +=int(s)
    print(sum)


if __name__=="__main__":
    
    sum_of_digits(input("숫자를 입력하세요."))