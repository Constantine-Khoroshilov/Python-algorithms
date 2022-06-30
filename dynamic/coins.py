# ЗАДАЧА О РАЗМЕНЕ МОНЕТ
# У нас есть несколько номиналов и неограниченное
# кол-во монет. Нужно набрать определенную сумму,
# используя наим. кол-во монет

# по возрастанию, номинал 1 должен быть обязат.
nominals = [1, 5, 12, 19]

def minCoinsWrap(S, nominals):
  M = max(nominals) + 1

  def minCoins(S, i, nominals, M):
    # i - текущий номинал
    
    # Крайний случай
    if S in nominals:
      return 1

    M1 = M2 = M
    
    # Рекурсивный вызов
    # Уменьшать (разменивать) сумму текущим
    # номиналом, т.е. использовать его монету, но
    # только тогда, когда он не больше суммы
    if S > nominals[i]:
      M1 = minCoins(S-nominals[i], i, nominals, M) + 1
    # Использовать другой номинал, если он есть
    if i > 0:
      M2 = minCoins(S, i-1, nominals, M)

    return min(M1, M2)
  # Уменьшать (разменивать) сумму начинаю с наиб.
  # номинала, т.к. это более разумно
  return minCoins(S, len(nominals)-1, nominals, M)
