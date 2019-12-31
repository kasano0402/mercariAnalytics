import requests
import bs4
import re

# 関数


def mercariSearch(search_word, category_root, category_child, scope,
                  sort_order):
    """メルカリで検索する関数
    Arguments:
        search_word {string} -- 検索文字列
        category_root {int} -- カテゴリID（親）
        category_child {int} -- カテゴリID（子）
        scope {int} -- 検索範囲
        sort_order {string} -- 検索結果表示順序
    """
    pagelist = []
    for i in range(1, scope):
        page = 'https://www.mercari.com/jp/search/?page={0}&sort_order={1}&keyword={2} & category_root = {3} & category_child = {4}'.format(
            str(i), sort_order, search_word, category_root, category_child)
        pagelist.append(page)

    with open('product.csv', 'w', encoding="utf-8") as f:
        f.write('name,price,elem' + "\n")
        for page in pagelist:
            headers = {
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/50.0.2661.102 Safari/537.36'}
            res = requests.get(page, headers=headers)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            elems_name = soup.select('.items-box-name')
            elems_price = soup.select('.items-box-price')
            elems_photo = soup.select('.items-box-photo')
            for i in range(len(elems_name)):
                new_elems_name = elems_name[i].text.replace(",", "")
                new_elems_price = elems_price[i].text.replace(
                    ",", "").replace("¥ ", "")
                new_elems_photo = re.search(
                    'figcaption', str(elems_photo[i].__str__))
                if new_elems_photo:
                    f.write(new_elems_name + "," + new_elems_price +
                            "," + new_elems_photo.group(0) + "\n")
                else:
                    f.write(new_elems_name + "," +
                            new_elems_price + "," + "" + "\n")


if __name__ == '__main__':
    # ソート方法
    sort_order = "created_desc"

    # 検索したいものの名前
    search_word = input("search_word?: ")

    # category_root（親ID）
    category_root = input("category_root?: ")

    # category_child（子ID）
    category_child = input("category_child?: ")

    # 検索範囲（ページ単位）
    how_many_page = input("how_many_page?: ")
    how_many_page = int(how_many_page)

    # 検索実行
    mercariSearch(search_word, category_root,
                  category_child, how_many_page, sort_order)
