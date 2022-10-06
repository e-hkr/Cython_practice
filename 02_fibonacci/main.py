import timeit
from fibo_py import fibo_py
from fibo_cy import fibo_cy


def fibo(n):
  return n if n <= 1 else fibo(n-1) + fibo(n-2)


def main():
    n = 30
    loop = 100

    t = timeit.timeit(f'fibo_py({n})', globals=globals(), number=loop)
    print(f'Pure Python : {t/loop:.5f} s')
    t = timeit.timeit(f'fibo_cy({n})', globals=globals(), number=loop)
    print(f'Cython : {t/loop:.5f} s')


if __name__ == '__main__':
    main()
