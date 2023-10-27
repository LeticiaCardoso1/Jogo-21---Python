import random

class Inicio():
    print("|-----------------------------|")
    print("| Seja bem-vindo ao jogo 21!  |")
    print("|-----------------------------|")

class Jogadores():
    def __init__(self, jogador, idade, fichas, cartas):
        self.__jogador = jogador
        self.__idade = idade
        self.__fichas = 20
        self.__cartas = []

    def get_jogador(self):
        return self.__jogador

    def get_idade(self):
        return self.__idade

    def get_fichas(self):
        return self.__fichas

    def get_cartas(self):
        return self.__cartas

    def adicionar(self, cartas):
        self.__cartas.append(cartas)

class Jogo():
    def __init__(self, jogador1, jogador2):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__jogadores = [self.__jogador1, self.__jogador2]
        self.__baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

    def entregar_cartas(self, jogador):
        carta = random.choice(self.__baralho)
        self.__baralho.remove(carta)
        jogador.adicionar(carta)
        print(carta)

    def jogar(self):
        for i in range(1):
            for jogador in self.__jogadores:
                self.entregar_cartas(jogador)

        for jogador in self.__jogadores:
            print(f"O jogador é {jogador.get_jogador()}: Cartas desse jogador {jogador.get_cartas()}")
            print(f'-------------------------------------------------------------------------------------')

        for jogador in self.__jogadores:
            while sum(jogador.get_cartas()) < 21:
                rodada = input(f"{jogador.get_jogador()}, você quer mais uma carta? Digite Sim ou Não: ").upper()
                if rodada == "SIM":
                    self.entregar_cartas(jogador)
                    print(f"Cartas do {jogador.get_jogador()}: {jogador.get_cartas()}")
                    print(f'-------------------------------------------------------------------------------------')
                else:
                    break

                    pontos = 0
                    ganhador = None

jogador1 = Jogadores("Jogador 1", 25, 20, [])
jogador2 = Jogadores("Jogador 2", 30, 20, [])

jogo = Jogo(jogador1, jogador2)
jogo.jogar()

