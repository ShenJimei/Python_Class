import requests
from lxml import html

def spider(sn, book_list = []):
    """爬取当当网图书信息  9787115428028"""
    url = "http://search.dangdang.com/?key={0}&act=input".format(sn)

    # 获取html中的内容
    html_data = requests.get(url).text

    # xpath 对象
    selector = html.fromstring(html_data)

    # 找到书本的列表
    ul_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')
    print(len(ul_list))

    for li in ul_list:

        # 标题
        title = li.xpath('a/@title')
        print(title[0])

        # 链接
        link = li.xpath('a/@href')

        print(link[0])

        # 价格
        price = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
        price = price[0].replace('¥', '')
        print(price[0])

        # 商铺
        store = li.xpath('p[@class="search_shangjia"]/a/text()')
        store = '当当自营' if len(store) == 0 else store[0]
        print(store)

        print('--------------------------------')

        book_list.append({
            'title': title,
            'price': price,
            'link': link,
            'store': store
        })



if __name__ == '__main__':
    spider(9787115428028)
