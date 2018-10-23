import requests

def spider(sn, book_list = []):
    """爬取淘宝网数据"""
    url = 'https://s.taobao.com/api?ajax=true&m=customized&sourceId=tb.index&q={0}'\
        .format(sn)
    print(url)

    rest = requests.get(url).json()
    bk_list = rest["API.CustomizedApi"]["itemlist"]["auctions"]
    print(len(bk_list))

    # 遍历列表中数据
    for bk in bk_list:

        # 标题
        title = bk["raw_title"]

        # 价格
        price = bk['view_price']

        # 链接
        link = bk['detail_url']

        # 店名
        store = bk['nick']

        print('{title}: {price}: {link}: {store}'
              .format(title = title,
                      price = price,
                      link = link,
                      store = store))
        book_list.append({
            'title': title,
            'price': price,
            'link': link,
            'store': store
        })






if __name__ == '__main__':
    spider(9787115428028)
