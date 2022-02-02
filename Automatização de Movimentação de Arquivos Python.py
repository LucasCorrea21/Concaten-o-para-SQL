from pathlib import Path
import shutil
import time


def Inicio():
    print("Bem vindo ao Programa de Automatização")
    entrada = input("Digite 1 - Para automatizar OS\nDigite 2 - Para uma nova automatização\nDigite 3 - Para pegar os Torrent\nDigite 4 - Para Sair: \n")
    if entrada == '1':
        Envia_OS()
    elif entrada == '3':
        Torrent()
    elif entrada == '4':
        exit()

def Acabou():
    entrada_acabou = input("Deseja continuar ? 1 - Sim / 2 - Não> ")
    if entrada_acabou == '1':
        Inicio()
    elif entrada_acabou == '2':
        print("O Programa será fechado em 3 segundos")
        time.sleep(3)
        exit()

#Inserindo o caminho do local onde está o arquivo.
caminho = Path('C:/Users/lucas/Downloads')

#print(caminho)
#Informando para o Python que a variável arquivos vai receber o caminho e será um iterável, possibilitando assim,
#os arquivos se tornarem um lista.
arquivos = caminho.iterdir()

#Criando a nova pasta na página desktop.
#Path('C:/Users/lucas/Desktop/Pasta OS').mkdir()

#Execução do Script
caminho = Path('C:/Users/lucas/Downloads')
arquivos = caminho.iterdir()


def Torrent():
    try:
        Path('D:/Download - Atual/Torrent').mkdir()
        print("Pasta criada")
    except:
        print("A pasta já foi criada")
    arquivos = caminho.iterdir()
    cont = 0
    for arquivo in arquivos:
        nome_arquivo = arquivo.name
        if nome_arquivo[-7:] == 'torrent':
            cont += 1
            local_final = caminho / Path('D:/Download - Atual/Torrent')
            shutil.copy2(arquivo, local_final)
    print(f"Foi enviado(os) {cont} para a pasta")        
    print("O programa foi finalizado")
    Acabou()

def Envia_OS():
    try:
        Path('D:/Download - Atual/Pasta OS').mkdir()
        print("Pasta criada")
    except:
        print("A pasta já foi criada")
    arquivos = caminho.iterdir()
    cont = 0
    for arquivo in arquivos:
        nome_arquivo = arquivo.name
        if nome_arquivo[:3] == 'OS ':
            cont += 1
            local_final = caminho / Path('D:/Download - Atual/Pasta OS')
            shutil.copy2(arquivo, local_final)
    print(f"Foi enviado(os) {cont} para a pasta")        
    print("O programa foi finalizado")
    Acabou()

Inicio()
time.sleep(150)


