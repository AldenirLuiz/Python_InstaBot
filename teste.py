

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

chrome_motor = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_motor)
driver.get('https://www.google.com/')
action = ActionChains(driver) 

inputer = ['definicao piada', 'definicao mapa astral', 'definicao xerecard', 'definicao masturbacao']


def pesquisador(dados):
    elemento_pesquisa = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    driver.get('https://www.google.com/')
    for dado in dados:
        driver.find_element(By.XPATH, elemento_pesquisa).click()
        driver.find_element(By.XPATH, elemento_pesquisa).send_keys(dado)
        sleep(3)
        driver.find_element(By.XPATH, elemento_pesquisa).send_keys(Keys.ENTER)
        print('enter enviado')
        elementos = driver.find_elements(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/span/div/div/div[3]/div/div[3]/div/div/ol/li[1]/div/div/div[1]/div[2]/div/div/div/span')
        print('elementos encontrados')
        print(elementos)
        for element in elementos:
            sleep(2)
            with open('loglist.txt', 'w') as texto:
                print('texto aberto')
                texto.write(f'-' * len(element.text))
                texto.write(f'\n{element.text}')
                texto.write(f'\n')
                print('texto copiado')
                continue
        else:
            elemento_pesquisa = '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input'
            driver.find_element(By.XPATH, elemento_pesquisa).click()
            action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.BACK_SPACE).perform()
            driver.find_element(By.XPATH, elemento_pesquisa).click()
            continue
            
        

pesquisador(inputer)

