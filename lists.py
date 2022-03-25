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

  # деление массива
  L = [ A[k] for k in range(N//2) ]
  R = [ A[k] for k in range(N//2, N) ]

  # рекуррентный вызов (дальнейшее деление массива)
  mergeSort(L)
  mergeSort(R)

  # !!! сортирующее действие совершается на обратном ходу
  r = l = a = 0

  while l < len(L) and r < len(R):
    # усточивость
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

  
    

    
  

