class Estudiante:
	
	#	Constructor
	def __init__(self, Nombre, No_C_E=1234, Materia="Materia", Calificacion=100):
		self.Nombre = Nombre or self.AsignarNombre()
		self.No_C_E = No_C_E
		self.Materia = Materia 
		self.Calificacion = Calificacion
		self.Estado = self.AsignarEstado(Calificacion)
	
	def AsignarNombre(self):
		self.Nombre = input("Ingresa el Nombre: \n")
		return self.Nombre

	def AsignarEstado(self, Calificacion):
		if (Calificacion >= 60):
			return "Aprobado"
		else:
			return "Reprobado"
