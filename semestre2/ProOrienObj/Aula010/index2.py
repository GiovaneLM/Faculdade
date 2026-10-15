
class Livro:
    def __init__(self, titulo, autor, ano, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__paginas = paginas

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_ano(self):
        return self.__ano

    def get_paginas(self):
        return self.__paginas

    def set_titulo(self, novoTitulo):
        self.__titulo = novoTitulo

    def mostrar_informacoes(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Ano: {self.__ano}")
        print(f"Páginas: {self.__paginas}")


### Início do Programa

# Criando objetos da classe Livro
livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96)
livro2 = Livro("Dom Quixote", "Miguel de Cervantes", 1605, 1260)

# Acessando os atributos através dos getters
print(livro1.get_titulo())
print(livro1.get_autor(), livro1.get_ano(), livro1.get_paginas())

print()

print("@" * 30, "PROIBIDO", "@" * 30)

livro1.__titulo = "teste"
print(livro1.__titulo)

print()

print("$" * 30, "CORRETO", "$" * 30)

livro1.set_titulo("Novo Título para livro 1 (OK)")
print(livro1.get_titulo())

print("\n\n" + "*" * 41)

# Chamando o método para mostrar as informações do livro
livro2.mostrar_informacoes()
