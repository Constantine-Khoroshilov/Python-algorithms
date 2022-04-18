def binarySearch(A:list, key:int) -> (int, int):
  # A отсортирован по возрастанию
  
  # поиск левой границы
  # указатели 
  L = -1
  R = len(A)

  while R - L > 1:
    M = (L + R) // 2
    # L не может указывать на элемент, к-ый равен key, а
    # R может. Это обеспечивает то, что L остановится на
    # leftBoundary, а R будет к нему приближаться
    if A[M] < key:
      L = M
    else:
      R = M

  leftBoundary = L 

  # поиск правой границы
  # указатели
  L = -1
  R = len(A)
    
  while R - L > 1:
    M = (L + R) // 2
    # R не может указывать на элемент, к-ый равен key, а
    # L может. Это обеспечивает то, что R остановится на
    # rightBoundary, а L будет к нему приближаться
    if A[M] <= key:
      L = M
    else:
      R = M

  rightBoundary = R

  return (leftBoundary, rightBoundary)
