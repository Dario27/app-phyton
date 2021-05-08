import os
import array
from datetime import date
import re

class CNEL:
    print("\n\t\tBIENVENIDOS AL SISTEMA DE CNEL")
    
    def mainMenu():

        def validarPlaca(placa):
            
            with open("Data/datos.txt", "r") as fileOpen:
                line = fileOpen.readlines()

            ok = True
            
            return ok

        def GrabarTxt(placa, tipo, anio, cliente1, numPlanillas):
            
            cliente = cliente1.split(" ")
            nomCliente = cliente[0]
            apeCliente = cliente[1]            
            nomClienteCompleto = nomCliente.capitalize() + " " + apeCliente.capitalize()
           
            currentDate = date.today() #Funcion que me devuelve la fecha actual del servidor
            anioActual = currentDate.year #Funcion que me devuelve el año actual del servidor
            difAnio = (anioActual-int(anio)) #sacamos la diferencia entre años 

            valor = int(numPlanillas) * 100 #calculo del valor de planillas

            file = open("Data/datos.txt", "a")
            file.write("Placa: " + placa+ "\n" )
            file.write("Tipo: " + tipo+ "\n" )
            file.write("Año: " + str(anio) + " [ "+ str(difAnio) +" Años]"+"\n" )
            file.write("Propietario: " + nomClienteCompleto+ "\n" )
            file.write("Planillas: " + str(numPlanillas) + " [ Total $" +str(valor) +" ] " + os.linesep)
            file.close()

        def valMedidor():
            print("Favor ingrese un codigo, tipo, año, propietario y cantidad de planillas, para terminar escribir SALIR:")
            
            try:
                dataMedidor = str(input("Ingrese los datos del medidor, …: "))
                if dataMedidor == "SALIR" or dataMedidor == "salir":
                    print("No se han ingresados medidores...\n")
                else :                    
                    StrArray = dataMedidor.split("-")
                    #print(len(StrArray))
                    if len(StrArray) == 5: #condicon para saber que haya escrito completo los datos
                        codigo  =  StrArray[0]
                        tipo    = StrArray[1]
                        year    = StrArray[2]
                        propiet = StrArray[3]
                        totPlan = StrArray[4] 
                        
                        placaOk = validarCodigoPlanilla(codigo) #Valida que la placa cumpla las determinaciones (primera letra en mayuscula seguido de tres digitos numericos)
                        anio = validarAnio(year)   #funcion que me devuelve si el año es mayor a 2000             
                        ok = validarPlaca(codigo) #Valida si el codigo ya está registrado en el archivo
                        if placaOk == True and anio == True and ok == True:
                            print("Grabandoo Datos...")
                            GrabarTxt(codigo, tipo, year, propiet, totPlan) #funcion que recibe como parametros los datos a grabar y crear el archivo txt
                        else:
                            if ok == False:
                                print("Placa ya Registrada, intente con otra placa. Gracias")
                            elif anio == False:
                                print("Año incorrecto, debe de ser mayor a 2000")
                            else:
                                print("Ha ocurrido un error, vuelva a intentarlo. Gracias")
                    else:
                        print("Datos incompletos, vuelva a intentarlo...")
            except:
                print("El campo no debe de estar vacío, vuelva a intentarlo...")
            
            
            
        def reportes():
            print("*** Generando Reporte....*** \n")
            try:
                with open("Data/datos.txt", "r") as fileOpen:
                    line = fileOpen.readlines()

                x = 0
                for item in line: #iteramos el file, para obtener la cantidad total de planillas registradas en el sistema
                    c = item.count("Placa:") #filtramos por la llave, en este caso nuestra llave será la placa
                    x += int(c) #incrementamos la suma total

                print("En total existen " +str(x) +" medidores y son los siguientes:\n")
                for reporte in line: #iteramos el file por segunda vez            
                    print(reporte.rstrip()) #mostramos el archivo en consola sin espacios entre lineas
            except:
                print("NO EXISTE INFORMACION INGRESADA")

        def diccionarioData():    
            print("opcion diccionario selccionada")  

        def validarAnio(anio):
            if int(anio) >= 2000:
                ok = True
            else:
                ok = False
            return ok
        
        def validarCodigoPlanilla(codigoP):
            #print(codigoP)
            if len(codigoP) >=1 and len(codigoP) <=4:
                placa = re.search("^[A-Z]", codigoP)
                placaNum = re.split("^[A-Z]", codigoP)
                OkPlaca = True               
                if placa and OkPlaca: 
                    print("valido placa ok" + placaNum[1])
                    placaOK = True
                else:
                    placaOK = False 
            else:
                print("Placa ingresada incorrecta solo se permite 4 caracteres....")
            return placaOK

        while True:
            print("\n** MENU PRINCIPAL **")
            print("\t1. Administrar Medidores ")
            print("\t2. Reportes ")
            print("\t3. Diccionario ")
            print("\t4. Salir ")
            
            try:         
                opcion = int(input("Ingrese una opcion: "))
                if opcion <= 3 and opcion > 0:
                    if opcion == 1:
                        valMedidor()
                    elif opcion == 2:
                        reportes()
                    elif opcion == 3:
                        diccionarioData()
                    else:
                        print("Opcion incorrecta... ")
                        break
                else:
                    print("Fin del programa... \n")
                    break           
            except:
                print("Eror de dato, escribir un numero del 1 al 4..")        
    mainMenu()
    
  
    