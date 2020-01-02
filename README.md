# mercariAnarytics
メルカリ価格分析webサービス

mercariAnarytics
│  app.py ←サーバープログラム（最初に呼び出されるもの）
│  scraping.py ←メルカリから情報を拾ってくるプログラム
│
├─static
│  ├─css
│  │      bootstrap.css ←いい感じのcssが詰まったファイル（詳しくは調べてみて）
│  │      index.css ←トップページ用のcss
│  │      result.css ←結果画面用のcss
│  │
│  ├─js
│  │      bootstrap.js ←いい感じのjqueryが詰まったファイル
│  │      jquery-3.1.1.min.js ←jquery
│  │
│  └─picture
│          logo.png ←ロゴ画像（仮）
│
├─templates
│      layout.html ←サイトの全体構成のhtml
│      index.html ←トップページのhtml
│      category.html ←トップページ内の選択ボックスのhtml（長いので個別ファイル化）
│      result.html ←結果画面のhtml
│      graph.html ←結果画面内のグラフのhtml
│
└─__pycache__
        main.cpython-38.pyc ←気にしなくてよい
        scraping.cpython-38.pyc ←気にしなくてよい
