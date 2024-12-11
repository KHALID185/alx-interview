#!/usr/bin/python3
"""
Prime Game Problem: Comprehensive Solution for Maria and Ben's Game
"""


def generate_primes(n):
    """
    Efficiently generate prime numbers up to n using Sieve of Eratosthenes
    Args:
        n (int): Upper limit for generating primes
    Returns:
        list: Prime numbers up to n
    """
    if n < 2:
        return []

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


def game_outcome(n):
    """
    Determine the game outcome for a single round
    Args:
        n (int): Upper limit of the game range
    Returns:
        bool: True if Ben wins, False if Maria wins
    """
    # Special case: If n is 1, Ben wins
    if n == 1:
        return True

    # Get primes in the range
    primes = generate_primes(n)

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
    if not x or x <= 0 or not nums or len(nums) != x:
        return None

    # Track wins for Maria and Ben
    maria_wins = ben_wins = 0

    # Play each round
    for n in nums:
        if game_outcome(n):
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"

    return None
