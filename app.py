# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request
import scraping

# Flaskオブジェクトの生成
app = Flask(__name__)

# 「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route('/')
def hello():
    return render_template('select.html')


@app.route('/search/', methods=["GET", "POST"])
def search():
    # GETの受け取り
    keyword = request.args.get('keyword')
    category_root = request.args.get('category_root')
    category_child = request.args.get('category_child')
    scope = 3
    sort_order = "created_desc"

    # デバッグ用
    print("keyword: ", keyword)
    print("category_root: ", category_root)
    print("category_child: ", category_child)

    # スクレイピング
    scraping.mercariSearch(keyword, category_root,
                           category_child, scope, sort_order)
    return render_template('category.html')


if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)
