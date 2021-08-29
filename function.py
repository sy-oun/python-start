# 함수
# 팩토리얼명령이란걸알려줄게, 내가 팩토리얼이라하면 그 명령을 수행하면돼

def factorial(number):
    count = number -1
    while count >= 2:
        number = number * count
        count = count - 1
    return number

print(factorial(21))
print(factorial(13))
print(factorial(8))

def say_hello():
    print("안녕!")
    print("hello!")
    print("bonjour!")

say_hello()
say_hello()
say_hello()
