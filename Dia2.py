class Gato(object):
	def __init__(self):

		self.diccionario = {
		'cabello' : 'naranja.',
		'ojos' : 'gris'
		}

	def habla(self):
		print ('Meow, tengo color de ojos ' + self.diccionario['ojos'] + ' y color de pelo ' + self.diccionario['cabello'] + " Soy Garfield.")

Gato1 = Gato()

Gato1.habla()
