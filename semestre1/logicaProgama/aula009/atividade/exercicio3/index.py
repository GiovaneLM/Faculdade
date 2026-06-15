       #
      ###
     #####
    #######
   ##     ##
  ###     ###
#####     #####
 ####     ####
  ###     ###
   ##     ##
    #######
     #####
      ###
       #


for i in range(1,7):
    espacos=12-i
    cerquilhas=i*2
    print(" " * espacos + "#" * cerquilhas)

for i in range(1,7):
    espacos=6-i
    cerquilhas=i
    espaco_interno=11
    print(" " * espacos + "#" * cerquilhas + " " * espaco_interno + "#" * cerquilhas)
    
for i in range(1,7):
    espacos=6-i
    cerquilhas=i
    espaco_interno=11
    print(" " * espacos + "#" * cerquilhas + " " * espaco_interno + "#" * cerquilhas)
for i in range(5,0,-1):
    espacos=6-i
    cerquilhas=i*2-1
    print(" " * espacos + "#" * cerquilhas)