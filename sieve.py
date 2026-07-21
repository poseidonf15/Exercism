"""
Module to find all the prime numbers up to a given number using the 'Sieve of Eratosthenes' algorithm.
"""
def primes(limit):
    """Function to return all the prime numbers up to a given number using the 'Sieve of Eratosthenes' algorithm.

    Args:
        limit (int): The limit number.

    Returns:
        list: All the prime numbers up to the limit.
    """
    candidates = [num for num in range(2,limit+1)]

    for index in range(int(limit ** 0.5) - 1):
        number = candidates[index]
        if number:
            for marking_index in range(index + number,len(candidates),number):
                candidates[marking_index] = False

    return [prime for prime in candidates if prime]