from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Instala o ChromeDriver automaticamente e inicializa o navegador
navegador = webdriver.Chrome()

navegador.get('https://www.youtube.com/')
time.sleep(150)

