total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
        print(i, end='+')
print('\b','=',total)

print()
print("="*30)

'''
List Comprehension
'''

lit = [n** 2 for n in range(10) if n%3==0]
print(list)

print()
print("="*30)