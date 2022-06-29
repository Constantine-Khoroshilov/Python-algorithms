# ЗАДАЧА О ВОРЕ

# Вор собирается ограбить дома. Ему нельзя грабить дома, 
# к-ые являются соседними по отношению друг к другу
# Цель - награбить как можно больше

# Массив, в к-ом индекс - номер дома (i), а сам эл. -
# - возможная добыча вора
import random
houses = [ int(random.random() * 100) for k in range(100) ]


# Реализация через меморизированнную функцию

def maxProfitWrap(houses):
  cache = [0] * len(houses)

  def maxProfit(houses, i, cache):
    # крайний случай
    if i == 1:
      return max(houses[i], houses[i-1])
    if i == 0:
      return houses[i]

    if cache[i] == 0:
      # рекурсивный вызов
      cache[i] = max(
        # ограбить
        maxProfit(houses, i-2, cache) + houses[i],
        # пропустить и перейти к следующему
        maxProfit(houses, i-1, cache)
        )
      
    return cache[i]
  
  return maxProfit(houses, len(houses) - 1, cache)


# Реализация снизу вверх с помощью табуляции

def maxProfit1(houses):
  cache = [ houses[0] ] + [ houses[1] ] + [0] * (len(houses) - 2)

  for i in range(2, len(houses)):
    # Максимальное из: ограбили предыдущий и не ограбили текущий
    # или ограбили предпредыдущий и ограбили текущий
    cache[i] = max( cache[i-1], cache[i-2] + houses[i] )

  return cache[-1]


# Реализация снизу вверх без кеша

def maxProfit2(houses):
  previos1 = houses[0]
  previos2 = houses[1]

  for i in range(2, len(houses)):
    # Максимальное из: ограбили предыдущий и не ограбили текущий
    # или ограбили предпредыдущий и ограбили текущий
    previos2, previos1 = max( previos2, previos1 + houses[i] ), previos2

  return previos2
  
