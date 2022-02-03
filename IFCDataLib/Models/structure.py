#Modulo con clase Structure que trabaja con la estructura de un proyecto y de manera superficial con los elementos de este

from queue import Empty
import ifcopenshell
import ifcopenshell.util.element


class Structure:
    
    def __init__(self):
        pass
    
    #Carga el archivo y el proyecto
    def load_file(self, file_path):
        global file
        file = ifcopenshell.open(file_path)
        global project
        project = file.by_type("IfcProject")[0]

    #Muestra el programa con el que está exportado el archivo
    def show_program(self):
        print(project.OwnerHistory.OwningApplication.ApplicationFullName)

    #Muestra la versión de IFC
    def show_version_ifc(self):
        print(file.schema)

    #Devuelve los sitios
    def sites(self):
        return project.IsDecomposedBy[0].RelatedObjects

    #Devuelve las construcciones
    def buildings(self):
        list = []
        for site in self.sites():
            list.append(site.IsDecomposedBy[0].RelatedObjects)

        return list

    #Devuelve los pisos
    def storeys(self):
        list = []
        for building in self.buildings():
            list.append(building[0].IsDecomposedBy[0].RelatedObjects)
            
        return list

    #Muestra los sitios
    def show_sites(self):
        for sites in self.sites():
            print(sites)

    #Muestra las construcciones
    def show_buildings(self):
        for buildings in self.buildings():
            for building in buildings:
                print(building)

    #Muestra los pisos
    def show_storeys(self):
        for storeys in self.storeys():
            for storey in storeys:
                print(storey)

    #Maneras de hacer un Mostrar y un Mostrar De
    #Métodos diferentes o con Parámetros por defecto

    #Método que se encarga de devolver una lista de BuildingElements
    #Este método devuelve un set ¿Posible otra solución más accesible?
    def get_list_building_elements(self):
        #Cambiado a List para poder acceder a cada elemento fácilmente
        building_elements = list()
        for element in file.by_type("IfcRoot"):
            if element.is_a("IfcBuildingElement"):
                building_elements.append(element)
        return building_elements

    #Método que se encarga de devoler una lista de elementos BuildingElements de un tipo en específico
    def get_list_building_elements_by_type(self, type):
        building_elements = list()
        for element in file.by_type("IfcRoot"):
            if element.is_a(type):
                building_elements.append(element)
        return building_elements

    #Método que se encarga de mostrar los BuildingElements (Todos o por tipo)
    def show_building_elements(self, type=""):
        set = self.get_list_building_elements()
        for element in set:
            if type=="":
                print(element)
            else:  
                if element.is_a(type):
                    print(element)

    #Método que se encarga de mostrar los tipos de los BuildingElements
    def show_building_elements_only_type(self):
        set = self.get_list_building_elements()

        for element in set:
            print(element.is_a())

    #Método que se encarga de contar los BuildingElements (Todos o por tipo)
    def count_building_element(self, type=""):
        count = 0
        for element in self.get_list_building_elements():
            if type=="":
                count += 1
            else:  
                if element.is_a(type):
                    count += 1
        return count

    #Método que se encarga da mostrar cuantos objetos de un tipo hay en otro objeto
    def how_much_of_an_object_has_other_object(self, contained, container):
        count = 0
        for element in container.ContainsElements[0].RelatedElements:
            if element.is_a(contained):
                count += 1
        return count

    #Método que se encarga de devolver dónde se encuentra un objeto (En el caso de una puerta el piso donde está)
    #¿Posible mostrar el muro en el que está? ¿Varía entre objetos? <- (Probablemente sí)
    def where_is_contained_my_object(self, object):
        try:
            print(ifcopenshell.util.element.get_container(object))
        except:
            print("Introduce un objeto")