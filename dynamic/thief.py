# ЗАДАЧА О ВОРЕ

# Вор собирается ограбить дома. Ему нельзя грабить дома, 
# к-ые являются соседними по отношению друг к другу
# Цель - награбить как можно больше

# Массив, в к-ом индекс - номер дома (i), а сам эл. -
# - возможная добыча вора
import random
houses = [ int(random.random() * 100) for k in range(100) ]


# Реализация через меморизированнную функциию

cache = [0] * len(houses)

def maxProfit(houses, i=-1):
  if i == -1:
    i = len(houses) - 1
  
  # крайний случай
  if i == 1:
    return max(houses[i], houses[i-1])
  if i == 0:
    return houses[i]

  if cache[i] == 0:
    # рекурсивный вызов
    cache[i] = max(
      # ограбить
      maxProfit(houses, i-2) + houses[i],
      # пропустить и перейти к следующему
      maxProfit(houses, i-1)
      )
    
  return cache[i]
