
def menu():
    print("1 Ingresar un paciente nuevo")
    print("2 Borrar de un paciente")
    print("3 Agregar más enfermedades")
    print('4 Agregar más medicamentos')
    print('5 Generar reporte de las enfermedades tratadas en la clínica')
    print('6 Generar reporte de los medicamentos entregados en la clínica')
    print('7 Comparacion de pacientes')
    print("[0] Salir")

    x= int(input('Digite un numero'))
    x = int(x)

    if x == 1:

        nuevo()

    elif x == 2:

        borrar()

    elif x == 3:    
    
       enfermedad()

    elif x == 4:    
    
       medicina()

    elif x == 5:    
    
        Enfermedad()   

    elif x == 6:    
    
        agregado()    


    elif x == 7:    
    
        comparacion()


    elif x == 0:    
        print("¿Desea salir?: (SI/NO)")
       
exit        
     

def nuevo():
    print ("Nuevo registro")
    archivo = open ("registro.txt","a")
  
    cedulas=input("Ingrese la cedula: ")
    nombre= input("Ingrese el nombre:" )
    apellido= input("Ingrese el apellido:" )
    Enfermedad= input("Ingrese la enfermedad:" )
    Enfermedad2=input ("Ingreso segunda enfermedad")
    Medicamento= input("Ingrese un medicamento:" )
    Medicamento2= input("Ingrese segundo medicamento" )
    
    info = [cedulas, nombre, apellido , Enfermedad , Enfermedad2,Medicamento,Medicamento2]
    for elemento in info:
      print(elemento)  
    print ("Se han capturado:",cedulas, "con el tel:",nombre,apellido,Enfermedad,Enfermedad2,Medicamento,Medicamento2 )
   
    
    archivo.write(str(info))
    archivo.close()
    menu()

def borrar():
  

     ID = int(input("Ingrese el numero de cédula: "))
    
    
     Variable = {'Nombre': 'Randy','apellido': 'Soto', 'cedula' : 117670332,'enfermedades': ['Hepaptiti'], 'medicamentos': ['Calcio', 'Paracetamol'] }
     Variable2 = {'Nombre': 'Melissa','apellido': 'Castro', 'cedula' : 154562, 'enfermedades': ['Dormicion'],'medicamentos': ['mamitis', 'Dalorium'] }
     
     
     if ID == 117670332:
      Variable.clear()
      print(Variable)
     elif ID == 154562: 
      print(Variable2) 
      Variable2.clear

      
      menu()



def enfermedad():
     ID = int(input("Ingrese el numero de cédula:"))
     Enfermedades = (input("Ingresar enfermedades: "))

     pacientes1 = {'Nombre': 'Jose','Apellido': 'Lopez','Cedula' : 15467}
     paciente1 = ['Durmicion', 'Colesterol']
     

     pacientes2 = {'Nombre': 'Rodrigo','Apellido': 'Frankie','Cedula' : 456678}
     paciente2 = ['Colera', 'Hepatitis']
    
     if ID == 15467:
       paciente1.append(Enfermedades)
       print(pacientes1,"enfermedades:", paciente1)   

     elif ID == 456678:
        paciente2.append(Enfermedades)
        print(pacientes2,"enfermedades:", paciente2) 

     print("Enfermedades agregadas al sistema con exito")
     print("------------------------------")
     menu()



def  medicina():
     ID = int(input("Ingrese el numero de cédula:"))
     Medicamentos = (input("Ingresar medicamentos: "))


     pacientes1 = {'Nombre': 'Rodrigo','Apellido': 'Fallas','Cedula' : 858585}
     paciente1 = ['calcio', 'Vitamina']
     

     pacientes2 = {'Nombre': 'Calcio','Apellido': 'Lopez','Cedula' : 11111}
     paciente2 = ['Tabcin', 'Gex']
    
     print("Medicamentos agregados")


     if ID == 858585:
       paciente1.append(Medicamentos)
       print(pacientes1, "Medicamentos: ", paciente1)   

     elif ID == 11111:
        paciente2.append(Medicamentos)
        print(pacientes2, "Medicamentos: ", paciente2) 
        print("------------")
     menu()


def  Enfermedad():
     Enfermedades = (input("Ingresar enfermedades: ")) 

     pacientes = ["Gripe", "Broquitis"]
     pacientes.append(Enfermedades)

     print(pacientes)
     print("------------------------------")
    

def  agregado():
     Enfermedades = (input("Ingresar medicamentos: "))      
 
     mec = ["Ibuprofeno", "Talerdin", "Acetaminofen", "Famotidina", "Gemfibrozilo", "Actein"]
     mec.append(Enfermedades)

     print("Medicamentos entregados:", mec)
     print("------------------------------")
     

def  comparacion():
     ced = int(input("Ingrese el numero de cédula del primer paciente:"))
     otra = int(input("Ingrese el numero de cédula del segundo paciente:"))
     segundo = (input("Digite su nombre: "))   
 
     P1 = [ced, primero]
     P2 = [otra, segundo]

     primero = {'Nombre': 'Karla','Apellido': 'Wood','Cedula' : 15,'enfermedades': ['Diabetes', 'Colesterol'],'medicamentos': ['Ibuprofeno', 'Famotidina']}

     segundo = {'nombre': 'Andrey','apellido': 'Ruiz','Cedula' : 23,'enfermedades': ['Anemia', 'Asma'],'medicamentos': ['Acetaminofen', 'Gemfibrozilo']}

     print("Los pacientes no poseen información similar: ")
     print(primero)
     print(segundo)
     

     print(P1 == P2)
     print("------------------------------")


    
menu()


 

