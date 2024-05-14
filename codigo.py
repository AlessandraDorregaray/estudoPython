# Passo a passo do projeto

# Abrir o sitema da empresa
    # abrir um navegador
    # abrir o site da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# biblioteca que simula         
# Fazer login
# Importar a base de dados de produto para cadastrar
# Cadastrar um produto
# Repetir até acabar a lista de produtos
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do tecladoa
# pyautogui.click -> cli    LG83.2car com o mousse
# pyautogui.hotkey -> combinação de teclas

# para instalar a biblioteca: pip install pyautogui
import pyautogui
import time

# uma pausa a cada comando

pyautogui.PAUSE = 0.8
# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter") 


# entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter") 
time.sleep(8)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=899, y=1013)
# escrever o seu email
pyautogui.write("alessandra.dorregara4y@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.press("enter")

# abrir e importar um arquivo csv
import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=889, y=725)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo   

    pyautogui.press("tab")  
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")       
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]  
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim




