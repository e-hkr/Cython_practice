# Cython練習
## 動機
データの集計・可視化にPythonは便利だが、ビッグデータに対してはPure Pythonだと動作が遅すぎる。  
そこで、Cythonを導入して少しでも高速にデータ解析を進めたい。

<br>

## 実現したいこと
数百GBの気象データを可視化する。  
1時間ごとの地表面データが1年分ずつ格納されているバイナリファイル20個を順番に読み込んで加工し、最終的にグラフを出力する。  

<br>

## 実行環境
01~04
- OS : Windows10
- Python : 3.10.7
- Cython : 0.29.32
- NumPy : 1.23.3

05
- OS : CentOS7
- Python : 3.9.
- Cython : 
- NumPy : 

<br>

## ディレクトリ構成
### 01_tutorial
まずは`'Hello World'`をCythonで

### 02_fibonacci
フィボナッチ数列の高速化  
Pure Python : 3.45222 s  
Cython : 1.04660 s  
→約3.3倍の高速化に成功

<!-- 
n = 30, loop = 100
PP:0.49631
CY:0.17051
 -->

### 03_file_io
ファイルの読み込みを含む関数の高速化  
Pure Python : 0.15331 s  
Cython : 0.08741 s  
→I/Oバウンドな処理中心だが、`for`文の最適化で高速化に成功したと考えられる

### 04_sample
サンプルデータでのデモ  
Pure Python :  s  
Cython :  s  
→

## 05_real
実データでの実験  
Pure Python :  s  
Cython :  s  
→

<br>

## 結論
複数回同じプログラムを実行する際にはCythonは有効な手段である。特にfor文の多いプログラムには有効。  
一方、ビッグデータ集計時のように一度きりしか実行しないプログラムやI/Oバウンドな処理に関しては高速化が見込めず、Cythonを使用するメリットが小さいため、他手法を検討する必要がある。また、演算にndarrayを使用したり、データ型を単精度にすることで高速化できることもわかった。

<br>

## 他手法
- アルゴリズムを工夫する  
  一番現実的な方法。今回はファイルのI/Oがボトルネックと考えられるので、ファイルを分割するのが良さそう。
- numba  
  手軽に高速化できるが、Cython同様のデメリットを持ち、一部対応していない部分もある。
- 並列処理(マルチプロセス、ProcessPoolExecutor)  
  計算量が多く分割して処理しても問題ないときに有効。今回はI/Oバウンドと考えられるので、効果は薄そう。
- 並行処理(マルチスレッド、ThreadPoolExecutor)  
  待ち時間が多いときに有効。

<br>

## 参考資料
<details><summary></summary>

Cythonの環境構築
- 環境構築からコンパイルまで  
  https://qiita.com/gwappa/items/db1f6f27218da0c5a932  
  https://qiita.com/en3/items/1f1a609c4d7c8f3066a7
- 

実行時間計測
- timeモジュール  
  https://docs.python.org/ja/3/library/time.html
- timeitモジュール  
  https://docs.python.org/ja/3/library/timeit.html  
  https://note.nkmk.me/python-timeit-measure/
- cProfile  
  https://docs.python.org/ja/3/library/profile.html  
  https://qiita.com/meshidenn/items/4dbde22d1e7a13a255bb
- pstatsモジュール  
  https://docs.python.org/ja/3/library/profile.html#module-pstats
- line_profiler  
  https://qiita.com/aratana_tamutomo/items/aa3b723a3dd7a44e45d6
- timeコマンド  
  https://qiita.com/tossh/items/659e5934e52b38183200

</details>