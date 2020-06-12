#Sistema de cadastro com com dicionário em python3

import os

dic = {}#dicionario principal
lista_nome = []
lista_idade = []
lista_sexo = []
lista_senha = []

def cadastrar():
    total = int(input("Insira quantidade de pessoa a cadastrar(0 -> sair): "))

    #dicionário e lista join
    dic["Nome"] = lista_nome
    dic["Idade"] = lista_idade
    dic["Sexo"] = lista_sexo
    dic["Senha"] = lista_senha
    
    if(total == 0):
        return
    else:
        for x in range(total):
            lista_nome.append(input(f"Insira seu nome {x+1}: "))
            lista_idade.append(int(input(f"Insira sua idade {x+1}: ")))
            lista_sexo.append(input(f"Insira seu sexo {x+1}: "))
            lista_senha.append(input(f"Insira sua senha {x+1}: "))
    print(dic.items())

def login():
    nome = input("Insira seu nome: ")

    for x, y in dic.items():
        for z in range(len(lista_nome)):
            if(nome == y[z]):
                senha = input("Insira sua senha: ")
                passe = dic["Senha"]# atribuir só password para imprimir na mesma posição de modo não ter vulnerabilidade
                if(senha == passe[z]):
                    print("Logado com sucesso!")
                    return



def main():
    os.system("cls" if os.name == "nt" else "clear")
    acrescenta = "-"*15
    print(f"1.Cadastrar {acrescenta} 2.Logar {acrescenta} 3.Sair")
    opcao = int(input("Insira uma opção: "))

    if(opcao == 1):
          cadastrar()
          input("Preciona qualquer tecla para continuar...")
          main()
    elif(opcao == 2):
        login()
        input("Preciona qualquer tecla para continuar...")
        main()
    elif(opcao == 3):
        quit()

main()
