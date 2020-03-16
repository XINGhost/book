from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

# 设置selenium的运行参数
option=webdriver.ChromeOptions()
option.add_argument('headless') # 设置optio，后台
driver = webdriver.Chrome(chrome_options=option)  # 调用带参数的谷歌浏览器

# 访问网址
driver.get("https://sobooks.cc/books/15700.html")

input = driver.find_element_by_xpath('/html/body/section/div[2]/div/article/div[2]/form/input[1]').send_keys("20191212")
driver.find_element_by_xpath('/html/body/section/div[2]/div/article/div[2]/form/input[1]').send_keys(Keys.ENTER)

cookies = driver.get_cookies()
js = json.dumps(cookies)
cookie = {}
def write_cookies():
    with open(r'd:\Desktop\test.json', 'w') as f:
        f.write(js)

def read_cookies():
    with open(r'd:\Desktop\test.json', 'r') as f:
        cookie = f.read()
        cookie = json.loads(cookie)

print(cookies)
write_cookies()
driver.close()

if __name__=="__main__":
    write_cookies()