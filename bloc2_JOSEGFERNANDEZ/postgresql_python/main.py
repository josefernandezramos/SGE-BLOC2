#import create_registre as cr
import read_registre as rr
import update_registre as up
#Trucada per executar la funció a l'arxiu create_registre.py
#cr.create_reg()
'''
results = rr.read_reg()
for i in results:
    print('\n')
    print('Nom: ' + i[0])
    print('Adreça: ' + i[1])
    print('Telefòn: ' + i[2])
    print('Email: ' + i[3])
    print('Neixament: ' + i[4])'''

up.update_reg()
#print(cr.create_reg())