import time
from read_binary_cy import read_binary_cy
from read_binary_py import read_binary_py


def main():
  # Cython
  start_time = time.time()
  for i in range(300):
    data = read_binary_cy(i)
  print(type(data))
  print(data.max())
  stop_time = time.time()

  print(f'Cython : {stop_time - start_time:.7f}s')

  # Pure Python
  start_time = time.time()
  for i in range(300):
    data = read_binary_py(i)
  print(type(data))
  print(data.max())
  stop_time = time.time()

  print(f'Pure Python : {stop_time - start_time:.7f}s')


if __name__ == '__main__':
  main()

# サンプルデータでの結果
## Cython
## 1回目：1.06255 s
## 2回目：0.21087 s
 
## Pure Python
## 1回目：0.21088 s
## 2回目：0.15854 s