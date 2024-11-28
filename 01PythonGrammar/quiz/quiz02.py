'''
문제 2: 팰린드롬 문자열 확인
주어진 문자열이 팰린드롬인지 확인하는 함수를 작성하세요.
(팰린드롬: 앞뒤가 똑같은 문자열, 예: "level", "radar")
함수 이름: is_palindrome
입력: 문자열 s (예: "radar")
출력: True 또는 False

'''
def is_palindrome(str):
    re = str[::-1]
    if str==re:
        print(True)
    else:
        print(False)


if __name__=="__main__":
    is_palindrome(input("팰린드롬을 적으세요 : "))