# 1
# 12
# 123
# 1234
# 12345

for linha in range(1, 6):
    for coluna in range(1, linha+1):
        print(coluna, end="")
    print()

linha = ""
for coluna in range(1, 6):
    linha = linha + str(coluna)
    print(linha)

