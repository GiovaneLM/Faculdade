# #1#3#5#7#9
# 0#2#4#6#8#
# #1#3#5#7#9
# 0#2#4#6#8#
# #1#3#5#7#9
# 0#2#4#6#8#

for linha in range(6):
    for coluna in range(10):
        if linha % 2 == 0 and coluna % 2 == 0:
            print("#", end="")
        elif linha % 2 == 1 and coluna % 2 == 1:
            print("#", end="")
        else: print(coluna, end="")
    print()

