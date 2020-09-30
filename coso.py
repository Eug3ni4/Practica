print ("Inserte 2 numeros")
x = int (input ())
y = int (input())
suma = x+y
print (suma)

print ("Nocierto")


# Clases que crean objetos
class MyRobot(object):
	def __init__(self):

		self.motor = motor

		self.wheel = wheel

	def Forward():
		pass

	def stop():
		pass

Robot1 = MyRobot()
Robot2 = MyRobot()
Robot3 = MyRobot()

MyRobot.Forward()

# Listas y diccionarios
x = ["string",2, [2,3]]
y = {"caja1":8,
		"caja2": "Hola"
		"caja3": 9
}

print (x)
#Esto imprimiria la lista

for variable in x:
	print variable
#Esto imprimira cada variable por separado

print x.index("string") #Esto te da la pusicion de la variable

print x[1] #Esto imprimiria la varible numero 1


y = [1,2,3,4,5,6,7]

for number in y:
	print number #Iterar
	if number = 2:
		print ("Es 2")
	else:
		print ("No es 2")

	if number == 7:
		number.pop(number)



diccionario = {
	
	"caja1": True,
	"caja2": False

}

print diccionario["caja1"]