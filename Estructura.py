from queue import Empty
import ifcopenshell
import ifcopenshell.util.element

def loadFile(filePath):
    global file
    file = ifcopenshell.open(filePath)
    global project
    project = file.by_type("IfcProject")[0]

def showProgram():
    print(project.OwnerHistory.OwningApplication.ApplicationFullName)

def showVersionIFC():
    print(file.schema)

def Sites():
    return project.IsDecomposedBy[0].RelatedObjects

def Buildings():
    list = []
    for site in Sites():
        list.append(site.IsDecomposedBy[0].RelatedObjects)

    return list

def Storeys():
    list = []
    for building in Buildings():
        list.append(building[0].IsDecomposedBy[0].RelatedObjects)
        
    return list

def showSites():
    for sites in Sites():
        print(sites)

def showBuildings():
    for buildings in Buildings():
        for building in buildings:
            print(building)

def showStoreys():
    for storeys in Storeys():
        for storey in storeys:
            print(storey)

#Maneras de hacer un Mostrar y un Mostrar De
#Métodos diferentes o con Parámetros por defecto

def GetListBuildingElements():
    #Este método devuelve un set ¿Posible otra solución más accesible?
    #Cambiado a List para poder acceder a casa elemento fácilmente
    building_elements = list()
    for element in file.by_type("IfcRoot"):
        if element.is_a("IfcBuildingElement"):
            building_elements.append(element)
    return building_elements

def GetListBuildingElementsByType(type):
    building_elements = list()
    for element in file.by_type("IfcRoot"):
        if element.is_a(type):
            building_elements.append(element)
    return building_elements



def ShowBuildingElements(type=""):
    set = GetListBuildingElements()
    for element in set:
        if type=="":
            print(element)
        else:  
            if element.is_a(type):
                print(element)

def ShowBuildingElements_OnlyType():
    set = GetListBuildingElements()

    for element in set:
        print(element.is_a())

def CountBuildingElement(type=""):
    count = 0
    for element in GetListBuildingElements():
        if type=="":
            count += 1
        else:  
            if element.is_a(type):
                count += 1
    return count


def HowMuchOfAnObjectHasOtherObject(contained, container):
    count = 0
    for element in container.ContainsElements[0].RelatedElements:
        if element.is_a(contained):
            count += 1
    return count

def WhereIsCotainedMyObject(object):
    try:
        print(ifcopenshell.util.element.get_container(object))
    except:
        print("Introduce un objeto")