# 산술연산
a = 21
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a ** b)  # a^b
print(a / b)
print(a // b)  # 몫 (floor division - 소수점 이하는 버린다.)
print(a % b)

# 비교연산
a, b = 5, 3

print (a == b)
print(a != b)
print(a > b)
print(a <= b)
print(a is b)
print(a is not b)

print(True or True)
print(True or False)

# 범위 연산
# range(n) : 0 <= n
list01 = list(range(100))
print(list01)

print(list01[2])        # 2
print(list01[12:49])    # 12 ~ 48
print(list01[12:49:3])  # 12 ,15 ,18, 21 ...

# [start: end] -> start ~ end - 1
# [start: end: step] -> start ~ end-1 까지 step 만큼 증가

str01= "Hello, World!"
print(str01)
print(str01[0:5])
print(str01[:5])
print(str01[7:])
print(str01[7:12])
print(str01[:4]*3)

#reverse
print(str01[-1])
print(str01[-6:])
print(str01[:-1])
print(str01[::-1])

# 멤버 연산
list02 = [0,1,2,3,4]
print(3 in list02)
print(5 in list02)
print(5 not in list02)

