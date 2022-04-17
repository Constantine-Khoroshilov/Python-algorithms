# Квадратичные сортировки

def insertionSort(A:list):
  N = len(A)
  for k in range(1, N):
    while k > 0 and A[k-1] > A[k]:
      A[k], A[k-1] = A[k-1], A[k]
      k -= 1


def selectionSort(A:list):
  N = len(A)
  for k in range(0, N-1):
    for n in range(k+1, N):
      if A[k] > A[n]:
        A[k], A[n] = A[n], A[k]


def bubbleSort(A:list):
  N = len(A)
  for bypass in range(1, N):
    for n in range(0, N-bypass):
      if A[n] > A[n+1]:
        A[n+1], A[n] = A[n], A[n+1]



# Инвертация списка

def reverseList(A:list):
  N = len(A)
  for k in range(N//2):
    A[k], A[N-1-k] = A[N-1-k], A[k]



# Проверка отсортированности за О(N)

def isSorted(A, ascending = True):
  # sign - множитель, к-ый принимает только значения 1 или -1.
  # Это нужно для того, чтобы менять знак сравнения в условии
  # в зависимости от значения ascending (по возрастанию или убыванию)
  sign = 2 * int(ascending) - 1
  
  for k in range(len(A)-1):
    if sign * A[k] > sign * A[k+1]:
      return False
  return True



# Циклический сдвиг

def cycleShift(A:list, count:int=1, direction:bool=True):
  N = len(A)

  for i in range(count):
    if direction:
      # left
      x = A[0]
      for k in range(0, N-1):
        A[k] = A[k+1]

      A[N-1] = x

    else:
      # right
      x = A[N-1]
      for k in range(N-1, 0, -1):
        A[k] = A[k-1]

      A[0] = x



# Рекурсивные алгоритмы сортировки

def mergeSort(A:list):
  N = len(A)
  if N <= 1:
    return

  L = [ A[k] for k in range(N//2) ]
  R = [ A[k] for k in range(N//2, N) ]

  mergeSort(L)
  mergeSort(R)

  # сортирующее действие (обратный ход рекурсии)
  r = l = a = 0

  while l < len(L) and r < len(R):
    # усточивость - не меняет исходный порядок равных элементов
    if L[l] <= R[r]:
      A[a] = L[l]
      l += 1
      a += 1
    else:
      A[a] = R[r]
      r += 1
      a += 1

  while l < len(L):
    A[a] = L[l]
    l += 1
    a += 1
  while r < len(R):
    A[a] = R[r]
    r += 1
    a += 1


def qsort(A:list, start:int, end:int):
  if not end > start:
    return

  # баррьерный элемент
  pivot = A[start]
  # указатели
  L = start
  R = end

  # сортирующее действие (прямой ход рекурсии)
  while L < R:
    while A[L] < pivot:
      L += 1
    while A[R] > pivot:
      R -= 1

    A[L], A[R] = A[R], A[L]

  qsort(A, start, L-1)
  qsort(A, R+1, end)

  
  
  
    

    
  

