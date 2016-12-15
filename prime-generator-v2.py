# In order to have a computer tell you if a number N is prime, 
# you can divide that number by all natural numbers in the 
# range [2, N). If any of those divisions yields zero 
# as a remainder, then the number is not a prime

# V2 for else loop
primes = []
upto = 100

for n in range(2, upto + 1):
    for divisor in range(2 , n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)                
