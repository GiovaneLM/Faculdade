#
##
#2#
#23#
#234#
#2345#
#23456#
#234567#
#2345678#
#########

linha = ""
for coluna in range(0, 9):
    if coluna > 1:
        linha += str(coluna)
    print(linha+"#")
    if coluna == 0:
        linha = "#"
print("#"*(coluna+1))


