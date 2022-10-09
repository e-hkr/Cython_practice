# Cythonを用いたPython高速化実験
## 動機
データの集計・可視化にPythonは便利だが、ビッグデータに対してはPure Pythonだと動作が遅すぎる。  
そこで、Cythonを導入して少しでも高速にデータ解析を進めたい。

<br>

## 実現したいこと
数百GBの気象データを可視化する。  
1時間ごとの地表面データが1年分ずつ格納されているバイナリファイル20個を順番に読み込んで加工し、最終的にグラフを出力する。  

<br>

## 実行環境
<!-- 01~04 -->
- OS : Windows10
- Python : 3.10.7
- Cython : 0.29.32
- NumPy : 1.23.3

<!-- 05
- OS : CentOS7
- Python : 3.9.
- Cython : 
- NumPy :  -->

<br>

## ディレクトリ構成
### 01_tutorial
まずは`'Hello World'`をCythonで

### 02_fibonacci
フィボナッチ数列を計算する関数の高速化  
||実行時間|
|:-|:-:|
Pure Python|3.45222 s
Cython|**1.04660 s**

→約3.3倍の高速化に成功

<!-- 
n = 30, loop = 100
PP:0.49631
CY:0.17051
 -->

### 03_file_io
ファイルの読み込みを含む関数の高速化  
||実行時間|
|:-|:-:|
Pure Python|0.15331 s
Cython|**0.08741 s**

→I/Oバウンドな処理中心だが、約2倍の高速化に成功

### 04_sample
サンプルデータでのデモ  
||実行時間|
|:-|:-:|
Pure Python 1回目|4.54160 s
Pure Python 2~6回目|3.81459 s
Cython 1回目|1.66525 s
Cython 2~6回目|**1.54715 s**

→約3倍の高速化に成功
<!-- したが、更なる高速化に向けてボトルネックはどこなのか探す
【課題】
- Cython内で正しくNumPyをつかえているのか
- 読み込みの行が1ループに付き3回呼び出されていること
  - `.reshape`と変数選択を別の行でやるべき？
  - 改行なしにしてみる
- 以下のどれが最速か
  - `hist = hist + _hist`
  - `hist += _hist`
  - `hist = np.add(hist, _hist)`
- ヒストグラムをスクラッチで実装する
- `hist = np.histgram(...)[0]` or `hist, _ = np.histgram(...)`
- `np.histgram(..., bins=40, range=(0,200))` -> `np.histgram(..., bins=40., range=(0.,200.))`
-  -->

<!-- ## 05_real
実データでの検証  
||実行時間|
|:-|:-:|
Pure Python 1回目| s
Pure Python 2回目| s
Cython 1回目| s
Cython 2回目| s

→ -->

<br>

## 結論
Pure Pythonに比べて3倍程度の高速化が見込めるため、Cythonを使用するメリットがありそうだとわかった。  
今後はさらに高速化できるようブラッシュアップしていきたい。
<!-- 複数回同じプログラムを実行する際にはCythonは有効な手段である。特にfor文の多いプログラムには有効。  
一方、ビッグデータ集計時のように一度きりしか実行しないプログラムやI/Oバウンドな処理に関しては高速化が見込めず、Cythonを使用するメリットが小さいため、他手法を検討する必要がある。また、演算にndarrayを使用したり、データ型を単精度にすることで高速化できることもわかった。 -->

<br>

## 他手法
- アルゴリズムを工夫する  
  <!-- 一番現実的な方法。今回はファイルのI/Oがボトルネックと考えられるので、ファイルを分割するのが良さそう。 -->
  一番現実的な方法。今回はファイルの読み飛ばし部分が無駄に感じられるので、ファイルを分割すればより速くなりそう。
- numba  
  <!-- 手軽に高速化できるが、Cython同様のデメリットを持ち、一部対応していないものもある。 -->
  手軽に高速化できるが、一部対応していないものがある。
- 並列処理(マルチプロセス、ProcessPoolExecutor)  
  計算量が多く分割して処理しても問題ないときに有効。
  <!-- 今回はI/Oバウンドと考えられるので、効果は薄そう。 -->
- 並行処理(マルチスレッド、ThreadPoolExecutor)  
  待ち時間が多いときに有効。

<br>

## 参考資料
<details><summary></summary>

Cythonの環境構築
- 環境構築からコンパイルまで  
  https://qiita.com/gwappa/items/db1f6f27218da0c5a932  
  https://qiita.com/en3/items/1f1a609c4d7c8f3066a7

<!-- NumPyをCython内で使用する方法
-  -->

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