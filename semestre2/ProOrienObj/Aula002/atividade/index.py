# Exercício Prático: Primeira Classe em Python (POO)

# Objetivo: Criar e manipular sua primeira classe em Python, compreendendo na prática como funcionam os atributos, a instanciação de objetos e a execução de métodos.

# Descrição da Atividade:

# Você foi contratado para desenvolver a estrutura inicial de um sistema de cadastro. Para isso, você deve criar uma classe chamada Pessoa seguindo os passos abaixo:

# Definição da Classe e Atributos:

# nome (texto)
# idade (número inteiro)
# cpf (texto)
# email (texto)
# celular (texto)

# Criação dos Métodos:
# cadatrar(self,nome,idade,cpf,email,celular): Método que atribui os valors ao objeto conforme  os 5 dados passados como parâmetros para a pessoa de forma organizada.

# exibir_dados(self): Método que imprime na tela todos os 5 dados cadastrados da pessoa de forma organizada.

# alterar_celular(self, novo_celular): Método que recebe um novo número de telefone como parâmetro e atualiza o atributo celular do objeto.

# Código Principal (Teste prático):


# Crie (instancie) um objeto da classe Pessoa com dados fictícios.
# Chame o método exibir_dados() para mostrar as informações iniciais.
# Chame o método alterar_celular(...) passando um novo número.
# Chame novamente o método exibir_dados() para confirmar se o número do celular foi realmente atualizado.


# Exemplo de Saída Esperada no Console:
# --- DADOS DA PESSOA ---
# Nome: Ana Souza
# Idade: 20
# CPF: 123.456.789-00
# E-mail: ana.souza@email.com
# Celular: (51) 98888-1111

# Número de celular atualizado com sucesso!

# --- DADOS DA PESSOA ---
# Nome: Ana Souza
# Idade: 20
# CPF: 123.456.789-00
# E-mail: ana.souza@email.com
# Celular: (51) 99999-2222



class Pessoa():
    nome = 'nome'
    idade = 0
    cpf = '0'
    email = 'email'
    celular = '(00)00000-0000'

    def cadastrar(self,nome,idade,cpf,email,celular):
        self.nome=nome
        self.idade=idade
        self.cpf=cpf
        self.email=email
        self.celular=celular
        print('Pessoa Cadastrada!!!')

    def listar(self):
        print('\n####################################################################')
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}')
        print(f'E-mail: {self.email}@email.com')
        print(f'Celular: ({self.celular[:2]}){self.celular[2:7]}-{self.celular[7:]}')
    def alterar_celular(self, novo_celular):
        self.celular=novo_celular
        print('celular alterado')


pessoa=Pessoa()

nome=input('digite um nome: ')
pessoa.cadastrar(nome,27,'85469246000','giovane','51994559463')

pessoa.listar()

pessoa.alterar_celular('51994559462')

pessoa.listar()