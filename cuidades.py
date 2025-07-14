import requests
import json
import time
import subprocess

def BorrarPantalla():
        '''Funcion para borrar la pantalla'''
        subprocess.call('cls', shell=True)  


API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjRmYmM1NWZjYjMxYTRhMTc5NGNhZDY5NDFjOWJhODU2IiwiaCI6Im11cm11cjY0In0="

#####################################################################
#Diccionarios

tipos_vehiculos = {"Auto" : "driving-car",
                   "Bicicleta" : "cycling-regular", 
                   "A pie" : "foot-walking"}
#1=Santiago 2=San Antonio
coordenadasCl = {"Santiago" : "-70.6693,-33.4489", 
                 "San Antonio" : "-71.6127,-33.5932"}
#1=Buenos Aires 2=Córdoba 3=Mendoza
coordenadasAr = {"Buenos Aires" : "-58.3816,-34.6037",
                 "Córdoba" : "-64.1888,-31.4201",
                 "Mendoza" : "-68.8440,-32.8894"}

#####################################################################
#Base para armar el url de la consulta final
url_base = "https://api.openrouteservice.org/v2/directions/"


while True:
    #####################################################################
    #Aqui inicia el menu
    print("---------------------------------------------------------------------")
    print("Este programa entrega informacion sobre la ruta entre una ciudad de Chile y una de Argentina,\n" \
    "a continuacion se muestra la lista de ciudades disponibles.")
    print("---------------------------------------------------------------------")
    print("Ciudades Chile: \n1.-Santiago\n2.-San Antonio")
    print("Ciudades Argentina: \n1.-Buenos Aires\n2.-Córdoba\n3.-Mendoza")
    print("")
    inicio = input("Por favor ingrese el numero de una ciudad de Chile para iniciar la ruta: ")         #Este pide la ciudad de chile
    final = input("Por favor ingrese el numero de una ciudad de Argentina para finalizar la ruta: ")    #Este pide la ciudad de argentina
    BorrarPantalla()
    time.sleep(1)
    print("---------------------------------------------------------------------")
    print("Selecciona un medio de transporte")
    print("---------------------------------------------------------------------")
    print("Medios de transporte: ")
    print("1.- Auto")
    print("2.- Bicicleta")
    print("3.- A pie")
    print("")
    medioT = str(input("Ingrese su opción: "))      #Este pide el medio de transporte
    print("")
    BorrarPantalla()
    time.sleep(1)
    print("---------------------------------------------------------------------")
    opt = input("Si desea continuar presione 'enter'\nDe lo contrario presione la letra 's' para salir\n>>> ")  #Esta es la opcion para salir o continuar
    opt = opt.upper()   #Este transforma el anterior a mayusculas

    BorrarPantalla()
    time.sleep(1)

    if opt != "S":                      #Si es distinto de 'S'continua el programa
        # Determina el medio de transporte
        # Relaciona el valor solicitado al usuario de la variable medioT con el valor respectivo en el diccionario
        if medioT == "1":
            trans = tipos_vehiculos["Auto"]
        elif medioT == "2":
            trans = tipos_vehiculos["Bicicleta"]
        elif medioT == "3":
            trans = tipos_vehiculos["A pie"]
        else:
            print("Opción de transporte no válida")
            continue

        # Determinar la ciudad de inicio en Chile
        if inicio == "1":
            inicioC = coordenadasCl["Santiago"]
        elif inicio == "2":
            inicioC = coordenadasCl["San Antonio"]
        else:
            print("Ciudad de inicio no válida")
            continue

        # Determinar la ciudad de destino en Argentina
        if final == "1":
            finC = coordenadasAr["Buenos Aires"]
        elif final == "2":
            finC = coordenadasAr["Córdoba"]
        elif final == "3":
            finC = coordenadasAr["Mendoza"]
        else:
            print("Ciudad de destino no válida")
            continue
        
        # Aqui se arma la URL final para la solicitud 
        URL = url_base + trans + "?api_key=" + API_KEY + "&start=" + inicioC + "&end=" + finC
        #print(URL)
        # Aqui se hace la solicitud
        respuesta = requests.get(URL)
        # Aqui se tranformo a json para poder verlo en pantalla
        rjson = respuesta.json()
        #print(rjson)

        '''with open('ruta.json', 'w', encoding='utf-8') as f:
            json.dump(respuesta.json(), f, ensure_ascii=False, indent=4)'''
        #Extraemos el valor de la distancia total del archivo json
        totalDistance = rjson["features"][0]['properties']['summary']['distance']
        totalDuration = rjson['features'][0]['properties']['summary']['duration']
        nmediot = int(medioT)
        ncini = int(inicio)
        ncend = int(final)
        c1 = list(coordenadasCl.keys())[ncini - 1]
        c2 = list(coordenadasAr.keys())[ncend - 1]
        mt = list(tipos_vehiculos.keys())[nmediot - 1]
        steps = rjson['features'][0]['properties']['segments'][0]['steps']

        #print(c1)
        #print(c2)
        #print(mt)

        print("---------------------------------------------------------------------")
        print(f"El medio de transporte utilizado es: {mt}")
        print(f"La distancia total entre {c1} y {c2} es: {totalDistance / 1000:.2f} km. o {((totalDistance / 1000) * 0.621371):.2f} mi.")
        print(f"La duración del recorrido entre {c1} y {c2} es: {totalDuration / 3600:.2f} horas")
        print("--- INSTRUCCIONES DE LA RUTA ---")
        for idx, step in enumerate(steps, 1):
            print(f"{idx:>2}. {step['instruction']}")
        print("---------------------------------------------------------------------")
        input("Precione 'enter' para continuar.\n>>>")
        BorrarPantalla()




    else:
        break