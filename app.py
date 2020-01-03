# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request
import scraping
import graph

# Flaskオブジェクトの生成
app = Flask(__name__)

# 「/」へアクセスがあった場合
@app.route('/')
def main():
    return render_template('category.html')

# 「/search/」へアクセスがあった場合
@app.route('/search/', methods=["GET", "POST"])
def search():
    # GETの受け取り
    keyword = request.args.get('keyword')
    category_root = request.args.get('category_root')
    category_child = request.args.get('category_child')
    # search_scopeの値を変えるとメルカリから取得してくる商品の数が変化します。
    # search_scope = 1で132件（132件以上商品が存在する場合）
    # 大きくなればなるほど取得に時間がかかるのでひとまず1でよいかと
    search_scope = 1

    # デバッグ用（getの値が正しく取得できているかどうか）
    print("keyword: ", keyword)
    print("category_root: ", category_root)
    print("category_child: ", category_child)

    # スクレイピング
    itemlist = scraping.mercariSearch(keyword, category_root,
                                      category_child, search_scope)

    # 取得内容確認
    print(*itemlist, sep='\n')

    # 取得リストの件数確認
    print("itemlistの件数", len(itemlist))

    # graph.pyの呼び出し
    graphdata = graph.graphdata(itemlist)
    dataText = graphdata[0]
    labelsText = graphdata[1]
    maxSoldNum = graphdata[2]

    print("dataの中身", dataText)
    print("labelsTextの中身", labelsText)
    # html呼び出し
    return render_template('graph.html', keyword=keyword, itemlist=itemlist, dataText=dataText, labelsText=labelsText, maxSoldNum=maxSoldNum)


if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)
