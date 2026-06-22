"""
Module to the Nth prime.
"""

def prime(number: int):
    """Function returns the prime number with a given position

    args:
        number (int): the N of the desired prime number

    returns:
        int: prime number with the given n

    raises:
        ValueError: if the given number is less than 1
    """
    if number < 1:
        raise ValueError('there is no zeroth prime')

    primes = []

    candidate = 1
    while len(primes) < number:
        candidate += 1
        is_prime = True

        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(candidate)

    return candidate