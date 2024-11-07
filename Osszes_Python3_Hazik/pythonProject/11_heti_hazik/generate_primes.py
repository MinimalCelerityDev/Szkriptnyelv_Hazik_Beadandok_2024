import json

def generate_primes(limit):
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    return [num for num, prime in enumerate(is_prime) if prime]

def save_primes_to_json(primes, filename):
    with open(filename, 'w') as file:
        json.dump(primes, file)

if __name__ == "__main__":
    primes = generate_primes(10_000_000)
    save_primes_to_json(primes, 'primes.json')
