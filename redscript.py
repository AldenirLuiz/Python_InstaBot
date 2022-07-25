
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

chrome_motor = 'chromedriver.exe'
diretorio = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "./download"}
diretorio.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=chrome_motor, chrome_options=diretorio)

driver.get('https://www.redtube.com.br/')
action = ActionChains(driver) 

classNameThumbVideo=f'/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/ul/li[2]/div/span[1]/a/picture/img'
scriptPlayerConfig='tm_pc_player_setup'

def pesquisador():
    try:
        print('try')
        for elemento in range(2, 20):
            if driver.find_elements(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/ul/li[2]'):
                print('elemento encontrado')
                driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/ul/li[2]').click()
                print('elemento aberto')
                sleep(6)
                try:
                    if driver.find_element(By.ID, scriptPlayerConfig):
                        print('script encontrado')
                        scriptPlayer = driver.find_element(By.ID, scriptPlayerConfig).get_dom_attribute
                        print(scriptPlayer)
                        print(driver.find_element(By.ID, scriptPlayerConfig).text)
                        sleep(5)
                        with open('loglist.txt', 'w') as scText:
                            print('texto aberto')
                            scText.write(scriptPlayer)
                            print('texto copiado')
                            print(scText)
                            sleep(5)
                except:
                    continue
            else:
                sleep(3)
                continue
    except:
        return 'erro'
    
    
pesquisador()