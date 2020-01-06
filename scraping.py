import requests
import bs4
import re

# 関数


def mercariSearch(keyword,
                  category_root,
                  category_child,
                  search_scope,
                  item_condition,
                  sold_flg):
    """メルカリで検索する関数
    Arguments:
        keyword {string} -- 検索文字列
        category_root {int} -- カテゴリID（親）
        category_child {int} -- カテゴリID（子）
        search_scope {int} -- 検索範囲
        item_condition{str} -- 商品の状態
        sold_flg {int} -- 抽出条件（0:販売中, 1:売り切れ）
    """
    if sold_flg == 0:
        status_trading_sold_out = 0
        status_on_sale = 1
    else:
        status_trading_sold_out = 1
        status_on_sale = 0
    keyword = keyword.replace(" ", "+")
    pagelist = []
    for i in range(0, search_scope):
        page = 'https://www.mercari.com/jp/search/?page={0}&sort_order=created_desc&keyword={1}&category_root={2}&category_child={3}&status_trading_sold_out={4}&status_on_sale={5}{6}'.format(
            str(i), keyword, category_root, category_child, status_trading_sold_out, status_on_sale, item_condition)
        pagelist.append(page)

        resultlist = []
        for page in pagelist:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
            res = requests.get(page, headers=headers)
            # エラーチェック
            res.raise_for_status()

            # スクレイピング
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            search_result_description = None
            search_result_description = soup.select(
                '.search-result-description')
            print("search_result_description:", search_result_description)
            elems_name = soup.select('.items-box-name')
            elems_price = soup.select('.items-box-price')
            elems_photo = soup.select('.items-box-photo')
            elems_url = soup.select('.items-box > a')
            elems_photo_url = soup.select('.items-box-photo > img')

            if not search_result_description:
                for i in range(len(elems_name)):
                    new_elems_name = elems_name[i].text.replace(",", "")
                    new_elems_price = elems_price[i].text.replace(
                        ",", "").replace("¥", "")
                    new_elems_photo = re.search(
                        'figcaption', str(elems_photo[i].__str__))
                    new_elems_url = elems_url[i].get("href")
                    new_elems_photo_url = elems_photo_url[i].get("data-src")

                    new_elems_price = int(new_elems_price)
                    # if len(new_elems_name) > 10:
                    # new_elems_name = new_elems_name[0:31]
                    # リストに挿入
                    if new_elems_photo:
                        resultlist.append(
                            [new_elems_name.replace("\u3000", ""), new_elems_price, "sold", new_elems_url, new_elems_photo_url])
                    else:
                        resultlist.append(
                            [new_elems_name.replace("\u3000", ""), new_elems_price, "", new_elems_url, new_elems_photo_url])
            else:
                resultlist = None
    print("mercariURL:", page)
    return resultlist


if __name__ == '__main__':

    # 検索したいものの名前
    keyword = input("keyword?: ")

    # category_root（親ID）
    category_root = input("category_root?: ")

    # category_child（子ID）
    category_child = input("category_child?: ")

    # 検索範囲（ページ単位）
    search_scope = int(input("search_scope?: "))

    # 検索実行
    mylist = mercariSearch(keyword, category_root,
                           category_child, search_scope)

    # 出力
    print(*mylist, sep='\n')
