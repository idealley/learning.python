from itertools import compress
from itertools import permutations

# Compress iterator
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))  

print("Even selector: ", even_selector)
print("Odd selector: ", odd_selector)
print("Data: ", list(data))
print("Even numbers: ", even_numbers)
print("Odd numbers: ", odd_numbers)

# Permutations
print("Permutations: ", list(permutations('ABC')))