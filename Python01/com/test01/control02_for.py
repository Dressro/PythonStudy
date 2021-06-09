subject = ['java','javascript','python']

for s in subject:
    print(s,end=' ')
else:
    print('재밋다.')

for i in range(1,100):
    print(i, end = ' ')
    
print()
print("-----------------------------------")

for i in range(2,10):
    print(str(i) + "단")
    for j in range (1,10):
        print(i," * ", j," = " ,i*j)
    print("-----------------------------------")
    
# range 함수 사용 해서 10 ~ 1 까지 거꾸로 출력
for i in range(10,0,-1):
    print(i)
    
a = set(['1','2','3','a','b','c'])

b = {'a','b','c','d','e','f'}

print(a.intersection(b))