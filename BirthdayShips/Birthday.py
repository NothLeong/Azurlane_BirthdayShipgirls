#制作人：Noth
#数据来源:碧蓝航线wiki:https://wiki.biligame.com/blhx
import time
import requests
from bs4 import BeautifulSoup

#获取本地日期
local_month = time.localtime().tm_mon
local_day = time.localtime().tm_mday

#获取wiki中舰船生日网址
url = 'https://wiki.biligame.com/blhx/舰船生日'
html = requests.get(url)
html.encoding = 'utf-8'

#解析
soup = BeautifulSoup(html.text,'lxml')
table = soup.find('table',id='CardSelectTr')
products = table.find_all('tr')[1:len(table.find_all('tr'))]
bir_ships = []

#遍历
for row in products:
    td_list = row.find_all('td')
    month = td_list[3].contents[0]
    day = td_list[4].contents[0]
    if month.isdigit() and int(month)==local_month:
        if day.isdigit() and int(day)==local_day:
            name = td_list[1].find('a').get('title')
            bir_ships.append(name)

if len(bir_ships)==0:
    print("今日没有小寿星")
else:
    print("今日小寿星：",end='')
    for name in bir_ships:print(name,end=' ')

#("今天是"+str(local_month)+"月"+str(local_day)+"日")
