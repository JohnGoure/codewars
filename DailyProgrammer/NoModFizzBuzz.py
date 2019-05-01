def fizzBuzz(num):
    for x in range(1, num + 1):
        if (((x // 3) * 3) // 5) * 5 == x:
            print('FizzBuzz')
        elif (x // 3) * 3 == x:
            print('Fizz')
        elif (x // 5) * 5 == x:
            print('Buzz')
        else:
            print(x)

fizzBuzz(100)
