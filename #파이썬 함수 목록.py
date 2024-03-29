
#파이썬 함수 목록

# 1. 내장함수
num = 527
word1 = '소이지'
word2 = 'Soeasy'

abs() # -> 절대값을 얻기위해 사용하는 함수

all() # -> all(iterable)함수는 iterable의 "모든 요소"가 참(True)이면 
      #    (또는 iterable이 비어있으면) True 값을 반환한다.

      #    *** 
      #    iterable이란 의미는 "반복 가능한 것"을 의미하며,
      #    반복가능한 데이터의 종류는 다음과 같다.
      #    >> 순서형 및 컬렉션 자료형 등등

any() # -> any(iterable)함수는 iterable의 요소 중 "어느 하나"라도
      #    참(True)이면 True 값을 반환한다.
      #    iterable이 비어있다면 False를 값을 반환한다.

ascii() # -> ascii(아스키)는 미국 정보교환 표준 부호(American Standard 
        #    Code for information interchange)의 줄임말이다.
        #    아스키코드는 기호와 영문알파벳에 적합한 문자 인코딩이다.

        #    + 추가 정보)
        #    아스키코드가 영문알파벳과 기호에 적합한 이유는 7비트
        #    인코딩이기 때문이다. 7비트 인코딩으로 표현 가능한 것은 0부터
        #    127까지 총 128개로 그 범위 안에 할당된 값은 기호와 영문알파벳이
        #    해당된다. 한글과 같이 크기가 큰 문자는 인코딩 하기에 적합하지
        #    않은 것.

        #    ***
        #    문자열이나 기호를 컴퓨터에서 사용하기 위해서는 "코드화,부호화"
        #    하는 "인코딩" 과정을 거쳐야한다.

bin() # -> bin(x)함수는 매개변수 x에 정수 값을 입력 받아서 2진수로 변환하여,
      #    변환한 값을 반환하는 함수이다.

      #    ***
      #    데이터 타입은 10진수로 표현된 integer값을 2진수로 바꿔서
      #    "문자열" 타입으로 변환한다. 즉, 반환형은 문자열(string)타입이다.

bool() # -> bool(x) 함수는 매개변수 x에 값을 입력 받아서 True 또는 False로
       #    반환하는 함수이다.
       #    x에 0을 제외한 어떤 값이 입력된다면

breakpoint() # -> Python 3.7부터 추가된 built-in(내장)함수로 이 함수를
             #    사용하면 프로그램이 멈추고 interactive debugger를 실행
             #    하면서 코드를 살펴볼 수 있다.

             #    ***
             #    interactive debugger란?
             #    *** 추가 정보 및 주석 필요 ***--------------------

bytearray() # -> 1바이트 단위의 값을 저장하는 자료형이다. byte와 다른 점은
            #    값의 수정이 가능하다.또한 bytearray는 다양한 형태로 활용
            #    가능하다.
            #    bytearray() : 빈 바이트 배열 객체를 생성
            #    bytearray(길이) : 해당 길이만큼 0으로 채운 byte형
            #                     배열을 생성
            #    bytearray(리스트) : 전달받은 리스트를 바이트 배열로
            #                       만들어서 객체를 생성
            #    bytearray(b'문자열') : 문자열을 바이트배열 객체로 생성

bytes() # -> 
callable()
chr()
classmethod()
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate()
eval()
exec()
filter()
float()
format()
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
input()
int()
isinstance()
issubclass()
iter()
len()
list()
locals()
map()
max()
memoryview()
min()
next()
object()
oct()
open()
ord()
pow()
print()
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()
__import__()