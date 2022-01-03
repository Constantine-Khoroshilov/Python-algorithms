# Быстрое возведение в степень

def pow(a:float, n:int) -> float:
  assert a > 0 and n >= 0, "a > 0, n ≽ 0"
  
  # крайний случай
  if n == 0:
    return 1
  
  # a^n = a^(n-1) * a
  # n - глубина рекурсии
  
  # пусть n - четное, тогда число n/2 целое
  # значит: a^n = a^2(n/2) = (a^2)^(n/2)
  # => умньшение глубины рекурсии
  
  elif n % 2 == 1: # нечетное
    return pow(a, n-1) * a

  else:
    return pow(a*a, n // 2)
