n = int(input('input n : '))

# 피보나치 수열 : 1 1 2 3 5 8 13 21 34 55 89 ...
start = 1
next_num = 1
print (start,end= " ")
print (next_num, end= " ")
for i in range(1,n):
    print(start + next_num, end=" ")
    start , next_num = next_num , start + next_num
