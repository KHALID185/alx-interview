#!/usr/bin/python3


def sieve_primes(n):
    """Generate prime numbers up to n using Sieve of Eratosthenes"""
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i*i, n + 1, i):
                prime[j] = False

    return prime


def isWinner(x, nums):
    """Determine the winner of Prime Game

    Args:
        x (int): Number of game rounds
        nums (list): Maximum numbers for each round

    Returns:
        str or None: Winner of the most rounds
    """
    if not x or not nums or x != len(nums):
        return None

    maria_wins = ben_wins = 0

    for n in nums:
        primes = sieve_primes(n)
        prime_count = sum(primes[2:n+1])

        # Determine winner based on prime count
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"

    return None
