"""
Module to Determine the fewest number of coins to give a customer so that the sum of their values equals the correct amount of change.
"""
def find_fewest_coins(coins, target):
    """Function to determine the amount of change to give based on the given change amount and coins to uses.

    Args:
        coins (list): The coins we can use to give change with.
        target (int): The target amount of change to give.

    Returns:
        list: List of coins to give to the customer.
    """
    if not target:
        return []
    if target < 0:
        raise ValueError("target can't be negative")

    coin_amount = 1
    while True:
        combinations = sorted([(sum(combination), combination) for combination in find_combinations(coins, coin_amount)])

        if combinations[0][0] > target:
            raise ValueError("can't make target with given coins")

        for combination in combinations:
            if combination[0] == target:
                return combination[1]
            elif combination[0] > target:
                continue

        coin_amount += 1

def find_combinations(coins, amount):
    """Recursive Function to find all possible combinations for a given set of coin types and amount of coins to use.

    Args:
        coins (list): The coins we can use to give change with.
        amount (int): The amount of coins we are recivred to use for each combination.

    Returns:
        list: List of all possible combinations.
    """
    if amount <= 1:
        return [[coin] for coin in coins]

    return [[coins[coin_index]] + combination
            for coin_index in range(len(coins))
            for combination in find_combinations(coins[coin_index:], amount - 1)]