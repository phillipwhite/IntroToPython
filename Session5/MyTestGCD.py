from GCDFunction import gcd
from PrimeNumberFunction import isPrime
print(gcd(45,30))

print(isPrime(37))
print(isPrime(1))
count = 0
for i in range(0, 10000):
    if isPrime(i):
        print(i)
        count += 1

print(count)
