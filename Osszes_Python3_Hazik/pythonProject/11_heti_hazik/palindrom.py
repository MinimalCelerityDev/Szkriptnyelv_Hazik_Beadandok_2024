import json

def generálás(limit):

    is_prime = [True] * limit

    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    return [num for num, prime in enumerate(is_prime) if prime]

def mentés(primes, filename):

    with open(filename, 'w') as file:
        json.dump(primes, file)

if __name__ == "__main__":
    
    prímek = generálás(10_000_000)

    mentés(prímek, 'primes.json')
