def factorial(num:int) -> int:
  f = 1
  for k in range(2, num+1):
    f *= k
  return f


N = 1

def showPermutations(elements:list, noRepeat:bool=True, depth:int=-1, prefix:list=[]):
  """ Print on the screen all possible permutations of the elements """
  # depth - глубина рекурсии
  # prefix - список перестановок
  # elements - список эл., для к-ых ищем перестановки
  # noRepeat - не учитывать повторения

  global N

  # Запуск программы
  if depth == -1:
    N = 1
    depth = len(elements)
    print("Кол-во перестановок:", factorial(depth) if noRepeat else depth**depth)
    input("Нажмите Enter, чтобы продолжить")

  # Крайний (базовый) случай
  if depth == 0:
    print(N, "-", *prefix)
    N += 1
    return

  for el in elements:
    if el in prefix and noRepeat:
      continue
    # Передаем КОПИЮ списка prefix в реккурентном вызове
    showPermutations(elements, noRepeat, depth-1, prefix+[el])
