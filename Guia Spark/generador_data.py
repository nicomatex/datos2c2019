import random

categorias = ["Comida","Tocador","Computacion","Bazar","Muebles"]

def generar_data(cantidad):
	for i in range(cantidad):
		print(f"{random.randint(1,28)}-{random.randint(1,12)}-{random.randint(2017,2019)},{random.randint(1,200)},{random.randint(500,2000)}")