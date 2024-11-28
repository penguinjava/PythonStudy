'''
문제 3: 소수 판별하기
입력받은 정수가 소수(Prime Number)인지 확인하는 함수를 작성하세요.
(소수: 1과 자기 자신만으로 나누어지는 1보다 큰 정수)
함수 이름: is_prime
입력: 정수 n (예: 7)
출력: True 또는 False
'''

def is_prime(prime):

    n = 2
    if prime<=1:
        print("소수가 아닙니다.")
        return
    else:
        while n**2<=prime:
            if prime % n == 0:
                print("소수가 아닙니다.")
                break
            n+=1
        else:
            print("소수입니다.")


if __name__=="__main__":

    is_prime(int(input("소수를 적으세요 : ")))