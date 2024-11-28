'''
문제 4: 문자열 단어 개수 세기
주어진 문자열에서 공백으로 구분된 단어의 개수를 세는 함수를 작성하세요.

함수 이름: count_words
입력: 문자열 s (예: "hello world python")
출력: 정수 (단어 개수)
'''

def count_words(str):
    list = str.strip().split(" ")
    count = 0

    for s in list:
        if(s==""):
            continue
        count+=1
    print(count)


if __name__=="__main__":

    count_words(input("문자를 입력하세요 : "))