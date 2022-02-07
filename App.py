#Clase para hacer pruebas ¡NO ESTÁN TODOS LOS MÉTODOS USADOS AQUÍ!

from IFCDataLib import Controller

cont = Controller('IFCOpenShell\Proyecto1_Normal.ifc')
#Cargamos el archivo
#cont.loadFile('IFCOpenShell\Proyecto1_Normal.ifc')

#Mostramos los sitios, construcciones y pisos
print()
print("Muestra la estructura")
cont.show_sites()
cont.show_buildings()
cont.show_storeys()

#Mostramos cuantas puertas tiene nuestro piso (A mejorar el sistema de obtener los datos)
print()
print("Muestra cuantas puertas tiene uno de nuestros pisos")
print(cont.how_much_of_an_object_has_other_object("IfcDoor",cont.storeys()[0][1]))

#Mostramos en que piso está contenida nuestra puerta
print()
print("Muestra la en qué piso está la puerta")
cont.where_is_contained_my_object(cont.get_list_building_elements_by_type("IfcDoor")[0])

#Mostramos el cálculo de la superficie de nuestros muros
print()
print("Muestra la superficie de TODOS los muros")
print(cont.calculate_surface_of_all_walls())

#Mostramos el programa que ha exportado el proyecto
print()
print("Muestra de qué programa viene el proyecto")
cont.show_program()

#Mostramos la versión con la que se ha exportado
print()
print("Muestra la versión de IFC usada")
cont.show_version_ifc()

print()
print("Muestra las caras del muro")
print()
contador = 1
print(cont.get_list_building_elements_by_type("IfcWall")[0])
for caras in cont.get_all_faces_of_an_object(cont.get_list_building_elements_by_type("IfcWall")[0]):
    print("Cara " + str(contador))
    for points in caras:
        print(points)
    contador +=1
    print()

#Obtengo la altura de un muro
print("Altura de un muro")
print(cont.get_height_of_an_object(cont.get_list_building_elements_by_type("IfcWall")[0]))

#Comentado porque es muy largo en la consola
#Mostramos los atributos de un objeto
#print("Muestra las propiedades de la puerta")
#print()
#cont.ShowAtributesOfAnObject(cont.GetListBuildingElementsByType("IfcDoor")[0])