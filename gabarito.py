# Passo 1: Entrar no sistema da empresa
import pyautogui
import time
import datetime

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3   # faz pausa para alocar o processamento do computador

# contador de tempo
inicio = time.time()
hora_atual = datetime.datetime.now()
print("início: ", hora_atual.strftime('%H:%M:%S'))

# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=1201, y=1060)
time.sleep(5)   # ajustar de acordo com capacidade de processamento do computador

# entrar no link
pyautogui.click(x=685, y=61)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(8)   # ajustar de acordo com a velocidade da internet


# Passo 2: Fazer login
pyautogui.click(x=902, y=360)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)


# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: loop para cadastrar produtos
for linha in tabela.index:
    pyautogui.click(x=774, y=249)   # clica no primeiro campo de preenchimento
    codigo = tabela.loc[linha, "codigo"]    # pegar da tabela o valor do campo que a gente quer preencher
    pyautogui.write(str(codigo))    # str transforma em texto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))    # formato que não cria variável
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]  # cria variável obs para nao preencher 'NaN'
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima (número positivo -> scroll para cima)
    #pyautogui.scroll(5000)

fim = time.time()
tempo_total = fim - inicio
minutos = int(tempo_total // 60)
segundos = int(tempo_total % 60)
print("Cadastro concluído")
hora_atual = datetime.datetime.now()
print("fim: ", hora_atual.strftime('%H:%M:%S'))
print(f"Tempo decorrido: {minutos} minutos e {segundos} segundos.")


