import create_registre as cr
import read_registre as rr

#Trucada per executar la funció a l'arxiu create_registre.py
cr.create_reg()

results = rr.read_reg()
for i in results:
    print('\n')
    print('Nom: ' + i[1])
    print('Adreça: ' + i[2])
    print('Telefòn: ' + i[3])
    print('Email: ' + i[4])
    print('Neixament: ' + i[5])


print(cr.create_reg())