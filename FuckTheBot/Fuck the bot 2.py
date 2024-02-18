from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import datetime
import pyautogui

# ATUALIZA WEBDRIVER DO SELENIUM
servico = Service(ChromeDriverManager().install())

# CRONÔMETRO
inicio = time.time()
hora_atual = datetime.datetime.now()
print("início: ", hora_atual.strftime('%H:%M:%S'))

# ACESSA O LINK
navegador = webdriver.Chrome(service=servico)
navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSentKSrewab3ZPz-TZKdNaxtrQ_Vxp3488rv93TEutsOvQJug/viewform?usp=sf_link")
time.sleep(3)

# LOGIN
pyautogui.click(x=583, y=642)
time.sleep(3)
pyautogui.write("matheusfuchs27@gmail.com")
pyautogui.press("enter")
time.sleep(5)

# # LOGIN
# navegador.find_element('xpath',
#                        '/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span').click()     # FAZER LOGIN
# time.sleep(5)
# navegador.find_element('xpath',
#                        '//*[@id="identifierId"]').send_keys("matheusfuchs27@gmail.com", Keys.ENTER) # EMAIL
# time.sleep(5)
# navegador.find_element('xpath',
#                        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("maf15052004", Keys.ENTER) # SENHA
#
# time.sleep(5)
# navegador.find_element('xpath',
#                        '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div/div[2]/div[4]/div[1]/button/span').click()     # AGORA NÃO
# time.sleep(5)

# PREENCHIMENTO
contador_iteracao = 0
for i in range(1, 96):
    contador_iteracao += 1
    print(f"iteração {contador_iteracao}")

    # PESQUISADOR
    navegador.find_element('xpath',
                           '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Matheus fuchs")

    # RESIDÊNCIA
    if i <= 20:
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Passeio Caconde")
    if i > 55:
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Passeio Sorocaba")
    else:
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Passeio Itu")

    # GÊNERO
    if i % 2 == 0:                                  # 50% homem PAR
        navegador.find_element('xpath',
                               '//*[@id="i20"]/div[3]/div').click()
    else:                                           # 50% mulher ÍMPAR
        navegador.find_element('xpath',
                               '//*[@id="i23"]/div[3]/div').click()

    # FAIXA ETÁRIA
    if i <= 19:
        navegador.find_element('xpath',
                               '//*[@id="i36"]/div[3]/div').click()
    elif 19 < i <= 38:
        navegador.find_element('xpath',
                               '//*[@id="i39"]/div[3]/div').click()
    elif 38 < i <= 57:
        navegador.find_element('xpath',
                               '//*[@id="i42"]/div[3]/div').click()
    elif 57 < i <= 76:
        navegador.find_element('xpath',
                               '//*[@id="i45"]/div[3]/div').click()
    else:
        navegador.find_element('xpath',
                               '//*[@id="i48"]/div[3]/div').click()

    # MOBILIDADE
    if i <= 21:                                     # A PÉ 23%
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[1]/label').click()
    elif 21 < i <= 45:                              # BICICLETA 25%
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[3]/label').click()
    elif 45 < i <= 69:                              # MOTOCICLETA 25%
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[4]/label').click()
    elif 69 < i <= 93:                              # AUTOMÓVEL 25 %
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[6]/label').click()
    else:                                           # ÔNIBUS 2%
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[5]/label').click()

    # MOTIVO MOBILIDADE
    if i <= 46:                                     # ESTUDO 48%
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label').click()
    elif 46 < i <= 93:                              # TRABALHO 50
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label').click()
    else:                                           # SAÚDE 2%
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label').click()

    # CONSCIÊNCIA
    navegador.find_element('xpath',
                           '//*[@id="i98"]/div[3]/div').click()

    # VEÍCULOS
    if i <= 47:                                     # sim AUTOMÓVEL E MOTOCICLETA 50%
        navegador.find_element('xpath',
                               '//*[@id="i108"]/div[3]/div').click()
        # CLICA EM "PRÓXIMA"
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        # QUANTIDADE                                # sim 100%
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/label').click()
        # PRETENDE TROCAR                           # sim 100%
        navegador.find_element('xpath',
                               '//*[@id="i22"]/div[3]/div').click()
        # CONDIÇÃO FINANCEIRA                       # não 100%
        navegador.find_element('xpath',
                               '//*[@id="i38"]/div[3]/div').click()
        # ENVIAR FORMULÁRIO
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()

    if i <= 47:                                     # não 50%
        navegador.find_element('xpath',
                               '//*[@id="i111"]/div[3]/div/div').click()
        # CLICA EM "PRÓXIMA"
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        # ENVIAR FORMULÁRIO
        navegador.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span').click()