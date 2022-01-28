#Clase para hacer pruebas ¡NO ESTÁN TODOS LOS MÉTODOS USADOS AQUÍ!

import Controlador as cont

#Cargamos el archivo
cont.loadFile('IFCOpenShell\Proyecto1_Normal.ifc')

#Mostramos los sitios, construcciones y pisos
print()
print("Muestra la estructura")
cont.showSites()
cont.showBuildings()
cont.showStoreys()

#Mostramos cuantas puertas tiene nuestro piso (A mejorar el sistema de obtener los datos)
print()
print("Muestra cuantas puertas tiene uno de nuestros pisos")
print(cont.HowMuchOfAnObjectHasOtherObject("IfcDoor",cont.Storeys()[0][1]))

#Mostramos en que piso está contenida nuestra puerta
print()
print("Muestra la en qué piso está la puerta")
cont.WhereIsCotainedMyObject(cont.GetListBuildingElementsByType("IfcDoor")[0])

#Mostramos el cálculo de la superficie de nuestros muros
print()
print("Muestra la superficie de TODOS los muros")
print(cont.CalculateSurfaceOfAllWalls())

#Mostramos el programa que ha exportado el proyecto
print()
print("Muestra de qué programa viene el proyecto")
cont.showProgram()

#Mostramos la versión con la que se ha exportado
print()
print("Muestra la versión de IFC usada")
cont.showVersionIFC()

#Comentado porque es muy largo en la consola
#Mostramos los atributos de un objeto
#print("Muestra las propiedades de la puerta")
#print()
#cont.ShowAtributesOfAnObject(cont.GetListBuildingElementsByType("IfcDoor")[0])