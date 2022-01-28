#Clase que trabaja con la estructura de un proyecto y de manera superficial con los elementos de este

from queue import Empty
import ifcopenshell
import ifcopenshell.util.element

#Carga el archivo y el proyecto
def loadFile(filePath):
    global file
    file = ifcopenshell.open(filePath)
    global project
    project = file.by_type("IfcProject")[0]

#Muestra el programa con el que está exportado el archivo
def showProgram():
    print(project.OwnerHistory.OwningApplication.ApplicationFullName)

#Muestra la versión de IFC
def showVersionIFC():
    print(file.schema)

#Devuelve los sitios
def Sites():
    return project.IsDecomposedBy[0].RelatedObjects

#Devuelve las construcciones
def Buildings():
    list = []
    for site in Sites():
        list.append(site.IsDecomposedBy[0].RelatedObjects)

    return list

#Devuelve los pisos
def Storeys():
    list = []
    for building in Buildings():
        list.append(building[0].IsDecomposedBy[0].RelatedObjects)
        
    return list

#Muestra los sitios
def showSites():
    for sites in Sites():
        print(sites)

#Muestra las construcciones
def showBuildings():
    for buildings in Buildings():
        for building in buildings:
            print(building)

#Muestra los pisos
def showStoreys():
    for storeys in Storeys():
        for storey in storeys:
            print(storey)

#Maneras de hacer un Mostrar y un Mostrar De
#Métodos diferentes o con Parámetros por defecto

#Método que se encarga de devolver una lista de BuildingElements
#Este método devuelve un set ¿Posible otra solución más accesible?
def GetListBuildingElements():
    #Cambiado a List para poder acceder a cada elemento fácilmente
    building_elements = list()
    for element in file.by_type("IfcRoot"):
        if element.is_a("IfcBuildingElement"):
            building_elements.append(element)
    return building_elements

#Método que se encarga de devoler una lista de elementos BuildingElements de un tipo en específico
def GetListBuildingElementsByType(type):
    building_elements = list()
    for element in file.by_type("IfcRoot"):
        if element.is_a(type):
            building_elements.append(element)
    return building_elements

#Método que se encarga de mostrar los BuildingElements (Todos o por tipo)
def ShowBuildingElements(type=""):
    set = GetListBuildingElements()
    for element in set:
        if type=="":
            print(element)
        else:  
            if element.is_a(type):
                print(element)

#Método que se encarga de mostrar los tipos de los BuildingElements
def ShowBuildingElements_OnlyType():
    set = GetListBuildingElements()

    for element in set:
        print(element.is_a())

#Método que se encarga de contar los BuildingElements (Todos o por tipo)
def CountBuildingElement(type=""):
    count = 0
    for element in GetListBuildingElements():
        if type=="":
            count += 1
        else:  
            if element.is_a(type):
                count += 1
    return count

#Método que se encarga da mostrar cuantos objetos de un tipo hay en otro objeto
def HowMuchOfAnObjectHasOtherObject(contained, container):
    count = 0
    for element in container.ContainsElements[0].RelatedElements:
        if element.is_a(contained):
            count += 1
    return count

#Método que se encarga de devolver dónde se encuentra un objeto (En el caso de una puerta el piso donde está)
#¿Posible mostrar el muro en el que está? ¿Varía entre objetos? <- (Probablemente sí)
def WhereIsCotainedMyObject(object):
    try:
        print(ifcopenshell.util.element.get_container(object))
    except:
        print("Introduce un objeto")