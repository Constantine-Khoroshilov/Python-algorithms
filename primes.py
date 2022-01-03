
def getPrimeFactors(num:int) -> list:
  primeFactors = []
  while num > 1:
    for divisor in range(2, num+1):
      if num % divisor == 0:
        
        if divisor not in primeFactors:
          primeFactors.append(divisor)
          
        num //= divisor
        break
    
  return primeFactors



def getPrimes(N:int) -> list:
  numbers = [True] * (N+1)
  numbers[0] = numbers[1] = False
  
  for k in range(2, int((N+1)**0.5)+1):
    if numbers[k]:
      for num in range(2*k, N+1, k):
        numbers[num] = False

  primes = []
  for k in range(0, N+1):
    if numbers[k]:
      primes.append(k)

  return primes



def isPrime(num:int) -> bool:
  for divisor in range(2, int(num**0.5)+1):
    if num % divisor == 0:
      return False
  return True


  
