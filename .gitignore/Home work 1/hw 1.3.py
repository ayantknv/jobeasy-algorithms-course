# Count odd and even numbers
m = int(input('input number '))

def count_odd_even(m):
    even_counter = 0
    odd_counter = 0
    while m > 0:
        digit = m % 10
        if digit % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
        m //= 10
    return {
        "odd": odd_counter,
        "even": even_counter
    }
print(count_odd_even(m))