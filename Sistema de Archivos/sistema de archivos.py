import os
import os.path
import tkinter
from tkinter import filedialog


def selecciona_ruta():
    while True:
        raiz= tkinter.Tk()
        raiz.title("Explorando archivos.")
        raiz.iconify() # Oculto la ventana
            
        ruta=filedialog.askopenfilename() #Obtengo la ruta seleccionada
        raiz.destroy() #Queda pendiente   
        
        ubicacion, extension=os.path.splitext(ruta)
        #nombre_archivo=os.path.basename(ruta)
        nombre_archivo= os.path.splitext(os.path.basename(ruta))[0] #?

        if extension==".txt":
            print("\nRuta del archivo seleccionado: {}\nNombre del archivo: {}\nExtensión del archivo: {}".format(ubicacion, nombre_archivo, extension))                    
            return ruta
            break
            
        else:
            print("\nSeleccione un archivo de tipo texto, intentelo nuevamente")        
            

def metodo(mi_ruta):   
    
    while True:
        print("\n-OPCIONES DISPONIBLES- \n1.-Insertar \n2.-Modificar \n3.-Eliminar \n4.-Localizar y mostrar un registro\n5.-Calcular promedio de edades\n6.-Ver un ASCCI ART\n7.-Salir")
        opcion=int(input("Selccione una opción: "))
        
    #opción 1    
        if opcion==1:
            
            contador=0

            #mi_archivo=mi_ruta
            mi_archivo=open(mi_ruta)
            mi_lista= mi_archivo.readlines() #Archivo convertido en lista
            mi_archivo.close()
            
            #Cuento el número de ID registradas para poder saber si sobre pasa el número permitido (10)
            for j in range(len(mi_lista)):
                if mi_lista[j][0:4]==("Id: "):
                    contador+=1            
            
            if os.stat(mi_ruta).st_size == 0: #Determino si esta vacío mi .txt                           
                    
                    
                    archivo0=open(mi_ruta, 'w')

                    id_alumno=input("Ingrese id del alumno: ")
                    archivo0.write("Id: "+id_alumno+"\n")

                    nombre= input("Ingrese nombre del alumno: ")
                    archivo0.write("Nombre: "+nombre+"\n")

                    paterno= input("Ingrese apellido paterno del alumno: ")
                    archivo0.write("Apellido paterno: "+paterno+"\n")

                    materno=input("Ingrese apellido materno del alumno: ")
                    archivo0.write("Apellido materno: "+materno+"\n")

                    edad= input("Ingrese edad del alumno: ")
                    archivo0.write("Edad: "+edad)

                    print("\n******* Alumno registrado correctamente *******")
                    
                    archivo0.close()

            elif  os.stat(mi_ruta).st_size != 0: #Evaluo si mi archivo no esta vacio
                    
                    archivo2=open(mi_ruta, 'a')
                    ite=0
                    
                    id_alumno=input("Ingrese id del alumno: ")
                    
                    #Cuento si se repite la ID
                    for j in range(len(mi_lista)):
                        if mi_lista[j]==("Id: "+id_alumno+"\n"):                        
                            ite+=1                                            

                    #Evaluo si la ID no existe
                    if ite==0:                   
                        archivo2.write("\n\nId: "+id_alumno+"\n")

                        nombre= input("Ingrese nombre del alumno: ")
                        archivo2.write("Nombre: "+nombre+"\n")

                        paterno= input("Ingrese apellido paterno del alumno: ")
                        archivo2.write("Apellido paterno: "+paterno+"\n")

                        materno=input("Ingrese apellido materno del alumno: ")
                        archivo2.write("Apellido materno: "+materno+"\n")

                        edad= input("Ingrese edad del alumno: ")
                        archivo2.write("Edad: "+edad)
                        
                        print("\n******* Alumno registrado correctamente *******")

                    #Si no existe la ID, mandara mensaje de que ya existe la ID                        
                    else:
                        print("\n******* Id ya registrada *******")                 
                                        
                    archivo2.close()
            
            #Evalua si sobrepaso el número de ID permitidos        
            elif contador>=10:
                print("Se supero el número máximo de alumnos registrados (10)")        
         
    #Opción 2
        elif opcion==2:

            mi_archivo=open(mi_ruta)
            mi_lista= mi_archivo.readlines() #Archivo convertido en lista
            mi_archivo.close()        
            ite=0
            cuen=0
            c=0

            busca_id=input("Ingrese el ID por BUSCAR: ")
            
            for i in range(len(mi_lista)):
                if mi_lista[i]==("Id: "+busca_id+"\n") or mi_lista[i]==("Id: "+busca_id):                     
                    print("Sí  encontro ID") 
                    c+=1
                    nueva_id= input("Ingrese NUEVA ID: ")                
                    for j in range(len(mi_lista)):
                        if mi_lista[j]==("Id: "+nueva_id+"\n"):                        
                            ite+=1 
                        if mi_lista[j][0:4]=="Id: ":
                            cuen+=1

                    if ite!=1: 
                        nuevo_nombre= input("Ingrese NUEVO Nombre: ")
                        nuevo_paterno= input("Ingrese NUEVA Apellido Paterno: ")
                        nuevo_materno= input("Ingrese NUEVA Apellido Materno: ")
                        nueva_edad= input("Ingrese NUEVA Edad: ")

                        mi_lista[i]="Id: "+nueva_id+"\n"
                        mi_lista[i+1]="Nombre: "+nuevo_nombre+"\n"
                        mi_lista[i+2]="Apellido paterno: "+nuevo_paterno+"\n"
                        mi_lista[i+3]="Apellido materno: "+nuevo_materno+"\n"
                        mi_lista[i+4]="Edad: "+nueva_edad+"\n"
                        print("Archivo modificado satisfactoriamente")
                        
                        mi_archivo = open(mi_ruta, "w")
                        new_file_contents="".join(mi_lista)
                        
                        mi_archivo.write(new_file_contents)
                        mi_archivo.close

                        #Hasta aquí
                        readable_file = open(mi_ruta)
                        read_file = readable_file.read()                                                
                        mi_archivo.close() 
                        
                    elif ite==1:
                        print("Id ya registrado")                
                                                    
            if cuen==c:
                print("No se encontro alumno con esa Id")            
                mi_archivo.close()        

    #Opción 3          
        elif opcion==3:
            mi_archivo=open(mi_ruta)
            mi_lista= mi_archivo.readlines() #Archivo convertido en lista
            mi_archivo.close()        
            
            cuen=0 #Cuenta cuantas ID hay en el archivo(txt)
            c=0    

            busca_id=input("Ingrese el ID por ELIMINAR: ")

            for j in range(len(mi_lista)):                    
                if mi_lista[j][0:4]=="Id: ":
                    cuen+=1

            for i in range(len(mi_lista)):
                if mi_lista[i]==("Id: "+busca_id+"\n") or mi_lista[i]==("Id: "+busca_id):
                    c+=1                     
                    print("Sí  encontro ID")                                             
                    
                    mi_lista[i-1]=""
                    mi_lista[i]=""
                    mi_lista[i+1]=""
                    mi_lista[i+2]=""
                    mi_lista[i+3]=""
                    mi_lista[i+4]=""                                                                                  
                    
                    mi_archivo = open(mi_ruta, "w")                    
                    new_file_contents="".join(mi_lista)                    
                    mi_archivo.write(new_file_contents)                                        

                    #Hasta aquí
                    readable_file = open(mi_ruta)
                    read_file = readable_file.read()                                                        
                    
                    print("\n******* Archivo eliminado satisfactoriamente *******")
                    mi_archivo.close()


                    #------------Aqui voy a hacer limpieza de residuos de lineas------------
                    mi_archivo2=open(mi_ruta)
                    mi_lista2= mi_archivo2.readlines() #Archivo convertido en lista
                    mi_archivo2.close()
                    print(mi_lista2)                    
                                        
                    poscicion=0
                    while poscicion<len(mi_lista2):                        
                            if str(mi_lista2[poscicion][-1:-2])==("\n") and str(mi_lista2[poscicion+1])=="\n":
                                mi_lista2.pop(poscicion+1)                                
                                poscicion+=1                                                        
                            else:
                                poscicion+=1

                    
                    if mi_lista2[-1][0:6]=="Edad: " or mi_lista2[-1]=="\n":  
                        print("S{i")
                        almacen="".join(mi_lista2[-1])
                        almacen=almacen.rstrip()
                        print(almacen)  
                        mi_lista2[-1]=almacen
                    
                    mi_archivo = open(mi_ruta, "w")                    
                    new_file_contents="".join(mi_lista2)
                    
                    mi_archivo.write(new_file_contents)                                        

                    #Hasta aquí
                    readable_file = open(mi_ruta)
                    read_file = readable_file.read()
                    mi_archivo.close()
                    print(mi_lista2)  
                    
            if c==0:
                print("\n******* No se encontro alumno con esa Id *******")
                mi_archivo.close()                                      
        
    #Opción 4
        elif opcion==4:
            mi_archivo=open(mi_ruta)
            mi_lista= mi_archivo.readlines() #Archivo convertido en lista
            mi_archivo.close()
            #print(mi_lista)            
            estado=False
            
            busca_id=input("Ingrese el ID por BUSCAR: ")                                  

            for i in range(len(mi_lista)):
                if mi_lista[i]==("Id: "+busca_id+"\n") or mi_lista[i]==("Id: "+busca_id):                     
                    print("\nSí  encontro ID\n")

                    print(mi_lista[i].rstrip())
                    print(mi_lista[i+1].rstrip())
                    print(mi_lista[i+2].rstrip())
                    print(mi_lista[i+3].rstrip())
                    print(mi_lista[i+4].rstrip())                                 
                    estado=True                    

                    #Hasta aquí
                    readable_file = open(mi_ruta)
                    read_file = readable_file.read()                                
                    mi_archivo.close()                                            

            if estado==False:
                print("\nNo se encontro alumno con esa Id")                
                mi_archivo.close()  

    #Opción 5
        elif opcion==5:

            archivo=open(mi_ruta, 'r+')
            con=0

            #Archivo vacío        
            if os.stat(mi_ruta).st_size == 0:
                print("El archivo esta vacío, no se pueden modificar datos")
            
            #Archivo diferente de vacío
            else:            
                mi_archivo=open(mi_ruta)
                mi_lista= mi_archivo.readlines() #Archivo convertido en lista                t
                mi_archivo.close()                                      
                
                edad=0
                div=0
                edad_guardada=""
                
                for i in range(len(mi_lista)):
                    if mi_lista[i][0:6]==("Edad: "):
                        div+=1
                        edad_guardada="".join(mi_lista[i][5:])
                        #edad_guardada=edad_guardada.rstrip()                        
                        edad+=float(edad_guardada.rstrip())
                
                #print(mi_lista[4][5:])            
                promedio=+edad/div
                print("El promedio de edades es: {}". format(promedio))
                archivo.close()                       
        
    #Opción 6
        elif opcion==6:        
            print("")
            print("         _nnnn_                      ")
            print("        dGGGGMMb     ,"""""""""""""".")
            print("       @p~qp~~qMb    | Linux Rules! |")
            print("       M|@||@) M|   _;..............'")
            print("       @,----.JM| -'")
            print("      JS^\__/  qKL")
            print("     dZP        qKRb")
            print("    dZP          qKKb")
            print("   fZP            SMMb")
            print("   HZM            MMMM")
            print("   FqM            MMMM")
            print(" __|  .        |\dS qML")
            print(" |    `.       |    \Zq")
            print("_)      \.___.,|     . ")
            print("\____   )MMMMMM|   .'")
            print("     `-'       `--' hjm")
 
    #Opción 7
        elif opcion==7:
            break                             
    #Else
        else:
            print("\nOpción no disponible, intente nuevamente con una de las opciones del menú")
    
la_ruta=selecciona_ruta()
metodo(la_ruta)