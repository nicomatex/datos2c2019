import random

categorias = ["Comida","Tocador","Computacion","Bazar","Muebles"]

def generar_data(cantidad):
	for i in range(cantidad):
		print(f"{random.randint(1,20)},8,9,10,{random.randint(2015,2017)}0{random.randint(1,9)}01,{random.randint(5,15)}")