def fibo_cy(n):
  return n if n <= 1 else fibo_cy(n-1) + fibo_cy(n-2)
