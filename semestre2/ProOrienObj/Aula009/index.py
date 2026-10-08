class Proprietario:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def exibir_dados(self):
        print('================')
        print('DADOS DO PROPRIETARIO')
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}')


class Corretor:
    def __init__(self, nome, creci, percentual_comissao):
        self.nome = nome
        self.creci = creci
        self.percentual_comissao = percentual_comissao

    def vender_imovel(self, imovel, valor_final):
        imovel.status = "VENDIDO"
        self.valor_comissao = valor_final * (self.percentual_comissao / 100)
        return self.valor_comissao

class Imovel:
    status_permitido = ['DISPONIVEL','ALUGADO','VENDIDO']

    def __init__(self, codigo, endereco, tipo, valor, proprietario, corretor=None):
        self.codigo = codigo
        self.endereco = endereco
        self.tipo = tipo
        self.valor = valor
        self.proprietario = proprietario
        self.corretor = corretor
        self.status = 'DISPONIVEL'

    def alterar_status(self, novo_status):
        if novo_status in self.status_permitido:
            self.status = novo_status

    def exibir_ficha(self):
        print('================')
        print('DADOS DO IMOVEL')
        print(f'Codigo: {self.codigo}')
        print(f'Endereço: {self.endereco}')
        print(f'Tipo: {self.tipo}')
        print(f'Valor: R${self.valor}')
        print(f'Status: {self.status}')
        if self.corretor is not None:
            print(f'Corretor: {self.corretor.nome}')
            print(f'Creci: {self.corretor.creci}')
        else:
            print('Corretor: Não Definido')
        print(f'Proprietario: {self.proprietario.exibir_dados()}')
        


corretor1 = Corretor("Carlos Silva", "CRECI 12345", 5)
corretor2 = Corretor("Ana Souza", "CRECI 67890", 6)


proprietario1 = Proprietario("João Santos","123.456.789-00","(51) 99999-1111","joao@email.com")
proprietario2 = Proprietario("Maria Oliveira","987.654.321-00","(51) 99999-2222","maria@email.com")


imovel1 = Imovel("IM001","Rua das Flores, 100","Apartamento",350000,proprietario1,corretor1)
imovel2 = Imovel("IM002","Avenida Brasil, 500","Casa",520000,proprietario2,corretor2)
imovel3 = Imovel("IM003","Rua Central, 250","Sala Comercial",280000,proprietario1,corretor2)


comissao = corretor1.vender_imovel(imovel1, 340000)
print(f'Comissão gerada: R${comissao:.2f}')

imovel2.alterar_status('ALUGADO')


imovel1.exibir_ficha()
imovel2.exibir_ficha()
imovel3.exibir_ficha()