import pyautogui
import time
import datetime

pyautogui.PAUSE = 0.5   # faz pausa para alocar o processamento do computador

# CRONÔMETRO
inicio = time.time()
hora_atual = datetime.datetime.now()
print("início: ", hora_atual.strftime('%H:%M:%S'))

# ACESSO AO LINK
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(8)   # ajustar de acordo com capacidade de processamento do computador
pyautogui.click(x=685, y=61)
pyautogui.write("https://forms.gle/dsVzFn4GvxwhWNg9A")
pyautogui.press("enter")
time.sleep(8)   # ajustar de acordo com a velocidade da internet

# PREENCHIMENTO
contador_iteracao = 0
for i in range(0, 45):
    contador_iteracao += 1
    print(f"iteração {contador_iteracao} concluída")

    # PESQUISADOR
    pyautogui.click(x=805, y=391)
    pyautogui.write("Matheus fuchs")
    pyautogui.press("tab")

    # RESIDÊNCIA
    # if i <= 20:
    #     pyautogui.write("Passeio Caconde")
    #     pyautogui.press("tab")
    if i <= 6:
        pyautogui.write("Passeio Itu")
        pyautogui.press("tab")
    else:
        pyautogui.write("Passeio Sorocaba")
        pyautogui.press("tab")

    # GÊNERO
    if i % 2 == 0:                                  # 50% homem PAR
        pyautogui.press("space")
        pyautogui.press("tab")
    else:                                           # 50% mulher ÍMPAR
        pyautogui.press("down")
        pyautogui.press("space")
        pyautogui.press("tab")

    # FAIXA ETÁRIA
    # if i <= 19:
    #     pyautogui.press("down")
    #     pyautogui.press("down")
    #     pyautogui.press("tab")
    #
    # elif 19 < i <= 38:
    #     pyautogui.press("down")
    #     pyautogui.press("down")
    #     pyautogui.press("down")
    #     pyautogui.press("tab")

    if i <= 7:
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("tab")

    elif 7 < i <= 26:
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("tab")

    else:
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("tab")

    # MOBILIDADE
    # if i <= 21:                                     # A PÉ 23%
    #     pyautogui.press("space")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    # elif 21 < i <= 45:                              # BICICLETA 25%
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    #     pyautogui.press("space")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    if i <= 20:                              # MOTOCICLETA 25%
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("space")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
    elif 20 < i <= 44:                              # AUTOMÓVEL 25 %
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("space")
        pyautogui.press("tab")
    else:                                           # ÔNIBUS 2%
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("space")
        pyautogui.press("tab")
        pyautogui.press("tab")

    # MOTIVO MOBILIDADE
    # if i <= 46:                                     # ESTUDO 48%
    #     pyautogui.press("space")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    #     pyautogui.press("tab")
    if i <= 44:                              # TRABALHO 50
        pyautogui.press("tab")
        pyautogui.press("space")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
    else:                                           # SAÚDE 2%
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("space")
        pyautogui.press("tab")
        pyautogui.press("tab")

    # CONSCIÊNCIA
    pyautogui.press("space")
    pyautogui.press("tab")

    # VEÍCULOS
    if i < 100:                                     # sim AUTOMÓVEL E MOTOCICLETA 50%
        pyautogui.press("space")
        pyautogui.press("tab")

        # CLICA EM "PRÓXIMA"
        pyautogui.press("enter")
        time.sleep(8)

        # QUANTIDADE                                # sim 100%
        pyautogui.click(x=638, y=429)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")

        # PRETENDE TROCAR                           # sim 100%
        pyautogui.press("space")
        pyautogui.press("tab")

        # CONDIÇÃO FINANCEIRA                       # não 100%
        pyautogui.press("down")

        # ENVIAR FORMULÁRIO
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(8)

        # ENVIAR OUTRA RESPOSTA
        pyautogui.click(x=694, y=251)
        time.sleep(8)

    # if i <= 47:                                     # não 50%
    #     pyautogui.press("down")
    #     pyautogui.press("tab")
    #
    #     # CLICA EM "PRÓXIMA"Matheus fuchs   Passeio Itu
    #     pyautogui.press("enter")
    #     time.sleep(8)
    #
    #     # ENVIAR FORMULÁRIO
    #
    #     pyautogui.click(x=769, y=286
    #                     )
    #     time.sleep(8)
    #
    #     # ENVIAR OUTRA RESPOSTA
    #     pyautogui.click(x=694, y=251)
    #     time.sleep(8)