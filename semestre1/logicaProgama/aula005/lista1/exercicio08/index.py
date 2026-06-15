# Exercício 08.
# Ler nome e perguntar se a pessoa está feliz (S/N), contando respostas

# Inicializa contador de pessoas felizes
qt_felizes = 0

# Inicializa contador de pessoas infelizes
qt_infelizes = 0

# Loop principal (roda indefinidamente)
while True:

    # Lê o nome da pessoa
    nome = input("Seu nome: ")

    # Loop para validar resposta S/N
    while True:

        # Pergunta se a pessoa está feliz e converte para minúsculo
        resp = input("voce e feliz s/n: ").lower()

        # Verifica se a resposta é válida
        if resp in "sn":

            # Sai do loop de validação
            break

        # Caso resposta inválida
        print("resposta incorreta")

    # Se a resposta for "s"
    if resp == "s":

        # Incrementa contador de felizes
        qt_felizes += 1

    # Caso contrário (resposta "n")
    else:

        # Incrementa contador de infelizes
        qt_infelizes += 1

    # Exibe quantidade de felizes
    print("felizes : ", qt_felizes)

    # Exibe quantidade de infelizes
    print("felizes : ", qt_infelizes)