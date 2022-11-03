from regras import confere_email
from crud import Db_comandos

def credenciais_de_email():
    while True:
        email=input("digite o seu email: ")
        if(confere_email(email)):
            return email
            
        else:
            print("infelizmente esse endereço email não é valido")
            print("digite um endereço email valido")
            continue

def credenciais_de_senha():
    senha=str(input("digite sua senha: "))
    return senha


        


def opcao():
    while True:
        op=int(input("digite um numero: "))
        if(op==1):
            email=credenciais_de_email()
            senha=credenciais_de_senha()
            if(Db_comandos.consulta(email,senha)):
                print("BEM VINDO AO SISTEMA")# pegar as credencias e fazer uma leitura no db
                break
            else:
                print("senha ou usuario incorretos")
                continue
             
            
        elif(op==2):
            print("cadastrar novo usuario")  # criar função de cadastro
            break
        else:
            print("opção invalida")
            continue

