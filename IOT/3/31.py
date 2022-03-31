import random
secret = random.randint(1, 99);
guess = 0
tries = 0
print('숫자를 알아맞춰보세요!')
print('숫자는 1부터 99까지입니다. 기회는 6번 드립니다.')
while guess != secret and tries < 6:
    guess = int(input('숫자를 입력하세요 : '))
    if guess < secret:
        print('Too low!!')
    elif guess > secret:
        print('Too high')

    tries = tries + 1

if guess == secret:
    print("맞췄네요!!")
else:
    print('아쉽네요, 기회가 끝났습니다.')
    print('숫자는 {} 입니다.'.format(secret))