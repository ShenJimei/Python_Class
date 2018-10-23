from spider_dangdang import spider as dangdang
from spider_taobao import spider as taobao
from spider_jd import spider as jd


def main(sn):
    """图书比价工具"""
    book_list = []

    # 当当网
    dangdang(sn, book_list)
    print('当当网数据爬取成功')

    # 京东

    jd(sn, book_list)
    print('京东网数据爬取成功')

    # 淘宝
    taobao(sn, book_list)
    print('淘宝网数据爬取成功')





    # 遍历
    for book in book_list:
        print(book)


    print('++++++++++++++++++++++++++开始排序++++++++++++')

    # book_list = sorted(book_list, key = lambda item : float(item["price"]))
    book_list = sorted(book_list, key=lambda item: float(item["price"][0]), reverse=True)

    for book in book_list:
        print(book)


if __name__ == '__main__':
    sn = input('请输入图书编号: ')
    main(sn)
