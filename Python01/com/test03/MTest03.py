'''
1. for 문을 사용하여 구구단 전체를 출력하는 gugu()라는 함수를 만들자
2. while 문을 사용하는 함수 호출시 입력된 단만 출력하는 gugudan(x)를 만들자
3. main함수에서 gugu()와 gugudan(x) 함수를 호출하되, gugudan에 입력해주는 숫자는 input을 사용하자
'''

def gugu():
    for i in range(2,10):
        for j in range(1,10):
            print(i," * ",j," = ",i*j)


def gugudan(x):
     for j in range(1,10):
            print(x," * ",j," = ",x*j)

if __name__ == "__main__":
    gugu()
    n = int(input("출력하고자 하는 단 : "))
    gugudan(n)