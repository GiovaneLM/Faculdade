class Tutor:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone

    def exibir_dados(self):
        print('*'*20,'TUTOR','*'*20)
        print(f'nome do tutor : {self.nome}')
        print(f'telefone do tutor : {self.telefone}')
        print('*'*47,'\n')

class Pet:
    def __init__(self,nome,especie,tutor):
        self.nome=nome
        self.especie=especie
        self.tutor=tutor

    def exibir_ficha_veterinaria(self):
        print('*'*20,'ficha','*'*20)
        print(f'nome: {self.nome}')
        print(f'especie: {self.especie}')
        print(f'tutor: {self.tutor.nome}')
        print(f'celular: {self.tutor.telefone}')
        print('*'*47,'\n')

    def exibir_ficha_veterinaria2(self):
        print('*'*20,'ficha','*'*20)
        print(f'nome: {self.nome}')
        print(f'especie: {self.especie}')
        tutor1.exibir_dados()
        print('*'*47,'\n')


tutor1=Tutor('giovane','51 994559463')
tutor1.exibir_dados()

pet1=Pet('pitucha','canino',tutor1)
pet1.exibir_ficha_veterinaria()

print('\n\n\n')
pet1.exibir_ficha_veterinaria2()