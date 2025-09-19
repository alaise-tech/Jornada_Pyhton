import pyautogui
import time


# pyautogui.click -> Clicar em algum lugar da tela
# pyautogui.press -> Pressionar uma tecla
# pyautogui.write -> Escrever algo
# pyautogui.hotkey -> Pressionar uma combinação de teclas


pyautogui.PAUSE = 0.5  # segundo de pausa após cada comando

# Passo 1 : Entratr no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login 
#abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#abrir o site
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press("enter")

# esperar 3 segundos
time.sleep(3)

# Passo 2 : Fazer Login
pyautogui.click(x=253, y=316) # clicar no email
pyautogui.write("alaisecaetano34@gmail.com")

#preencher senha
pyautogui.press("tab")
pyautogui.write("Alaise1234!")

#botao logar
pyautogui.press("tab")
pyautogui.press("enter")

# esperar 3 segundos
time.sleep(3)


# Passo 3 : Importar a base de dados
import pandas
import os

caminho = "C:/Users/Alaise Caetano/OneDrive/Desktop/Jornada_Python/Python_Power_Up/produtos.csv"

if os.path.exists(caminho):
    tabela = pandas.read_csv(caminho)
    print(tabela)
else:
    print(f"Arquivo não encontrado: {caminho}")
    exit()  # Encerra o programa se o arquivo não for encontrado

# Função para limpar o campo e escrever novo valor
def limpar_e_escrever(texto):
    import pyautogui
    pyautogui.hotkey("ctrl", "a")  # Seleciona tudo
    pyautogui.press("backspace")   # Apaga o conteúdo
    pyautogui.write(str(texto))    # Escreve o novo valor



# Passo 4 : Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=187, y=230)  # campo código
    limpar_e_escrever(tabela.loc[linha, "codigo"])

    pyautogui.press("tab")  
    limpar_e_escrever(tabela.loc[linha, "marca"])

    pyautogui.press("tab")
    limpar_e_escrever(tabela.loc[linha, "tipo"])

    pyautogui.press("tab")
    limpar_e_escrever(tabela.loc[linha, "categoria"])

    pyautogui.press("tab")
    limpar_e_escrever(tabela.loc[linha, "preco_unitario"])

    pyautogui.press("tab")
    limpar_e_escrever(tabela.loc[linha, "custo"])

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        limpar_e_escrever(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)



# Passo 5 : Repetir para todos os produtos

#nan --> Not a number --> valor vazio
