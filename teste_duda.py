import random
class Jogador():
    def __init__(self, nome, fichas):
        self.nome = nome
        self.fichas = fichas
        self.cartas_jogador = []
class Jogo():
    def __init__(self):
        self.jogador1 = None
        self.jogador2 = None
        self.jogadores = [self.jogador1, self.jogador2]
        self.baralho = {
        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Q': 10, 'J': 10, 'K': 10
        }
    def menu(self):
        print("-------------------------------------"
        "| Welcome to my Blackjack game! |"
        "-------------------------------------")
        print("1- Start game")
        print("2- See value of cards")
        print("3- Rules")
        print("4- Exit game")
        option = int(input("What you want to do?"))
        print("---------------------------------------------------------------------------------------------------------------")
        match option:
            case 1:
                self.start_game()
            case 2:
                print("Value of cards")
                print(self.get_baralho())
                self.menu()
            case 3:
                self.regras()
            case 4:
                exit()
    def get_baralho(self):
        return self.baralho

    def regras(self):
        print("RULES BLACKJACK")
        print("\nObjective: Get as close as possible to 21 points without exceeding it."
        "\nCard Distribution:"
        "\nEach player and the dealer receive two cards."
        "\nWinning and Losing:"
        "\nBlackjack: Having 21 points with the first two cards automatically wins"
        "\nGoing Over 21: Immediate loss."
        "\nTies:"
        "\nThe bet is typically returned in case of a tie.")
        self.menu()

    def sortear_cartas(self, jogador):
        cartas = random.choice(self.baralho)
        self.baralho.remove(cartas)
        self.cartas_jogador.append(cartas)
    def start_game(self):
        print("Let's start!")
        for i in range(1):
            for jogador in self.jogadores:
                self.sortear_cartas(jogador)
                while True:
                    print(f'Cartas {self.jogador1.nome}: {self.jogador1.cartas_jogador}'
                    f'Soma total: {self.soma}')
                    print(f'Cartas {self.jogador2.nome}: {self.jogador2.cartas_jogador}'
                    f'Soma total: {self.soma}')
                    acao_jogador1 = int(input(f'{self.jogador1.nome}, deseja:'
                    f'1- Pedir cartas'
                        f'2- Parar'))
                    acao_jogador2 = int(input(f'{self.jogador2.nome}, deseja pedir cartas?:'
                        f'1- Sim'
                        f'2- Não'))
                    match acao_jogador1:
                        case 1:
                            self.sortear_cartas(self.jogador1)
                            self.verificar_vencedor()
                        case 2:
                            continue
                             self.verificar_vencedor()
                    match acao_jogador2:
                         case 1:
                              self.sortear_cartas(self.jogador2)
                              self.verificar_vencedor()
                          case 2:
                               continue
                               self.verificar_vencedor()
    def verificar_vencedor(self):
        self.soma_jogador1 = sum(self.jogador1.cartas_jogador)
        self.soma_jogador2 = sum(self.jogador2.cartas_jogador)
            if self.soma_jogador1 or self.soma_jogador2 == 21:
                print("You won! Congrats")
                self.menu()
            elif self.soma_jogador1 == 21:
                print(f'{self.jogador1}, you lost :(')
                print(f'{self.jogador2} you won, Congrats!')
                self.menu()
            elif self.soma_jogador2 == 21:
                print(f'{self.jogador2}, you lost :(')
                print(f'{self.jogador3} you won, Congrats!')
                self.menu()
            elif self.soma_jogador1 or self.soma_jogador2 < 21:
                self.start_game()

jogador1 = Jogador("Jogador 1", 100)
jogador2 = Jogador("Jogador 2", 100)
jogo = Jogo()
jogo.jogador1 = jogador1
jogo.jogador2 = jogador2
jogo.menu()