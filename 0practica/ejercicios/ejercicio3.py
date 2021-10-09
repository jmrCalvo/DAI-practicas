def criba_eratostenes(n):
    primes = []
    isPrime = [1 for i in range(n)]
    isPrime[0] = isPrime[1] = 0

    for number in range(n):
        if isPrime[number]:
            primes.append(number)
            divisible = 2
            while number*divisible < n:
                isPrime[number*divisible] = 0
                divisible += 1
    return primes


if __name__ == "__main__":
    print(criba_eratostenes(200))
