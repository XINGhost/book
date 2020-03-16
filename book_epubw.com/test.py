from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 设置selenium的运行参数
option=webdriver.ChromeOptions()
option.add_argument('headless') # 设置optio，后台
driver = webdriver.Chrome(chrome_options=option)  # 调用带参数的谷歌浏览器

# 访问网址
driver.get("https://sobooks.cc/books/15700.html")

#获取标题
a = driver.find_element_by_xpath('/html/body/section/div[2]/div/header/h1/a')
title = a.text
print(title)

# 获取下载链接
a = driver.find_element_by_xpath('/html/body/section/div[2]/div/article/table/tbody/tr[3]/td/a[1]')
str1 = a.get_attribute('href')
link = str1.split("=")[1]
print(link)

#获取验证码
input = driver.find_element_by_xpath('/html/body/section/div[2]/div/article/div[2]/form/input[1]').send_keys("20191212")
driver.find_element_by_xpath('/html/body/section/div[2]/div/article/div[2]/form/input[1]').send_keys(Keys.ENTER)
if input:
    driver.find_element_by_xpath('/html/body/section/div[2]/div/article/div[2]/form/input[1]').send_keys(Keys.ENTER)
else:
    a = driver.find_element_by_xpath('/html/body/section/div[2]/div/article/div[2]/b')
    str2 = a.text
    str3 = "".join(str2)  #list转为string
    code = str3.split("：")[1]
    print(code)

# 关闭浏览器
driver.close()
