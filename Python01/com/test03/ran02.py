import random

# 1 ~ 45 사이의 중복되지 않는 6개 숫자를 출력하자
def lotto():
    list = [];
    while(len(list) != 6):
        num = random.randint(1, 45)
        if(num not in list):
            list.append(num)
        
    return list

if __name__ == "__main__":
    print(lotto())