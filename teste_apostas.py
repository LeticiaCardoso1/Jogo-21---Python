import random

class Inicio:
    def __init__(self):
        print("|---------------------------------------|")
        print("| Seja bem-vindo ao jogo de cartas 21! |")
        print("|---------------------------------------|")
        print("REGRAS:")
        print("* 1. O objetivo do jogo é chegar a 21")
        print("* 2. Ganha quem completar 21 ou chegar mais próximo")
        print("* 3. Caso ultrapasse 21, você perde automaticamente e passará para o próximo jogador")
        print("* 4. Quando for perguntado se deseja mais cartas, utilize apenas 'SIM' ou 'NÃO'")
        print("BOM JOGO ;) ")
        print(f'-------------------------------------------------------------------------------------')

class Jogadores:
    def __init__(self, jogador, idade, fichas=100, cartas=None):
        self.__jogador = jogador
        self.__idade = idade
        self.__fichas = fichas
        self.__cartas = cartas if cartas else []

    def get_jogador(self):
        return self.__jogador

    def get_idade(self):
        return self.__idade

    def get_cartas(self):
        return self.__cartas

    def adicionar(self, carta):
        self.__cartas.append(carta)

    def get_fichas(self):
        return self.__fichas

    def set_fichas(self, valor):
        self.__fichas = valor

class Jogo:
    def __init__(self, jogador1, jogador2):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__jogadores = [self.__jogador1, self.__jogador2]
        self.__baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        self.__total_apostas = 0

    def apostas(self):
        for jogador in self.__jogadores:
            while True:
                try:
                    valor_aposta = int(input(f"{jogador.get_jogador()}, faça sua aposta (mínimo 20 fichas): "))
                    if 20 <= valor_aposta <= jogador.get_fichas():
                        jogador.set_fichas(jogador.get_fichas() - valor_aposta)
                        self.__total_apostas += valor_aposta
                        break
                    else:
                        print("A aposta deve ser no mínimo 20 fichas e não pode ultrapassar o saldo disponível.")
                except ValueError:
                    print("Por favor, insira um valor numérico.")

    def entregar_cartas(self, jogador):
        carta = random.choice(self.__baralho)
        self.__baralho.remove(carta)
        jogador.adicionar(carta)
        print(f"Carta para {jogador.get_jogador()}: {carta}")
        print(f'Valor da soma das cartas: {sum(jogador.get_cartas())}')
        print(f'-------------------------------------------------------------------------------------')

    def set_jogar(self):
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

    def verificar_vencedor(self):
        pontuacoes = [sum(jogador.get_cartas()) for jogador in self.__jogadores]
        vencedor = None
        pontuacao_vencedor = 0
        for i in range(len(self.__jogadores)):
            if pontuacoes[i] == 21:
                vencedor = self.__jogadores[i].get_jogador()
                pontuacao_vencedor = pontuacoes[i]
                break
            elif pontuacoes[i] > 21:
                continue
            elif vencedor is None or (pontuacoes[i] <= 21 and pontuacoes[i] > pontuacao_vencedor):
                vencedor = self.__jogadores[i].get_jogador()
                pontuacao_vencedor = pontuacoes[i]
        if vencedor:
            print(f'O {vencedor} ganhou com {pontuacao_vencedor} pontos! Você ganhou {self.__total_apostas} fichas!')
        else:
            print('Ninguém ganhou.')

inicio_jogo = Inicio()
jogador1 = Jogadores("Jogador 1", 25, 100, [])
jogador2 = Jogadores("Jogador 2", 30, 100, [])
jogo = Jogo(jogador1, jogador2)
jogo.apostas()
jogo.set_jogar()
jogo.verificar_vencedor()
