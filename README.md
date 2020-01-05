# mercariAnarytics

メルカリ価格分析 web サービス

mercariAnarytics</br>
│ app.py ← サーバープログラム（最初に呼び出されるもの）</br>
│ scraping.py ← メルカリから情報を拾ってくるプログラム</br>
| graph.py ← グラフの構成要素を作成するプログラム（まさ担当）</br>
│</br>
├─static</br>
│ ├─css</br>
│ │ bootstrap.css ← いい感じの css が詰まったファイル（詳しくは調べてみて）</br>
│ │ index.css ← トップページ用の css</br>
│ │ result.css ←△ 結果画面用の css</br>
│ │</br>
│ ├─js</br>
│ │ bootstrap.js ← いい感じの jquery が詰まったファイル</br>
│ │ jquery-3.1.1.min.js ←jquery</br>
│ │</br>
│ └─picture</br>
│ logo.png ← ロゴ画像（仮）</br>
│</br>
├─templates</br>
│ layout.html ← サイトの全体構成の html</br>
│ index.html ← トップページの html</br>
│ category.html ← トップページ内の選択ボックスの html（長いので個別ファイル化）</br>
│ result.html ←△ 結果画面の html</br>
│ graph.html ←△ 結果画面内のグラフの html</br>
│</br>
└─**pycache**</br>
main.cpython-38.pyc ← 気にしなくてよい</br>
scraping.cpython-38.pyc ← 気にしなくてよい</br>
