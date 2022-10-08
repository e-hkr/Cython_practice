import timeit
from sample_py import sample_py
from sample_cy import sample_cy


def main():
    loop = 5

    t = timeit.timeit('sample_py()', globals=globals(), number=1)
    print(f'Pure Python 1回目 : {t:.5f} s')
    t = timeit.timeit('sample_py()', globals=globals(), number=loop)
    print(f'Pure Python 2~{loop+1}回目 : {t/loop:.5f} s')

    t = timeit.timeit('sample_cy()', globals=globals(), number=1)
    print(f'Cython 1回目 : {t:.5f} s')
    t = timeit.timeit('sample_cy()', globals=globals(), number=loop)
    print(f'Cython 2~{loop+1}回目 : {t/loop:.5f} s')


if __name__ == '__main__':
    main()
