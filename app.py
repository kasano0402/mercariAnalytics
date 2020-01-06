# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request
import scraping
import graph

# Flaskオブジェクトの生成
app = Flask(__name__)

# 「/」へアクセスがあった場合
@app.route('/')
def main():
    return render_template('condition.html', title="mercari analytics")

# 「/search/」へアクセスがあった場合
@app.route('/search/', methods=["GET", "POST"])
def search():
    # GETの受け取り
    keyword = request.args.get('keyword')
    category_root = request.args.get('category_root')
    category_child = request.args.get('category_child')
    item_condition = ""
    if None != request.args.get("condition_all"):
        item_condition += "&condition_all=1"
    if None != request.args.get("item_condition_id[1]"):
        item_condition += "&item_condition_id[1]=1"
    if None != request.args.get("item_condition_id[2]"):
        item_condition += "&item_condition_id[2]=1"
    if None != request.args.get("item_condition_id[3]"):
        item_condition += "&item_condition_id[3]=1"
    if None != request.args.get("item_condition_id[4]"):
        item_condition += "&item_condition_id[4]=1"
    if None != request.args.get("item_condition_id[5]"):
        item_condition += "&item_condition_id[5]=1"
    if None != request.args.get("item_condition_id[6]"):
        item_condition += "&item_condition_id[6]=1"

    # デバッグ用（getの値が正しく取得できているかどうか）
    print("keyword: ", keyword)
    print("category_root: ", category_root)
    print("category_child: ", category_child)
    print("item_condition", item_condition)

    # 検索範囲の指定
    search_scope = 1

    # 売り切れ商品の取得
    sold_itemlist = scraping.mercariSearch(keyword, category_root,
                                           category_child, search_scope, item_condition, 1)

    # 販売中の商品の取得
    unsold_itemlist = scraping.mercariSearch(keyword, category_root,
                                             category_child, search_scope, item_condition, 0)

    # 取得内容の並び替え
    sold_itemlist = sorted(sold_itemlist, key=lambda x: x[1])
    unsold_itemlist = sorted(unsold_itemlist, key=lambda x: x[1])

    # 取得内容確認
    print("sold_itemlistの件数", len(sold_itemlist))
    # print(*sold_itemlist, sep='\n')
    print("---------------------------------------------------------------")
    print("unsold_itemlistの件数", len(unsold_itemlist))
    # print(*unsold_itemlist, sep='\n')

    # graph.pyを呼び出し&値の受け取り
    graphdata = graph.graphdata(sold_itemlist)
    graph_data = graphdata[0]
    graph_labels = graphdata[1]
    graph_max = graphdata[2]
    graph_stepsize = graphdata[3]

    # 購入件数の多い価格帯
    price_list = graph_labels.split("~'")
    int_pricelist = []
    for price in price_list:
        tmp = price.replace(",", "").replace("'", "")
        tmp = tmp[1:]
        if tmp != "":
            int_pricelist.append(int(tmp))

    graph_data_list = graph_data.split(",")
    int_graph_data_list = []
    for data in graph_data_list:
        int_graph_data_list.append(int(data))

    popular_price = int_pricelist[int_graph_data_list.index(
        max(int_graph_data_list))]

    # html呼び出し
    return render_template('graph.html',
                           title=keyword+"の分析結果",
                           keyword=keyword,
                           sold_itemlist=sold_itemlist,
                           unsold_itemlist=unsold_itemlist,
                           graph_data=graph_data,
                           graph_labels=graph_labels,
                           graph_max=graph_max,
                           graph_stepsize=graph_stepsize,
                           popular_price=popular_price)


if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)
