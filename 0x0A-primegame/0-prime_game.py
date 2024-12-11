#!/usr/bin/python3
"""
Prime Game Problem: Optimized Solution for Maria and Ben's Game
"""


def sieve_of_eratosthenes(n):
    """
    Efficiently generate prime numbers up to n using Sieve of Eratosthenes
    Args:
        n (int): Upper limit for generating primes
    Returns:
        list: Primes numbers up to n
    """
    # Initialize boolean array for prime checking
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of prime as non-prime
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    # Collect prime numbers
    return [num for num in range(2, n+1) if is_prime[num]]


def count_primes_and_moves(n):
    """
    Determine the number of primes and game outcome for a single round
    Args:
        n (int): Upper limit of the game range
    Returns:
        bool: True if Ben wins, False if Maria wins
    """
    # Get primes in the range
    primes = sieve_of_eratosthenes(n)

    # Game outcome depends on number of primes
    return len(primes) % 2 == 0


def isWinner(x, nums):
    """
    Determine the overall winner of multiple rounds of Prime Game
    Args:
        x (int): Number of game rounds
        nums (list): Upper limits for each round
    Returns:
        str/None: Name of the winner or None if no clear winner
    """
    # Input validation
    if not x or not nums or x != len(nums):
        return None

    # Track wins for Maria and Ben
    maria_wins = ben_wins = 0

    # Play each round
    for n in nums:
        if count_primes_and_moves(n):
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"

    return None
