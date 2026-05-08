   ##
  ####
 ######
########
 ######
  ####
   ##
n=4
for i in range(1,n+1):
   espacos=n-i
   cerquilhas=i*2
   print(" " * espacos + "#" * cerquilhas)

for i in range(n-1,0,-1):
   espacos=n-i
   cerquilhas=i*2
   print(" " * espacos + "#" * cerquilhas)



# coluna = 4
# top = [((" " * (coluna - linha) +"##" * linha)) for linha in range (1,coluna+1)]
# print("{}\n{}".format("\n".join(top),"\n".join(top[-2::-1])))