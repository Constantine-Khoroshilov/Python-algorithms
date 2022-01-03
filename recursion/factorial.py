# Головная рекурсия
# (использование параметров после вызова)
def factorial1(n:int) -> int:
  assert n >= 0, "Факториал при n < 0 неопределен"
  
  # Базовый случай
  if n == 0:
    return 1

  # Реккурентный вызов, возрат значения функции
  return factorial1(n-1) * n

print(factorial1(3))



# Хвостовая рекурсия
# (использование параметров перед вызовом)
def factorial2(n:int, res:int=1) -> int:
  assert n >= 0, "Факториал при n < 0 неопределен"

  if n == 0:
    return res

  return factorial2(n-1, n * res)

print(factorial2(3))
