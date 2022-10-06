def fibo_py(n):
  return n if n <= 1 else fibo_py(n-1) + fibo_py(n-2)
