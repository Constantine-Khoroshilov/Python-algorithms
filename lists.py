# Квадратичные сортировки

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
  # крайний случай
  if len(A) <= 1:
    return

  # деление массива
  middle = len(A) // 2
  L = [ A[k] for k in range(middle) ]
  R = [ A[k] for k in range(middle, len(A)) ]

  # рекуррентный вызов (дальнейшее деление массива)
  mergeSort(L)
  mergeSort(R)

  # сортирующее действие совершается на обратном ходу
  def merge(L:list, R:list) -> list:
    mergeList = []
    l = r = 0
    
    while l < len(L) and r < len(R):
      # усточивость
      if L[l] <= R[r]:
        mergeList.append(L[l])
        l += 1
      else:
        mergeList.append(R[r])
        r += 1

    while l < len(L):
      mergeList.append(L[l])
      l += 1
    while r < len(R):
      mergeList.append(R[r])
      r += 1
    
    return mergeList

  # L и R отсортированы и объединены
  C = (merge(L, R))
  # не потерять связь с исходным списком!
  for k in range(len(A)):
    A[k] = C[k]

  
    

    
  

