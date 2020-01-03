# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request
import scraping

# Flaskオブジェクトの生成
app = Flask(__name__)

# 「/」へアクセスがあった場合
@app.route('/')
def hello():
    return render_template('category.html')

# 「/search/」へアクセスがあった場合
@app.route('/search/', methods=["GET", "POST"])
def search():
    # GETの受け取り
    keyword = request.args.get('keyword')
    category_root = request.args.get('category_root')
    category_child = request.args.get('category_child')
    search_scope = 3

    # デバッグ用
    print("keyword: ", keyword)
    print("category_root: ", category_root)
    print("category_child: ", category_child)

    # スクレイピング
    itemlist = scraping.mercariSearch(keyword, category_root,
                                      category_child, search_scope)

    print(*itemlist, sep='\n')
    return render_template('graph.html', keyword=keyword, itemlist=itemlist)


if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)
