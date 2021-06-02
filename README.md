# PythonStudy
## 1일차
dictionary

-> {} key : value 로 이루어짐

범위 연산

-> range(n) : 0 <= n

->[start: end] -> start ~ end - 1

->[start: end: step] -> start ~ end-1 까지 step 만큼 증가

Regular Expression

. : 문자 1개

^ : 문자열의 시작

$ : 문자열의 마지막

[] : 문자 집합

| : OR

() : 괄호 안의 정규식 그룹

* : 0 or more

+ : 1 or more

? : 0 or 1

{n} : n번 반복

{n,m} : n번 부터 m번

{n, } : n번 부터 무한번

r  문자열 표기법 (re 모듈의 확장 문법)

\w : [a-zA-Z0-9_] : a~z,A~Z,0~9,_를 포함하는 모든 문자

\W : [^a-zA-Z0-9_] : 위의 문자들을 제외한 나머지

\d : [0-9] : 0 부터 9

\D : [^0-9] : 숫자를 제외한 나머지

\s : [\t\n\r\f\v] : 공백문자

\S : [^\t\n\r\f\v] : 공백문자 제외한 나머지

\b : 단어의 시작과 끝의 빈 공백

\B : 단어의 시작과 끝이 아닌 빈 공백

\\ : \

\[숫자] : 지정된 숫자만큼 일치하는 문자열

\A : 문자열의 시작

\Z : 문자열의 끝

if , for ,while 을 적용하기 위해서는 space 2 , space 4 , 1tab을 해야만 함 

파이썬 개발자는 space 4를 권장

## 2일차
-*- coding:utf-8 -*-
python 에서의 인코딩 방법!

__변수__ : 내부적으로 사용하는 변수

pip install numpy -> 수치해석,숫자,행렬 ...
pip install matplotlib -> 시각화 (그래프)

파일 옵션
'''
r : 읽기
w : 쓰기 (기존 내용 덮어쓰기)
a : 쓰기 (기존 내용 이어서쓰기)
x : 새로운 파일 만들어서 쓰기
t / b : text / binary (default : t)
'''

크롤링

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn')
soup = BeautifulSoup(resp,'html.parser')

-> 해당 정보를 가지고 옴

find() -> 해당 태그를 통해서 값을 찾을 수 있음
