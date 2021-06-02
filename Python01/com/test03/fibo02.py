def fibo01(n):
    start = 0
    next_num = 1
    print(start, next_num, end=" ")
    for i in range(1, n):
        start, next_num = next_num, start + next_num
        print(next_num, end=" ")


def fibo02(n):
    list = [0,1]
    for i in range(0, n):
        list.append(list[i]+list[i+1])
    return list

if __name__ == "__main__":
    n = int(input("n : "))
    # 입력된 숫자 만큼 반복 출력
    fibo01(n)
    print()
    # 입력된 숫자 만큼 반복해서 list에 저장하고,
    # list를 리턴
    print(fibo02(n))
