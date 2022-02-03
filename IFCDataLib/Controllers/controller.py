#Modulo con clase Controller que se encarga de intermediar todos los métodos y pasarle a Datos las referencias desde Estructura

from IFCDataLib.Models.structure import Structure
from IFCDataLib.Models.data import Data

class Controller:
    
    def __init__(self, filePath):
        self.structure = Structure()
        self.data = Data()
        self.load_file(filePath)

    def load_file(self, file_path):
        self.structure.load_file(file_path)

    def show_program(self):
        self.structure.show_program()

    def show_version_ifc(self):
        self.structure.show_version_ifc()

    def sites(self):
        return self.structure.sites()

    def buildings(self):
        return self.structure.buildings()

    def storeys(self):
        return self.structure.storeys()

    def show_sites(self):
        self.structure.show_sites()

    def show_buildings(self):
        self.structure.show_buildings()

    def show_storeys(self):
        self.structure.show_storeys()

    def get_list_building_elements(self):
        return self.structure.get_list_building_elements()

    def get_list_building_elements_by_type(self, type):
        return self.structure.get_list_building_elements_by_type(type)

    def show_building_elements(self, type=""):
        self.structure.show_building_elements(type)

    def show_building_elements_only_type(self):
        self.structure.show_building_elements_only_type()

    def count_building_element(self, type=""):
        return self.structure.count_building_element(type)

    def how_much_of_an_object_has_other_object(self, contained, container):
        return self.structure.how_much_of_an_object_has_other_object(contained, container)

    def where_is_contained_my_object(self, object):
        self.structure.where_is_contained_my_object(object)

    def calculate_surface_of_an_object(self, object):
        return self.data.calculate_surface_of_an_object(object)

    def calculate_surface_of_all_walls(self):
        return self.data.calculate_surface_of_all_walls(self.structure.get_list_building_elements_by_type("IfcWall"))

    def calculate_surface_of_all_doors(self):
        return self.data.calculate_surface_of_all_doors(self.structure.get_list_building_elements_by_type("IfcDoor"))

    #En desarrollo
    def calculate_surface_of_all_roofs(self):
        return self.data.calculate_surface_of_all_roofs(self.structure.get_list_building_elements_by_type("IfcRoof"))

    def show_atributes_of_an_object(self, object):
        self.data.show_atributes_of_an_object(object)
    
    def get_all_faces(self, object):
        return self.data.get_all_faces(object)