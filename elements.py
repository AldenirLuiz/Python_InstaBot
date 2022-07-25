
elementos = {
    # botao de login
    'bt_login' : '//*[@id="loginForm"]/div/div[3]/button/div',
    # botao do popup inicial ativar notificacoes.
    'bypass': '//*[@id="mount_0_0_K/"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]',
                #'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm',
    # primeiro bitmap do resultado da pesquisa por hashtag.
    'bitmap1': '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]',
    # segundo bitmap do resultado da pesquisa por hashtag.
    'bitmap2': '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div[1]/div[2]',
    # terceiro bitmap do resultado da pesquisa por hashtag.
    'bitmap3': '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[3]/a/div[1]/div[2]',
    # quarto bitmap do resultado da pesquisa por hashtag.
    'bitmap4': '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div[1]/div[2]',
    # quinto bitmap do resultado da pesquisa por hashtag.
    'bitmap5': '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[2]/div[2]/a/div[1]/div[2]',
    # sexto bitmap do resultado da pesquisa por hashtag.
    'bitmap6': '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[2]/div[3]/a/div[1]/div[2]',
    # campo de pesquisa inicial, ativar.
    'campo_pesquisa1': '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.QY4Ed.P0xOK > div.cTBqC',
    # campo de pesquisa inicial, digitar.
    'campo_pesquisa2': '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.QY4Ed.P0xOK > input',
    # primeiro resultado do campo de pesquisa inicial
    'campo_pesquisa3': '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div',
    # link seguir pessoa na thumb
    'seguir1': '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div',
              #/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div
    'seguir2': '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button',
    'divscreen': '/html/body/div[6]/div[1]/button/div/svg',
    # botao proximo thumb
    'proximo': '/html/body/div[6]/div[2]/div/div[2]/button/div/span/svg',
    'agora nao': '//*[@id="react-root"]/section/main/div/div/div/div/button'
                 #/html/body/div[1]/section/main/div/div/div/div/button
}

_retornos_ErrConect = [
    'Aguarde alguns minutos antes de tentar novamente.',
    'Não foi possível se conectar ao Instagram. Verifique se você está conectado à Internet e tente novamente.']
_retorno_ErrLogin = [
    'Sua senha está incorreta. Confira-a.',
    'O nome de usuário inserido não pertence a uma conta. Verifique seu nome de usuário e tente novamente.']

retornos = {
    'bloqueio': '\nO servidor bloqueou por ecesso de tentativas, tente novamente em alguns minutos.\n',
    'dados_invalidos': '\nDados de login Invalidos. Impossivel Prosseguir\n'
}

#'{"format":"mp4","videoUrl":"https:\/\/
#/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/ul/li[2]/div/span[1]/a/picture/img
#/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/ul/li[2]/div/span[1]/a/picture/img
#/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/ul/li[3]/div/span[1]/a/picture/img
#/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/ul/li[4]/div/span[1]/a/picture/img
#/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/ul/li[9]/div/span[1]/a/picture/img
#https://www.redtube.com.br/media/hls?s=eyJ2a2V5IjozOTU4OTA5MSwicyI6IjNkYWM3NWIyMzRkNmNmNGY4MGZjMDRmYjE3MWNlOTA5MmJjMTE3NjYwNjBmYTU5ZWE4MjkzNjEyNGVhY2E3MzIiLCJndCI6MTY1MjQ3OTQ3Nn0
#
