def is_prime(n):
        if n<=2:
         return False
        for i in range(2,n):
          if n%i == 0:
            return False
        return True
        
def find_primes(array):
        primes =[]
        for num in array:
            if is_prime(num):
                primes.append(num)
        return primes
        
numbers = [ 19, 23, 4, 16, 28, 13, 31, 8, 29, 14, 6, 35, 2, 11, 17, 5, 9, 27, 12, 30]
prime_numbers = find_primes(numbers)
print(prime_numbers)
print(max(prime_numbers))
print(min(prime_numbers))
print(sum(prime_numbers))
