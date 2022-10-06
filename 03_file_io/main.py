import timeit
from read_binary_cy import read_binary_cy
from read_binary_py import read_binary_py


def main():
    num_days = 300
    loop = 10

    t = timeit.timeit(f'read_binary_py({num_days})', 
                      globals=globals(), 
                      number=loop)
    print(f'Pure Python : {t/loop:.5f} s')
    
    t = timeit.timeit(f'read_binary_cy({num_days})', 
                      globals=globals(), 
                      number=loop)
    print(f'Cython : {t/loop:.5f} s')


if __name__ == '__main__':
    main()
