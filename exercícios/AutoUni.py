from selenium import webdriver
import pyautogui


pyautogui.PAUSE = 2
# O chromdriver.exe deve estar instalado onde o python tbm está instalado
navegador = webdriver.Chrome()
navegador.get('https://univirtus.uninter.com')
navegador.find_element_by_xpath('//*[@id="ru"]').click()
pyautogui.write("*****")
navegador.find_element_by_xpath('//*[@id="senha"]').click()
pyautogui.write("*****")
pyautogui.press("enter")
navegador.find_element_by_xpath('//*[@id="loginBoxAva"]/i').click()

