number = (input(f'Enter a number: '))

def count_something():
    even_counter = 0
    odd_counter = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
        n //= 10
    return {
        'odd': odd_counter,
        'even': even_counter
    }

print(count_something(number))
