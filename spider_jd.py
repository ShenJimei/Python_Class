import requests
from lxml import html

def spider(sn, book_list = []):
    """爬取京东图书数据"""
    url = 'https://search.jd.com/Search?keyword={sn}'\
        .format(sn=sn)
    # 获取html文档
    resp = requests.get(url)
    resp.encoding = 'UTF-8'
    html_data = resp.text
    # print(html_data)

    # 获取xpath对象
    selector = html.fromstring(html_data)

    # 找到书本的列表
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    print(len(ul_list))

    # 解析对应的内容
    for li in ul_list:
        # 标题
        title = li.xpath('div/div[@class="p-name"]/a/@title')
        print(title[0])

        # 购买链接
        link = li.xpath('div/div[@class="p-name"]/a/@href')
        print('https:' + link[0])

        # 价格
        price = li.xpath('div/div[@class="p-price"]/strong/i/text()')
        print(price[0])

        # 店铺
        store = li.xpath('div/div[@class="p-shopnum"]/a[@class="curr-shop"]/@title')
        print(store[0])

        book_list.append({
            'title': title,
            'price': price,
            'link': link,
            'store': store
        })
if __name__ == '__main__':
    spider(9787115428028)
