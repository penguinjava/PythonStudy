a = 1
while a<= 20:
    if a % 2 == 0:
        #짝수인 경우 단순히
        a = a + 1
        continue
    else:
        print(a, end=' ')
        a += 1

print()
print("="*30)

dan = 2
while dan<=9 :
    su = 1
    while su<=9:
        
        print("%d*%d=%2d" % (dan,su,su*dan), end=' ')
        su += 1
    dan += 1
    print()

print()
print("="*30)

dan = 2
while dan<=9:
    if dan%2 ==1:
        dan += 1
        continue
    else:
        su = 1
        while su<=9:
            print("%s*%s=%2s" % (dan,su,su*dan), end=' ')
            su += 1
    dan += 1
    print()
print()