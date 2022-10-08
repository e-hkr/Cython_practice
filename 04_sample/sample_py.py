import numpy as np
import matplotlib.pyplot as plt


def sample_py():
    """
    格子点データを1日ごとに読み込み集計し、ヒストグラムを作成する関数
    """

    # h:24h v:5変数 y:緯度方向の格子数 x:経度方向の格子数
    h, v, y, x = 24, 5, 30, 30
    path = '../sample.dat'

    # 初日分を読み込み、0番目の変数(降水量)を抽出
    grid_data = np.fromfile(path, dtype='>f', count=h*v*y*x, offset=0)\
                  .reshape(h, v, y, x)[:,0,:,:]
    hist = np.histogram(grid_data, bins=40, range=(0, 200))[0]
    
    for d in range(1825):#365d*5y+1d-1
        grid_data = np.fromfile(path, dtype='>f', count=h*v*y*x, 
                                offset=h*v*y*x*4*(d+1))\
                      .reshape(h, v, y, x)[:,0,:,:]
        _hist = np.histogram(grid_data, bins=40, range=(0, 200))[0]
        hist = hist + _hist

    edges = np.linspace(0, 200, 40)
    plt.bar(edges, hist, width=5.1)
    plt.yscale('log')
    plt.title('sample')
    plt.savefig('sample.png')
    # plt.show()
