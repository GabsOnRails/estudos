'''
Cadastro de viagem.
O programa deve ter as seguintes funções:
1 - O usuário deve informar o nome para cadastrar uma viagem;
2 - Deve selecionar um destino baseado nas instâncias de objeto da classe viagem;
3 - Deve ser apresentado uma mensagem que o cadastro para a viagem foi realizado e o local.
'''
class Destino:
        def __init__(self,destino):
                self.destino = destino
# Criando opções de viagem
viagem_0 = Destino("Japão - Shibuya") # -> Usar a class aqui é de suma importância, pois estamos instânciando os objetos.
viagem_1 = Destino("Brasil - Salvador")
viagem_2 = Destino("Alemanha - Frankfurt")
viagem_3 = Destino("Grécia - Atenas")
viagem_4 = Destino("Suíça - Zurique")
print("Seja bem vindo!")
viajante = input("Digite seu nome para comerçamos: ")
print(f"\n{viajante.title()}, temos alguns destinos para você:"
        '''
        [0] Japão - Shibuya
        [1] Brasil - Salvador
        [2] Alemanha - Frankfurt
        [3] Grécia - Atenas
        [4] Suíça - Zurique
        '''
        )
escolha = int(input("Selecione seu destino: "))
lista_viagem = [viagem_0,viagem_1,viagem_2,viagem_3,viagem_4]
for opcoes in lista_viagem:
        if escolha >= 5:
                print("EStá opção é inválida..")
                break
        if escolha <= 4 and escolha >= 0:
                print(f"{viajante.title()}, sua viagem para {lista_viagem[escolha].destino} está marcada!")
                print("Boa viagem e volte sempre!!")
                break