# Pre Requisites:
#  Botting Process -> Selenium
#  pip3 install selenium
#  Geko driver - Firefox
#  Chrome driver
#  brew install chromedriver

from selenium import webdriver

url = 'https://www.lncc.br/~borges/php/testar.html'
driver = webdriver.Chrome()
driver.get(url)

# clicar em inspecionar no input
# ao abrir a html clicar com botão direito onde está highlight em 
# Copy > Copy Xpath

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys("Hello World")

showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')

additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('12')

getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()