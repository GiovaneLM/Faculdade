class Receita():
    def __init__(self,nome,porcoes):
        self.nome = nome;
        self.porcoes = porcoes;
        self.fator = self.porcoes / 2

    def calculo_de_porcoes(self):
        #para o espaguete de abobbrinha
        self.e_abobrinha = 2 * self.fator
        self.e_azeite = 1 * self.fator
        self.e_cebola = 0.5 * self.fator
        self.e_sal = 'sal'
        self.e_pimenta = 'Pimenta-do-reino'
        #para o molho à bolonhesa
        self.m_patinho = 500 * self.fator
        self.m_cebola = 0.5 * self.fator
        self.m_azeite = 2 * self.fator
        self.m_latatomate = 2 * self.fator
        self.m_alho = 1 * self.fator
        self.m_noz = 'Noz-Moscada'
        self.m_sal = 'sal'
        self.m_pimenta = 'Pimenta-do-reino moida'
        self.m_manjericao = 'manjericão'


    def exibir_informacoes(self):
            for i in range(30):
                print('-', end='')
            print('\nRECEITA : Espaguete de abobrinha ao molho bolonhesa')
            print(f'\nchefe responsavel: {self.nome}')
            print(f'Rendimento: {self.porcoes} porçaão(ões)')
            print(f'Tempo de preparo : Aproximadamente 40 minutos')
            for i in range(30):
                print('-', end='')
            print('\nINGREDIENTES NECESSARIOS:')
            print('\nPara o espaguete de abobrinha:')
            print(f'- {self.e_abobrinha} abobrinhas médias')
            print(f'- {self.e_azeite} colher (sopa) de azeite de oliva.')
            print(f'- {self.e_cebola} cebola picada (opcional).')
            print(f'- {self.e_sal} e {self.e_pimenta} a gosto')
            print('\nPara o molho à bolonhesa:')
            print(f'- {self.m_patinho} g de patinho moído.')
            print(f'- {self.m_cebola} cebola picada.')
            print(f'- {self.m_azeite} colheres (sopa) de azeite de oliva.')
            print(f'- {self.m_latatomate} latas de tomate pelado com líquido (cerca de 400 g cada).')
            print(f'- {self.m_alho} dente de alho picado.')
            print(f'- {self.m_noz},{self.m_sal} e {self.m_pimenta} a gosto')
            print(f'- Folhas de  {self.m_manjericao}  fresco (opcional).')
            print('\nPASSO A PASSO:')
            print('1. Organize todos os ingredientes e utensílios antes de iniciar o preparo.')
            print('2. Aqueça o azeite e sele o patinho moído em fogo médio até dourar. Adicione a cebola, o alho e os temperos e refogue até dourarem.')
            print('3. Acrescente o tomate pelado com o líquido e cozinhe em fogo baixo por 20 a 25 minutos, mexendo ocasionalmente.')
            print('4. Finalize o molho com folhas de manjericão fresco e mantenha-o aquecido até a montagem.')
            print('5. Lave as abobrinhas, retire as pontas e corte-as em tiras finas usando um ralador tipo Julienne.')
            print('6. Aqueça o azeite em uma frigideira grande e refogue as tiras de abobrinha em fogo alto por 2 a 3 minutos.')
            print('7. Tempere a abobrinha com sal e pimenta-do-reino, mantendo-a levemente macia, mas ainda firme.')
            print('8. Distribua o espaguete de abobrinha nos pratos, cubra com o molho bolonhesa quente e finalize com manjericão fresco.')


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
            break
        except:
            print('digite algo valido')
    return nome, porcoes

while True:
    nome,porcoes = entrada_de_dados()
    if nome == 'SAIR':
        print('Adeus')
        break
    else:
        receita = Receita(nome,porcoes)
        receita.calculo_de_porcoes()
        receita.exibir_informacoes()