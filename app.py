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

    # 売り切れ商品の取得
    sold_itemlist = scraping.mercariSearch(keyword, category_root,
                                           category_child, search_scope, 1)

    # 販売中の商品の取得
    unsold_itemlist = scraping.mercariSearch(keyword, category_root,
                                             category_child, search_scope, 1)

    # 取得内容の並び替え
    sold_itemlist = sorted(sold_itemlist, key=lambda x: x[1])
    unsold_itemlist = sorted(unsold_itemlist, key=lambda x: x[1])

    # 取得内容確認
    print("sold_itemlistの件数", len(sold_itemlist))
    print(*sold_itemlist, sep='\n')
    print("---------------------------------------------------------------------------------------")
    print("unsold_itemlistの件数", len(unsold_itemlist))
    print(*unsold_itemlist, sep='\n')

    # graph.pyを呼び出し&値の受け取り
    graphdata = graph.graphdata(sold_itemlist)
    graph_data = graphdata[0]
    graph_labels = graphdata[1]
    graph_max = graphdata[2]
    graph_stepsize = graphdata[3]

    # html呼び出し
    return render_template('graph.html',
                           keyword=keyword,
                           sold_itemlist=sold_itemlist,
                           unsold_itemlist=unsold_itemlist,
                           graph_data=graph_data,
                           graph_labels=graph_labels,
                           graph_max=graph_max,
                           graph_stepsize=graph_stepsize)


if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)
