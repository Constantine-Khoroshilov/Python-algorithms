def selection_sort(A:list):
  N = len(A)
  for k in range(0, N-1):
    for n in range(k+1, N):
      if A[k] > A[n]:
        A[k], A[n] = A[n], A[k]


def bubble_sort(A:list):
  N = len(A)
  for bypass in range(1, N):
    for n in range(0, N-bypass):
      if A[n] > A[n+1]:
        A[n+1], A[n] = A[n], A[n+1]


def left_shift(A:list):
  N = len(A)
  x = A[0]
  for k in range(0, N-1):
    A[k] = A[k+1]

  A[N-1] = x


def right_shift(A:list):
  N = len(A)
  x = A[N-1]
  for k in range(N-1, 0, -1):
    A[k] = A[k-1]

  A[0] = x
    
  

