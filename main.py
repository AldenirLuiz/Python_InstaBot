
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import elements


"""Verifique a versao do seu browser se e compativel com o webdriver.
    faca download do webdriver no site do seu browser. 
    ex:https://chromedriver.storage.googleapis.com/index.html?path=103.0.5060.134/
    
    Os elementos do instagram podem mudar periodicamente, sendo necessario alterar os caminhos
    voce pode alterar o caminho dos elementos no pacote elements.py
    substitua os caminhos de acordo com a sua descricao do elemento.

Returns:
    _type_: _description_
"""

chrome_motor = 'chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chrome_motor)

action = ActionChains(webdriver)
webdriver.get('https://www.instagram.com/accounts/login')
sleep(3)

hashtag = ['amor', 'saúde', 'esperanca', 'tiktok']
seguidos = list()


def home():
    for x in range(4):
        try:
            webdriver.get('https://www.instagram.com/')
            pesquisar(hashtag)
        except: continue
        
    
def loggin_insta(_user, _passw):
    # 3 tentativas para adicionar os dados de login aos campos
    for _ in range(3):
        try: # Tenta obter o status de erro, se houver a etapa de login nao sera feita, pula caso nao aja um status valido.
            bypass = webdriver.find_element(By.ID, 'slfErrorAlert').text
            if bypass in elements._retornos_ErrConect: # busca o status nos erros de conexao, caso haja.
                print(elements.retornos['bloqueio'])
                print(f'\nStatus: {bypass}\n')
                return 'ERR_STTS_BLQ_MIN'
            elif bypass in elements._retorno_ErrLogin: # busca o status nos erros de login, caso haja.
                print(elements.retornos['dados_invalidos'])
                return 'ERR_STTS_DDS_INV'
            else:
                print(f'\nStatus: {bypass}\n')
                print(f'\nTentativa ({_ + 1}) Aguarde 5 segundos\n')
                sleep(randint(1, 4))
                webdriver.refresh()
        except:
            sleep(1)
            # campos de usuario e senha para login
            webdriver.find_element(By.NAME, 'username').send_keys(_user)
            sleep(randint(1, 2))
            webdriver.find_element(By.NAME, 'password').send_keys(_passw)
            sleep(randint(1, 3))
            err_count = 0
            for _ in range(4):
                err_count += 1
                try: # botao de login
                    webdriver.find_element(By.XPATH, elements.elementos['bt_login']).click()
                    sleep(randint(1, 2))
                    pass
                except:
                    if err_count < 3:
                        continue
                    else:
                        break
            try:
                bypass = webdriver.find_element(By.ID, 'slfErrorAlert').text
                if bypass in elements._retornos_ErrConect or bypass in elements._retorno_ErrLogin:
                    continue
            except:
                sleep(randint(1, 4))
                return 'STTS_PASSED'
    else:
        print('ERRO de Login.')
        webdriver.close()
        
        
def bypass_popup():
    '''passa pelo pupup inicial'''
    try:
        webdriver.find_element(By.XPATH, elements.elementos['agora nao']).click()
        sleep(randint(1,3))
        webdriver.find_element(By.CSS_SELECTOR, elements.elementos['bypass']).click()
        sleep(randint(2,4))
        pesquisar(hashtag)
    except:
        return

def pesquisar(dados):
    '''Requer uma lista com os dados a serem pesquisados.
    Os dados de pesquisa devem ser do tipo string!'''
    for dado in dados:
        sleep(randint(1, 2))
        try:
            #ativa o campo de pesquisa
            webdriver.get(f'https://www.instagram.com/explore/tags/{dado}')
            print('pesquisa ok')
            print(f'hashtag: {dado}')
            if select_pesquisa() == 'ok':
                print('--> pesquisa ok')
                continue
        except:
            continue
    else:
        if webdriver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]'):
            webdriver.refresh()
            home()


def select_pesquisa():
    for tentativa in range(4):
        sleep(randint(1, 2))
        try: # Tenta abrir o primeiro bitmap.
            print(f'passP {tentativa} ts')
            webdriver.find_element(By.XPATH, elements.elementos[f'bitmap{randint(1, 6)}']).click()
            print(f'passP {tentativa} ok')
            print('Bitmap ok')
            if seguir() == 'ok':
                print('--> seguir')
                return 'ok'
        except:
            continue
    else:
        if webdriver.find_elements(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]'):
            webdriver.refresh()
            home()


def seguir():
    print('seguir')
    for tentativa in range(4):
        try:
            print('try')
            sleep(randint(2,4))
            seguirB = webdriver.find_element(By.XPATH, elements.elementos['seguir1']).text
            print(f'A seguir {seguirB}')
            if  seguirB == 'Seguir':
                print(f'\nseguir t {tentativa}')
                webdriver.find_element(By.XPATH, elements.elementos['seguir1']).click()
                print(f'\nseguir t {tentativa} ok T{tentativa}')
                sleep(randint(1, 5))
                action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
                sleep(randint(1,4))
                continue
            else:
                action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
                print(f'\nproximo1')
                continue
        except:
            action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
            print(f'\nproximo2')
    else:
        return 'ok'
                
        
def chamar():
    if loggin_insta('seuUsuario@gmail.com', 'sua_senha') == 'STTS_PASSED':
        bypass_popup()
    else:
        webdriver.close()
chamar()