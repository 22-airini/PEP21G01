def primes(max_prime):
    _my_primes = []

    for number in range(1, max_prime + 1):
        if number < 3:
            _my_primes.append(number)
            continue
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            _my_primes.append(number)
    return _my_primes

###

def encrypted(text,number=144):
    my_list = []
    for letter in text :
        my_letter = chr(ord(letter).__xor__(number))
        my_list.append(my_letter)
    result = "".join(my_list)
    return result


print(encrypted(text))
