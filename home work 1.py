n = int(input('Input a number of digits'))

once = n % 10

n = n // 10

tens = n % 10

n = n // 10

result = n + tens + once
print(result)
