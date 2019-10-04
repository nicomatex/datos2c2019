import random

categorias = ["Comida","Tocador","Computacion","Bazar","Muebles"]

def generar_data(cantidad):
	for i in range(1,200+1):
		print(f"{i},Descripcion Random,{random.choice(categorias)}")