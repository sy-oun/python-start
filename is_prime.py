#소수판별프로그램
# 1과 그 자신만을 약수로 가지는 수
# 17 2 ~ 16

def is_prime(number):
    count = 2
    while count < number:
        print (count)
        if number % count == 0:
            print("소수가 아닙니다.")
            break #명제가 참이아니어도 만나면 강제로
        count = count+1

is_prime(25)
