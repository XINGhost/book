import threading
import time
t1 = time.localtime()
from sanqiu import get_book, insert_db

lock=threading.Lock() #申请锁

# 起始页面
begin_page = 17000
# 终止页面
end_page = 18000
range_num = int((end_page - begin_page) / 3)  #有多少个线程除以多少
def work1():
    global lock
    global begin_page
    for i in range(range_num):

        begin_page += 1
        book = get_book(begin_page)  #获得书籍
        lock.acquire()  # 加锁
        insert_db(book)  # 插入到数据库
        lock.release()
    print("in work1 g_num is : %d" % begin_page)

def work2():
    global lock
    global begin_page
    for i in range(range_num):  #设置进程结束条件
        begin_page += 1
        book = get_book(begin_page)  # 获得书籍
        lock.acquire()  # 加锁
        insert_db(book)  # 插入到数据库
        lock.release()
    print("in work2 g_num is : %d" % begin_page)

def work3():
    global lock
    global begin_page
    for i in range(range_num):  #设置进程结束条件
        begin_page += 1
        book = get_book(begin_page)  # 获得书籍
        lock.acquire()  # 加锁
        insert_db(book)  # 插入到数据库
        lock.release()
    print("in work2 g_num is : %d" % begin_page)

if __name__ == '__main__':

    t1 = threading.Thread(target=work1)
    t1.start()
    t2 = threading.Thread(target=work2)
    t2.start()
    t3 = threading.Thread(target=work2)
    t3.start()
