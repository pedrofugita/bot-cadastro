import pyautogui
import time
import datetime

pyautogui.PAUSE = 0.3   # faz pausa para alocar o processamento do computador
delay = 5

# CRONÔMETRO
inicio = time.time()
hora_atual = datetime.datetime.now()
print("início: ", hora_atual.strftime('%H:%M:%S'))

# ACESSO AO LINK
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(delay)   # ajustar de acordo com capacidade de processamento do computador
#pyautogui.click(x=1156, y=1056)
#time.sleep(delay)
pyautogui.click(x=685, y=61)
pyautogui.write("https://forms.gle/dsVzFn4GvxwhWNg9A")
pyautogui.press("enter")
time.sleep(5)   # ajustar de acordo com a velocidade da internet

# PREENCHIMENTO
# for i in range(75):
#     print(f'Iteração {i + 1}')

# PESQUISADOR
pyautogui.click(x=767, y=392)   # clica no primeiro campo de preenchimento
pyautogui.write("Matheus fuchs")
pyautogui.press("tab")

# RESIDÊNCIA
pyautogui.write("Barras")
pyautogui.press("tab")

# GÊNERO
pyautogui.press("down")
pyautogui.press("enter")
pyautogui.press("tab")

# FAIXA ETÁRIA
pyautogui.press("down")
pyautogui.press("enter")
pyautogui.press("tab")

# MOBILIDADE
# Localizar um elemento usando XPath
elemento_xpath = "//input[@id='nome_do_elemento']"
elemento = driver.find_element_by_xpath(elemento_xpath)
elemento.send_keys("Texto de exemplo")

# MOTIVO MOBILIDADE


# CONSCIÊNCIA


# VEÍCULOS
    # SIM
    # QUANTIDADE
    # PRETENDE TROCAR
    # CONDIÇÃO FINANCEIRA

    # NÃO