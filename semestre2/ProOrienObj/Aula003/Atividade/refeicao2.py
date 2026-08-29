class Receita():
    def __init__(self, nome, porcoes):
        self.nome = nome;
        self.porcoes = porcoes;
        self.fator = self.porcoes / 1

    def calculo_de_porcoes(self):
        # para a massa dos nuggets
        self.m_frango = 500 * self.fator
        self.m_azeite = 4 * self.fator
        self.m_sal = 0.5 * self.fator
        self.m_alho = 3 * self.fator
        self.m_cebola = 0.5 * self.fator
        self.m_paprica = 0.5 * self.fator
        self.m_curcuma = 0.5 * self.fator
        self.m_cheiro_verde = 2 * self.fator
        self.m_pimenta = 'Pimenta-do-reino'
        # para empanar
        self.e_ovos = 2 * self.fator
        self.e_panko = 1 * self.fator

    def exibir_informacoes(self):
        for i in range(30):
            print('-', end='')
        print('\nRECEITA: Nuggets Saudáveis')
        print(f'\nChefe responsável: {self.nome}')
        print(f'Rendimento: {self.porcoes} porção(ões)')
        print('Tempo de preparo: Aproximadamente 35 minutos')
        for i in range(30):
            print('-', end='')
        print('\nINGREDIENTES NECESSÁRIOS:')
        print('\nPara a massa dos nuggets:')
        print(f'- {self.m_frango} g de peito de frango cru, cortado em pedaços.')
        print(f'- {self.m_azeite} colheres (sopa) de azeite de oliva.')
        print(f'- {self.m_sal} colher (chá) de sal.')
        print(f'- {self.m_alho} dentes de alho picados.')
        print(f'- {self.m_cebola} cebola picada.')
        print(f'- {self.m_paprica} colher (chá) de páprica defumada.')
        print(f'- {self.m_curcuma} colher (chá) de cúrcuma.')
        print(f'- {self.m_cheiro_verde} colheres (sopa) de cheiro-verde picado.')
        print(f'- {self.m_pimenta} a gosto.')
        print('\nPara empanar:')
        print(f'- {self.e_ovos} ovos batidos.')
        print(f'- {self.e_panko} xícara de panko ou farinha de rosca integral.')
        print('\nPASSO A PASSO:')
        print('1. Prepare a massa colocando o frango, azeite, sal, alho, cebola, páprica, cúrcuma, cheiro-verde e pimenta no processador. Processe até formar uma massa homogênea.')
        print('2. Com as mãos levemente untadas com azeite, modele pequenas porções da massa no formato de nuggets e disponha-os em uma assadeira forrada com papel manteiga ou levemente untada.')
        print('3. Prepare o empanado colocando os ovos batidos em um prato e o panko ou farinha de rosca integral em outro.')
        print('4. Passe cada nugget primeiro no ovo batido e depois no panko, pressionando suavemente para que o empanado fique bem aderido.')
        print('5. Preaqueça o forno a 200 °C e leve os nuggets para assar por aproximadamente 25 a 30 minutos.')
        print('6. Na metade do tempo de forno, vire os nuggets para que dourem por igual e cozinhem uniformemente.')
        print('7. Retire os nuggets quando estiverem dourados por fora e completamente cozidos por dentro. Se preferir, também podem ser grelhados em frigideira antiaderente com um fio de azeite.')
        print('8. Sirva os nuggets ainda quentinhos. Se desejar, acompanhe com molhos saudáveis, como iogurte temperado com limão e ervas.')

def entrada_de_dados():
    print('\n\n\n\n')
    for i in range(30):
        print('-', end='')
    print('\nFICHA TÉCNICA DIGITAL (POO) - REFEIÇÕES PRÁTICAS')
    for i in range(30):
        print('-', end='')
    nome = input('\nDigite seu nome (sair para fechar o programa): ').upper()
    while True:
        try:
            porcoes = int(input('Quantas porções você deseja preparar? '))
            if porcoes > 0:
                break
            else:
                print('Digite um número maior que zero.')
        except:
            print('Digite algo válido.')
    return nome, porcoes


while True:
    nome, porcoes = entrada_de_dados()
    if nome == 'SAIR':
        print('Adeus')
        break
    else:
        receita = Receita(nome, porcoes)
        receita.calculo_de_porcoes()
        receita.exibir_informacoes()
