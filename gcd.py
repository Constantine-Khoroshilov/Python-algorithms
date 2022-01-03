# Если общего делителя нет, алгоритм вернет 1

def gcd1(a:int, b:int) -> int:
  while a > 0 and b > 0:
    if a > b:
      a %= b
    else:
      b %= a

  return max(a, b)


def gcd2(a:int, b:int) -> int:
  if a == 0:
    return b
  elif b == 0:
    return a
  elif a > b:
    return gcd2(a%b, b)
  else:
    return gcd2(a, b%a)


def gcd3(a:int, b:int) -> int:
  # Пусть первый аргумент (a) всегда больше второго (b)
  # 0 может быть результатом только остатка от деления 
  if b == 0: 
    return a
  # Тогда в качестве первого аргумента передаем наим. число (b),
  # а в качестве второго - остаток от деления на это число (a%b),
  # так как он всегда меньше делителя (a%b < b)
  return gcd3(b, a%b)
