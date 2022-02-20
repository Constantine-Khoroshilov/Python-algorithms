def pow(a:float, n:int) -> float:
  assert n >= 0, "n ≥ 0"
  
  if n == 0:
    return 1
  if a == 0:
    return 0
  if a == 1:
    return 1
  
  if n % 2 == 0:
    return pow(a*a, n//2)

  else:
    return a * pow(a, n-1)
