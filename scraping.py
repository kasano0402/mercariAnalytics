import requests
import bs4
import re

# 関数


def mercariSearch(keyword, category_root, category_child, search_scope):
    """メルカリで検索する関数
    Arguments:
        keyword {string} -- 検索文字列
        category_root {int} -- カテゴリID（親）
        category_child {int} -- カテゴリID（子）
        search_scope {int} -- 検索範囲
    """
    pagelist = []
    for i in range(1, search_scope):
        page = 'https://www.mercari.com/jp/search/?page={0}&sort_order=created_desc&keyword={1}&category_root={2}&category_child={3}'.format(
            str(i), keyword, category_root, category_child)
        pagelist.append(page)

        resultlist = [["name", "price", "status", "link", "photo"]]
        for page in pagelist:
            headers = {
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/50.0.2661.102 Safari/537.36'}
            res = requests.get(page, headers=headers)
            # エラーチェック
            res.raise_for_status()

            # スクレイピング
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            elems_name = soup.select('.items-box-name')
            elems_price = soup.select('.items-box-price')
            elems_photo = soup.select('.items-box-photo')
            elems_url = soup.select('.items-box > a')
            elems_photo_url = soup.select('.items-box-photo > img')

            for i in range(len(elems_name)):
                new_elems_name = elems_name[i].text.replace(",", "")
                new_elems_price = elems_price[i].text.replace(
                    ",", "").replace("¥ ", "")
                new_elems_photo = re.search(
                    'figcaption', str(elems_photo[i].__str__))
                new_elems_url = elems_url[i].get("href")
                new_elems_photo_url = elems_photo_url[i].get("data-src")

                # リストに挿入
                if new_elems_photo:
                    resultlist.append(
                        [new_elems_name.replace("\u3000", ""), new_elems_price, "sold", new_elems_url, new_elems_photo_url])
                else:
                    resultlist.append(
                        [new_elems_name.replace("\u3000", ""), new_elems_price, "", new_elems_url, new_elems_photo_url])
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

    print(*mylist, sep='\n')
