def fib1(n:int) -> int:
  
  if n == 0: return 0
  if n == 1: return 1

  return fib1(n-2) + fib1(n-1)


# Оптимизация с использованием
# динамического программирования
# (небольшая подзадача вычисляется ОДИН раз)

# Способ 1 - Memoization (сверху вниз)
# Реализация: рекурсия (рекурсивный способ)

# Вычисляет только уникальные
# значения и записывает их в кеш (массив)

def fib_wrap(n:int) -> int:

  # храним уже вычисленные числа фибоначчи
  # в массиве под их индексом в САМОЙ последовательности
  cache = [0] * (n+1)

  def fib(n:int, cache:list) -> int:
    if n == 0: return 0
    if n == 1: return 1
    # Проверка на наличие в кеше
    # Если нет, вычисляем и записываем в кеш
    if cache[n] == 0:
      cache[n] = fib(n-2, cache) + fib(n-1, cache)

    return cache[n]

  return fib(n, cache)


# Способ 2 - Tabulation (снизу вверх)
# Реализация: цикл (итеративный способ)

# реализация c использованием кеша

def fib2(n:int) -> int:
  # n - индекс (номер) числа фибоначчи в последовательности
  if n == 0 or n == 1:
    return 1
  
  cache = [0] * (n+1)
  cache[0] = cache[1] = 1

  for k in range(2, n+1):
    cache[k] = cache[k-1] + cache[k-2]

  return cache[n]

# реализация без использования кеша

def fib3(n:int) -> int:
  if n == 0: return 0
  if n == 1: return 1
  
  a = 0
  b = 1
  res = 0
  
  for k in range(2, n+1):
    res = a + b
    a = b
    b = res

  return res




