#from archivos import estudiante
from estudiante import Estudiante

class Menu:

	global lista
	lista=[]
	def inicio(self):
		print("\nMenu \n\n")
		print("a) CapturarAlumnos \n")
		print("b) MostrarAlumnos \n")
		print("c) Salir \n")
		x = input("Elige una opcion: \n")
		
		if(x == "a"):
			menue.CapturarAlumnos()
		elif(x == "b"):
			menue.MostrarAlumnos()
		elif(x == "c"):
			pass

	def CapturarAlumnos(self):
		if(len(lista)>9):
			print("Limite alcanzado!!! \n")
			self.inicio()
		
		Nombre = input("Ingresa el Nombre: \n")
		No_C_E = input("Ingresa el Numero de Control: \n")
		Materia = input("Ingresa la Materia: \n")
		Calificacion = int(input("Ingresa la Calificacion: \n"))
		Alumno_n = Estudiante(Nombre, No_C_E, Materia, Calificacion)
		lista.append((Alumno_n.Nombre, Alumno_n.No_C_E, Alumno_n.Materia, Alumno_n.Calificacion, Alumno_n.Estado))  
		self.inicio()  

	def MostrarAlumnos(self):
		for i in lista:
			print(f"{i}")
		self.inicio()




	Alumno_1 = Estudiante("Jose",1231, "Matematicas", 76)
	Alumno_2 = Estudiante("Josue",1232, "Fisica", 90)
	Alumno_3 = Estudiante("Mariana",1233, "Geografia", 70)
	Alumno_4 = Estudiante("Marlenne",1234, "Algebra", 76)
	Alumno_5 = Estudiante("Carlos",1235, "Quimica", 78)
	Alumnos = [(Alumno_1.Nombre, Alumno_1.No_C_E, Alumno_1.Materia, Alumno_1.Calificacion, Alumno_1.Estado),
				(Alumno_2.Nombre, Alumno_2.No_C_E, Alumno_2.Materia, Alumno_2.Calificacion, Alumno_2.Estado),
				(Alumno_3.Nombre, Alumno_3.No_C_E, Alumno_3.Materia, Alumno_3.Calificacion, Alumno_3.Estado),
				(Alumno_4.Nombre, Alumno_4.No_C_E, Alumno_4.Materia, Alumno_4.Calificacion, Alumno_4.Estado),
				(Alumno_5.Nombre, Alumno_5.No_C_E, Alumno_5.Materia, Alumno_5.Calificacion, Alumno_5.Estado)]

	for i in Alumnos:
		lista.append(i)

menue = Menu() 
menue.inicio()






