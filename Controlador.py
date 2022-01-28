#Clase que se encarga de intermediar todos los métodos y pasarle a Datos las referencias desde Estructura

import Estructura, Datos

def loadFile(filePath):
    Estructura.loadFile(filePath)

def showProgram():
    Estructura.showProgram()

def showVersionIFC():
    Estructura.showVersionIFC()

def Sites():
    return Estructura.Sites()

def Buildings():
    return Estructura.Buildings()

def Storeys():
    return Estructura.Storeys()

def showSites():
    Estructura.showSites()

def showBuildings():
    Estructura.showBuildings()

def showStoreys():
    Estructura.showStoreys()

def GetListBuildingElements():
    return Estructura.GetListBuildingElements()

def GetListBuildingElementsByType(type):
    return Estructura.GetListBuildingElementsByType(type)

def ShowBuildingElements(type=""):
    Estructura.ShowBuildingElements(type)

def ShowBuildingElements_OnlyType():
    Estructura.ShowBuildingElements_OnlyType()

def CountBuildingElement(type=""):
    return Estructura.CountBuildingElement(type)

def HowMuchOfAnObjectHasOtherObject(contained, container):
    return Estructura.HowMuchOfAnObjectHasOtherObject(contained, container)

def WhereIsCotainedMyObject(object):
    Estructura.WhereIsCotainedMyObject(object)

def CalculateSurfaceOfAnObject(Object):
    return Datos.CalculateSurfaceOfAnObject(Object)

def CalculateSurfaceOfAllWalls():
    return Datos.CalculateSurfaceOfAllWalls(Estructura.GetListBuildingElementsByType("IfcWall"))

def CalculateSurfaceOfAllDoors():
    return Datos.CalculateSurfaceOfAllDoors(Estructura.GetListBuildingElementsByType("IfcDoor"))

#En desarrollo
def CalculateSurfaceOfAllRoofs():
    return Datos.CalculateSurfaceOfAllRoofs(Estructura.GetListBuildingElementsByType("IfcRoof"))

def ShowAtributesOfAnObject(object):
    Datos.ShowAtributesOfAnObject(object)