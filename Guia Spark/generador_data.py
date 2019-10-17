import random

marcas = ['Ford','Chevrolet','Toyota','Fiat','Renault','Citroen','Volkswagen']
modelos = ['Vento','Fluence','Corolla','Uno','Focus','C4','Cruze']
tipos = ['auto','pickup','camion','moto']


def generar_data(cantidad):
	with open('data.csv','w') as archivo:
		for i in range(cantidad):
			linea = f"{i},{random.choice(marcas)},{random.choice(modelos)},version random,{random.choice(tipos)},provincia,{random.randint(1,28)}-{random.randint(1,12)}-{random.randint(2016,2018)}"
			archivo.write(f"{linea}\n")

generar_data(2000)