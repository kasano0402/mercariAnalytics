# mercariAnarytics
メルカリ価格分析webサービス

mercariAnarytics</br>
│  app.py ←サーバープログラム（最初に呼び出されるもの）</br>
│  scraping.py ←メルカリから情報を拾ってくるプログラム</br>
│</br>
├─static</br>
│  ├─css</br>
│  │      bootstrap.css ←いい感じのcssが詰まったファイル（詳しくは調べてみて）</br>
│  │      index.css ←トップページ用のcss</br>
│  │      result.css ←🔺結果画面用のcss</br>
│  │</br>
│  ├─js</br>
│  │      bootstrap.js ←いい感じのjqueryが詰まったファイル</br>
│  │      jquery-3.1.1.min.js ←jquery</br>
│  │</br>
│  └─picture</br>
│          logo.png ←ロゴ画像（仮）</br>
│</br>
├─templates</br>
│      layout.html ←サイトの全体構成のhtml</br>
│      index.html ←トップページのhtml</br>
│      category.html ←トップページ内の選択ボックスのhtml（長いので個別ファイル化）</br>
│      result.html ←🔺結果画面のhtml</br>
│      graph.html ←🔺結果画面内のグラフのhtml</br>
│</br>
└─__pycache__</br>
        main.cpython-38.pyc ←気にしなくてよい</br>
        scraping.cpython-38.pyc ←気にしなくてよい</br>
