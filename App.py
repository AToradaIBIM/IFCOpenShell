#Clase para hacer pruebas ¡NO ESTÁN TODOS LOS MÉTODOS USADOS AQUÍ!

import Controlador as cont

#Cargamos el archivo
cont.loadFile('C:/Users/Sabiin/Downloads/Proyecto1_Normal.ifc')

#Mostramos los sitios, construcciones y pisos
cont.showSites()
cont.showBuildings()
cont.showStoreys()

#Mostramos cuantas puertas tiene nuestro piso (A mejorar el sistema de obtener los datos)
print(cont.HowMuchOfAnObjectHasOtherObject("IfcDoor",cont.Storeys()[0][1]))

#Mostramos en que piso está contenida nuestra puerta
cont.WhereIsCotainedMyObject(cont.GetListBuildingElementsByType("IfcDoor")[0])

#Mostramos el cálculo de la superficie de nuestros muros
print(cont.CalculateSurfaceOfAllWalls())

#Mostramos el programa que ha exportado el proyecto
cont.showProgram()

#Mostramos la versión con la que se ha exportado
cont.showVersionIFC()

#Mostramos los atributos de un objeto
cont.ShowAtributesOfAnObject(cont.GetListBuildingElementsByType("IfcDoor")[0])