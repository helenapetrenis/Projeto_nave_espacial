## Definindo variáveis
combustivel = 110
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
    combustivel = 110
    print("Tanque cheio. Aproveite a viagem! ⛽")


def status_nave():
    ## Mostra a quantidade de combustível e os tripulantes
    print("\n--------STATUS DA NAVE---------")
    global combustivel
    print(f"O status de combustível disponível é: {combustivel} ⛽")
    global tripulantes
    print(f"Os tripulantes presentes na nave são: {tripulantes} 🧑‍🚀")
    

def registrarTripulantes():
    novoTripulante = input("Digite o nome do(a) novo(a) tripulante:")
    tripulantes.append(novoTripulante)
    print("Tripulante inserido com sucesso! 🧑‍🚀")


print("\n ----Bem vindo ao menu interativo da nave 🚀. Por favor selecione uma opção:")
while True: 
    print("\n| 1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 4- Novo Tripulante | 5- Sair |")
    opcao = input("--Digite a opção desejada: ")
    if (opcao == "1"):
        status_nave()
    elif (opcao == "2"):
        viajar()
    elif (opcao == "3"):
        abastecer()       
    elif (opcao == "4"):    
        registrarTripulantes()
    else:    
        print("Viagem encerrada!")
        break


# status_nave()
# registrarTripulantes()
# status_nave()

# viajar()
# viajar()
# viajar()
# abastecer()
# status_nave()
# registrar_tripulantes()

