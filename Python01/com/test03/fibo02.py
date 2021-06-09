def fibo01(n):
    start = 0
    next_num = 1
    print(start, end = " ")
    while next_num <= n:
        print(next_num, end= " ")
        start, next_num = next_num, start+next_num

        


def fibo02(n):
    list = [0,1]
    i = 0
    while list[i]+list[i+1] <=n:
        list.append(list[i]+list[i+1])
        print(list[i] , i)
        i += 1
    return list

if __name__ == "__main__":
    n = int(input("n : "))
    # 입력된 숫자 만큼 반복 출력
    fibo01(n)
    print()
    # 입력된 숫자 만큼 반복해서 list에 저장하고,
    # list를 리턴
    print(fibo02(n))
