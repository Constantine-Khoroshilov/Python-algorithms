def isPalindrome(string:str, i:int=0) -> bool:
  
  # Дошли до середины слова
  if i == len(string) // 2:
    return True

  # Число не палидром (буквы не сходятся)
  j = len(string) - 1 - i
  if string[i] != string[j]:
    return False

  # Реккурентный вызов, возрат значения функции
  # и переход к след. индексу синвола строки
  return isPalindrome(string, i+1)

print(isPalindrome("доход"))
