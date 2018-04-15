# coding: utf8
# -*- coding: utf-8 -*- 
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import alert
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

path = 'index.html'

with open(path, 'w', encoding='utf-8') as output_file:
  output_file.write("""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <link rel="shortcut icon" href="img/Favicon.ico" type="image/x-icon">
  <title>Эскалация</title>
  <link href="https://fonts.googleapis.com/css?family=PT+Sans:400,700&amp;subset=cyrillic" rel="stylesheet">
  <link href="css/main.css" rel="stylesheet">
</head>
<body>
  <img class="logo" src="img/edi.png" width="200" height="38" alt="Kontur.EDI">
  <div class="main-tree">""")

print('ПОЖАЛУЙСТА, ПОДОЖДИТЕ...')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'driver\chromedriver.exe')
driver.get('https://wic.skbkontur.ru/knowledges/c75966a5-0da5-42f9-adb2-9a2df2bcaf15')
# driver.get('https://wic.skbkontur.ru/knowledges/29cd4474-4e08-4987-9c6b-11f60c288f58')
driver.find_element_by_xpath("""//*[@id="username1"]""").send_keys('*****')
driver.find_element_by_xpath("""//*[@id="password1"]""").send_keys('*****')
driver.find_element_by_xpath("""//*[@id="tab1"]/form/div[3]/div[2]/button""").click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.alert_is_present())
alert.Alert(driver).accept()

"""ДОЖДАТЬСЯ ПОЯВЛЕНИЯ ОБЪЕКТА"""
time.sleep(3)

posts = driver.find_elements_by_class_name('tabs__anchor')
TS = []
for post in posts:
  if post.text.isdigit()==True:
    with open(path, 'a', encoding='utf-8') as output_file:
      output_file.write("<span class='main-tree__element main-tree__first-element'>"+post.text+"</span>")
      output_file.write("<div class='main-tree__line line__visible line__visible--always'>")
  else:
    TS.append(post.text)

for i in range(1, len(TS)+1):
  with open(path, 'a', encoding='utf-8') as output_file:
    output_file.write("<span id='" + str(i) + "' class='main-tree__element'>"+TS[i-1]+"</span>")

soluts = []
for post in posts:
  if post.text.isdigit()==True:
    pass
  else:
    post.click()
    solutions = driver.find_elements_by_css_selector("[data-bind='html: html']")
    for solution in solutions:
      if solution.text.strip() != "":
        soluts.append(solution.text.strip())

for i in range(1, len(soluts)+1):#сейчас len(TS)==len(soluts), но возможно и другое, два фора, чтобы прописывать див для дочек
  with open(path, 'a', encoding='utf-8') as output_file:
    output_file.write("<div class='"+str(i)+"__inner main-tree__line'>")
    output_file.write("<span id='"+str(i)+"."+str(i)+"' class='main-tree__element'>"+soluts[i-1]+"</span>")
    output_file.write("</div>")

with open(path, 'a', encoding='utf-8') as output_file:
  output_file.write("</div>")

with open(path, 'a', encoding='utf-8') as output_file:
  output_file.write("""<div class="textarea-block">
    <textarea class="textarea-block__text" rows="25">В чём проблема?</textarea>
    <button class="textarea-block__button" type="button">Копировать</button>
  </div>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>
  <script src="js/main.js"></script>
</body>
</html>""")

driver.quit()