from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import json
import requests

url = 'https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Fcontacts.google.com%2F&followup=https%3A%2F%2Fcontacts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
browser = webdriver.Firefox(firefox_binary=binary,
                            executable_path=r"C:\\geckodriver.exe")
browser.get(url)


# pegar o campo de busca onde podemos digitar algum termo
email_box = browser.find_element_by_id('identifierId')
# Digitar "informe o e-mail" no campo de busca
email_box.send_keys('kaioeduardoescar@gmail.com')
# Simular que o enter seja precisonado
email_box.send_keys(Keys.ENTER)
sleep(15)


search_box = browser.find_element_by_class_name('Ax4B8')
search_box.send_keys('daniel bispo')
search_box.send_keys(Keys.ENTER)

