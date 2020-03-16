import requests
import re
from bs4 import BeautifulSoup
from pyquery import PyQuery as py
import pymysql

head = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}

proxies = {
    'http': '171.13.201.232:9999',
    'http': '123.169.169.19:9999'
 }

db = pymysql.connect(host="localhost", user="root", passwd="xing1230.", db="test", charset="utf8")  # 连接数据库
#创建数据表
def create_db():  #创建数据表


    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS BOOK_SANQIU") #如果存在book表则删除表重新创建

    sql = """CREATE TABLE BOOK_EPUD (
            ID INT PRIMARY KEY AUTO_INCREMENT,
            TITILE  CHAR(255),
            LINK CHAR(255),
            CODE CHAR(255) )ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""  #设置默认编码为utf-8，charset='utf8' 不能写成utf-8

    cursor.execute(sql)
    print("创建数据库表成功！")

def test():
    url = "https://www.d4j.cn/download.php?id=17144"
    response = requests.get(url, headers=head, proxies=proxies)
    # 获取pyquery对象
    html1 = response.text
    html = py(html1)
    print(html)

def get_book():

    book =[]

    url = "https://sobooks.cc/books/15702.html"

    response = requests.get(url, headers=head, proxies=proxies)
    # 获取pyquery对象
    html1 = response.text
    html = py(html1)

    title = html("body > section > div.content-wrap > div > header > h1 > a").text()
    # 获取百度网盘地址
    link = html("body > section > div.content-wrap > div > div.row.equal > article.col-xs-4.col-sm-3.card-27 > a").attr("href")
    # 获取提取码
    code = html("body > div.wrap > div.content > div.plus_box > div.plus_l > ul > li:nth-child(4) > font").text()

    print(html1)
    # if link:
    #     print("第"+str(i)+"页面")
    #     print(title)
    #     print(link)
    #     print(code)
    #
    #     book.append(title)
    #     book.append(link)
    #     book.append(code)
    #     return book
    # else:
    #     print("第" + str(i) + "页面")

def insert_db(value): #插入数据库

    cursor = db.cursor()
    sql = "INSERT INTO book_sanqiu(TITILE,LINK,CODE) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql,value)
        db.commit()
        # print('插入数据成功')
        cursor.close()
    except:
        db.rollback()
        # print("插入数据失败")
        cursor.close()


if __name__=="__main__":
    # list = ["asd","sdf","fdsf"]
    # insert_db(list)
    get_book()
