"""
Module to determine which poker hand is the best.
"""

RANK_TO_NUMBER = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

HAND_TYPE_TO_POINTS = {
    "high card": 0,
    "pair": 1,
    "two pairs": 2,
    "three of a kind": 3,
    "straight": 4,
    "flush": 5,
    "full house": 6,
    "four of a kind": 7,
    "straight flush": 9,
    "royal flush": 10
}

def best_hands(hands):
    """Function to determine which poker hand is the winning one.

    Args:
        hands (list): List of poker hands.

    Returns:
        list: The highest poker hands.
    """
    hands_ranking = {}
    best_rank = ()
    for hand in hands:
        hand_rank = check_hand_rank(hand)
        if best_rank < hand_rank:
            best_rank = hand_rank
        hands_ranking[hand] = hand_rank

    return [hand for hand, rank in hands_ranking.items() if rank == best_rank]

def check_hand_rank(hand):
    """Function to determine the value of a given poker hand.

    Args:
        hand (list): List of poker hands.

    Returns:
        tuple: The value of the poker hands.
    """
    result = 0
    ranks = {}
    suits = []

    for card in hand.split(" "):
        suits.append(card[-1])

        if card[:-1] in RANK_TO_NUMBER:
            current_card_rank = RANK_TO_NUMBER[card[:-1]]
        else:
            current_card_rank = int(card[:-1])

        ranks[current_card_rank] = ranks.get(current_card_rank, 0) + 1

    # Checks for flush.
    if "".join(suits) == suits[0]*5:
        result += HAND_TYPE_TO_POINTS["flush"]

    sorted_ranks = sorted(ranks.keys())
    # Checks for flush
    if len(ranks) == 5:
        if sorted_ranks[-1] - sorted_ranks[0] == 4 or sorted_ranks == [2, 3, 4, 5, 14]:
            result += HAND_TYPE_TO_POINTS["straight"]

    # Checks for royal flush.
    if result == HAND_TYPE_TO_POINTS["straight flush"] and sorted_ranks[0] == 10:
        result += 1

    result = (result,)
    if result > (0,):
        return *result, *get_kicker(ranks, is_low_flush= sorted_ranks == [2, 3, 4, 5, 14])


    same_rank_cards_amount = sorted(ranks.values(), reverse=True)

    # Checks for four of a kind.
    if same_rank_cards_amount[0] == 4:
        return HAND_TYPE_TO_POINTS["four of a kind"], max(ranks, key=ranks.get), min(ranks, key=ranks.get)

    # Checks for full house.
    if same_rank_cards_amount == [3, 2]:
        return HAND_TYPE_TO_POINTS["full house"], max(ranks, key=ranks.get), min(ranks, key=ranks.get)

    # Checks for three of a kind.
    if same_rank_cards_amount[0] == 3:
        result = HAND_TYPE_TO_POINTS["three of a kind"], max(ranks, key=ranks.get)

    # Checks for types of pairs.
    pairs = [rank for rank, amount in ranks.items() if amount == 2]
    if pairs:
        result = (len(pairs) * HAND_TYPE_TO_POINTS["pair"],)

    for pair in sorted(pairs, reverse=True):
        result += (pair,)

    # returns the three of a kind, two pairs, pairs and high cards with kickers.
    return *result, *get_kicker(ranks)

def get_kicker(ranks, is_low_flush=False):
    """Function to find the kickers of a given poker hand.

    Args:
        ranks (list): List of the poker hand cards ranks.
        is_low_flush (bool): Determine whether it's a low flush or not. (for calculating the 'ace').

    Returns:
        tuple: The kickers of the given poker hand.
    """
    result = tuple()
    for kicker in sorted([rank for rank, amount in ranks.items() if amount == 1], reverse=True):
        if is_low_flush and kicker == 14:
            result += (1,)
        else:
            result += (kicker,)
    return result