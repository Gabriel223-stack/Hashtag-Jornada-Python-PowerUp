# bibliotecas = pacotes de código
# pip install pyautogui

import pyautogui
import time

# pyautogui.click
# pyautogui.write
# pyautogui.press
# pyautogui.hotkey

# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# abriria o navegador

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.hotkey("ctrl", "alt", "t") # Comando para atalhos
time.sleep(1) # Delay de 1 segundo para abrir o terminal
pyautogui.write("google-chrome")
pyautogui.press("enter")

time.sleep(2)
pyautogui.moveTo(x=881, y=599, duration=0.5)
time.sleep(1)
pyautogui.click()
pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 2: Fazer login
# Clicar no campo de e-mail
pyautogui.moveTo(x=2648, y=518, duration=0.5)
time.sleep(1)
pyautogui.click()
pyautogui.write("gabrielsouza66162@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
# Fazer uma pausa maior pro site carregar
time.sleep(4)

# Passo 3: Abrir a base de dados (importar o arquivo Excel)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.moveTo(x=2549, y=376, duration=0.5)
    codigo = str(tabela.loc[linha, "codigo"]) # Transformar o código em string
    pyautogui.click()
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": # Se a observação não for vazia
        pyautogui.write(obs)
    pyautogui.press("tab") # Passar para o botão enviar

    pyautogui.press("enter") # Clicar no botão enviar
    # voltar para o inicio da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos