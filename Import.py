import Otro3  #Si queremos utilizar todo
from Otro3 import Funcion2 #Si solo queremos utilizar una cosa
from Otro2 import Diccionario as Dic
import wpilib
import time
from wpilib import MecanumDrive



class MyRobot(object):
	def __init__(self):

	self.controller = wpilib.Joystick(0)

	self.motor_derecho_front = wpilib.Talon(1)
	self.motor_izquiedo_front = wpilib.Talon(2)
	self.motor_derecho_atras = wpilib.Talon(3)
	self.motor_izquiedo_atras = wpilib.Talon(4)
	self.motor_cañon_izquierdo = wpilib.Talon(5)
	self.motor_cañon_derecho = wpilib.Talon(6)

	self.drive = MecanumDrive(self.motor_derecho_front, self.motor_izquiedo_front, 
				self.motor_derecho_atras, self.motor_izquiedo_atras)

	self.drive.driveCartesian(x,y,z)   #libreria de plano cartesiano

#DEF de ejemplo
# 	def Run(self):
# 		pass
# 		# otro.Funcion()
# 		# otro.Funcion2()
# 		# Dic["Hola"]   -->Algo exacto de la biblioteca

	def Teleoperated(self): #Def para que el robot sea controlado por los drivers

		x = self.controller.getRawAxis(0)
		y = self.controller.getRawAxis(1)
		z = self.controller.getRawAxis(4)

		BotonA = self.controller.getRawButton(0)


		if BotonA_presionado == True:
			self.motor_cañon_izquierdo.set(-0.5) #Nivel de energia al 1. El menos es para que vaya de reversa.
		else:
			self.motor_cañon_izquierdo.set(0)

		Palanca1 = self.controller.getRawAxis(3)

		self.motor_cañon_izquierdo.set(Palanca1)


		self.controller.getRawAxis(3)


	def Autonomus(self): #Def para que sea autonomo

		self.motor_cañon_izquierdo.set(1)
		time.sleep(2)
		self.motor_cañon_izquierdo.set(0)

if __main__ == '__main__':
	wpilib.run(MyRobot)





		