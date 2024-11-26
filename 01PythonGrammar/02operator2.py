#대입 연산자
a = tot = 10

b = c = d = 30
print(b)
print(id(b))
print(c)
print(id(c))
print(d)
print(id(d))

#복합 대입 연산자
#좌측의 a에 1이 합산되어 11이 됨
a += 1
#10 + 11의 결과가 tot에 할당됨
tot += a
print(a, tot)

#최초 100, 200이 할당
v1, v2 = 100, 200
v2, v1 = v1, v2
#교체후에는 200,100이 할당됨
print('변수교체', v1, v2)
'''
알고리즘에서 정렬을 위해 사용한 Swap(스왑) 기능을 위와같이
간편하게 구현할 수 있다.
'''

# 5개의 값을 저장한 List를 선언 후 초기화
mylist = [1,2,3,4,5]

# x1는 1이 할당되고, 나머지는 *x2에 할당된다.
x1, *x2 = mylist
print('패킹연산자1', x1, x2)

*y1, y2, y3 = mylist
print('패킹연산자2',y1,y2,y3)