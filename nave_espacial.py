## Definindo variáveis
combustivel = 100
tripulantes = []

## Definindo funções
def viajar():
    ##Aqui vamos gastar combustível
    global combustivel 
    if (combustivel >= 30): 
      combustivel = combustivel - 30
      print("A nave viajou")
    else:
      print("Você está sem combustível suficiente. Abasteça! 🪫")

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio. Aproveite a viagem! ⛽")


def status_nave():
    ## Mostra a quantidade de combustível e os tripulantes
    print("\n--------STATUS DA NAVE---------")
    global combustivel
    print(f"O status de combustível disponível é: {combustivel} ⛽")
    global tripulantes
    print(f"Os tripulantes presentes na nave são: {tripulantes} 🧑‍🚀")
    

def registrarTripulantes():
    novoTripulante = input("Digite o nome do(a) novo(a) tripulante: ")
    tripulantes.append(novoTripulante)
    print("Tripulante inserido(a) com sucesso! 🧑‍🚀")


## Cria uma função que tira o último tripulante

def removerTripulantes():
    if len(tripulantes) > 0:
        tripulantes.pop()
        print("Tripulante removido com sucesso!")
        print(tripulantes)

    else:
        print("A lista de tripulantes está vazia! Volte para o menu para adicionar um novo tripulante. 🧑‍🚀")


print("\n ----Bem vindo ao menu interativo da nave 🚀. Por favor selecione uma opção:")
while True: 
    print("\n| 1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 4- Novo Tripulante | 5- Remover Tripulante | 6- Sair |")
    opcao = input("--Digite a opção desejada: ")
    if (opcao == "1"):
        status_nave()
    elif (opcao == "2"):
        viajar()
    elif (opcao == "3"):
        abastecer()       
    elif (opcao == "4"):    
        registrarTripulantes()
    elif (opcao == "5"):    
        removerTripulantes()
    else:    
        print("Viagem encerrada!")
        break




