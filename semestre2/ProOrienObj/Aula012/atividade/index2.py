class Consulta:
    def __init__(self, data: str, hora: str):
        self.data = data
        self.hora = hora

    def exibir_consulta(self):
        return f"Data: {self.data} | Hora: {self.hora}"


class Animal:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.historico_consultas = []

    def emitir_som(self):
        pass  

    def agendar_consulta(self, data: str, hora: str):
        consulta = Consulta(data, hora)
        self.historico_consultas.append(consulta)

    def listar_consultas(self):
        print(f"Consultas de {self.nome}:")
        if not self.historico_consultas:
            print("  Nenhuma consulta agendada.")
            return
        for i, consulta in enumerate(self.historico_consultas, start=1):
            print(f"  {i}. {consulta.exibir_consulta()}")

    def listar_animal(self):
        print("-" * 35)
        print(f"Nome do Pet: {self.nome} | Idade: {self.idade} anos")
        print("-" * 35)


class Cachorro(Animal):
    def __init__(self, nome: str, idade: int, raca: str):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print(f"{self.nome} diz: Au au!")


class Gato(Animal):
    def __init__(self, nome: str, idade: int, cor: str):
        super().__init__(nome, idade)
        self.cor = cor

    def emitir_som(self):
        print(f"{self.nome} diz: Miau!")

    def listar_animal(self):
        print("-" * 35)
        print(f"Nome do Pet: {self.nome} | Idade: {self.idade} anos | Cor do pelo: {self.cor}")
        print("-" * 35)


class Passaro(Animal):
    def __init__(self, nome: str, idade: int, especie: str):
        super().__init__(nome, idade)
        self.especie = especie

    def cantar(self):  
        print(f"{self.nome} canta: Piu piu!")

    def listar_passaro(self):
        self.listar_animal() 
        print(f"Espécie: {self.especie}")



rex = Cachorro("Rex", 5, "Labrador")
mia = Gato("Mia", 3, "Cinza")
piu = Passaro("Piu", 2, "Canário")


print("\n=== Som ===")
rex.emitir_som()
mia.emitir_som() 
piu.cantar()

rex.agendar_consulta("10/11/2026", "14:00")
rex.agendar_consulta("24/11/2026", "09:30")
mia.agendar_consulta("12/11/2026", "16:15")

print("\n=== Cadastro dos pets ===")
rex.listar_animal()
mia.listar_animal()
piu.listar_passaro()

print("\n=== Históricos ===")
rex.listar_consultas()
mia.listar_consultas()
piu.listar_consultas() 