#Clase que se encarga de cálculos y propiedades específicas

import math
from ifcopenshell import geom
import ifcopenshell.util.element
settings = geom.settings()

#Calcula la distancia entre dos vértices
def DistanceBetweenTwoPoints3D(x1, y1, z1, x2, y2, z2):
    d = math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) +
                math.pow(z2 - z1, 2)* 1.0)
    return d

#Obtiene los vértices de un objecto
def GetTheVertsOfAnObject(Object):
    shape = geom.create_shape(settings, Object)
    verts = shape.geometry.verts
    grouped_verts = [[verts[i], verts[i + 1], verts[i + 2]] for i in range(0, len(verts), 3)]
    return grouped_verts

#Obtiene las caras de un objeto
def GetTheFacesOfAnObject(Object):
    shape = geom.create_shape(settings, Object)
    faces = shape.geometry.faces
    grouped_faces = [[faces[i], faces[i + 1], faces[i + 2]] for i in range(0, len(faces), 3)]
    return grouped_faces

#Calcula el área del triángulo rectágulo pasando sus 3 distancias y descartando su hipotenusa
def AreaTriangleWithThreeNumbers(d1,d2,d3):
    if (d1 > d2) and (d1 > d3):
        area = (d2 * d3)/2
    elif (d2 > d1) and (d2 > d3):
        area = (d1 * d3)/2
    else:
        area = (d2 * d1)/2
    return area

#Calcula la superficie de un objeto
def CalculateSurfaceOfAnObject(Object):
    surface = 0
    #Obtengo los datos de los vértices y las caras con referencias a sus vértices
    verts = GetTheVertsOfAnObject(Object) # x y z
    faces = GetTheFacesOfAnObject(Object) #f1v1, f1v2, f1v3...
    
    #Calculo la distancia entre los puntos de un triángulo rectángulo
    #De 0 a 1, de 1 a 2 y de 0 a 2.
    for face in faces:
        d1 = DistanceBetweenTwoPoints3D(verts[face[0]][0],#x₁
                                        verts[face[0]][1],#x₂
                                        verts[face[0]][2],#y₁
                                        verts[face[1]][0],#y₂
                                        verts[face[1]][1],#z₁
                                        verts[face[1]][2])#z₂
        
        d2 = DistanceBetweenTwoPoints3D(verts[face[1]][0],#x₁
                                        verts[face[1]][1],#x₂
                                        verts[face[1]][2],#y₁
                                        verts[face[2]][0],#y₂
                                        verts[face[2]][1],#z₁
                                        verts[face[2]][2])#z₂

        d3 = DistanceBetweenTwoPoints3D(verts[face[0]][0],#x₁
                                        verts[face[0]][1],#x₂
                                        verts[face[0]][2],#y₁
                                        verts[face[2]][0],#y₂
                                        verts[face[2]][1],#z₁
                                        verts[face[2]][2])#z₂
        
        #Calcula el área de la cara pasango la distancia entre los vértices
        surface += AreaTriangleWithThreeNumbers(d1,d2,d3)

    return surface

#Calculamos la superficie de todos los muros
def CalculateSurfaceOfAllWalls(walls):
    surface = 0
    for wall in walls:
        surface += CalculateSurfaceOfAnObject(wall)
    return surface

#Calculamos la superficie de todas las puertas
def CalculateSurfaceOfAllDoors(doors):
    surface = 0
    for door in doors:
        surface += CalculateSurfaceOfAnObject(door)
    return surface

#Calculamos la superficie de todos los tejados (En desarrollo)
def CalculateSurfaceOfAllRoofs(roofs):
    surface = 0
    for roof in roofs:
        surface += CalculateSurfaceOfAnObject(roof)
    return surface

#Mostramos los atributos de un objeto
def ShowAtributesOfAnObject(object):
    for key, pset in ifcopenshell.util.element.get_psets(object).items():
    
        print("         --- "+key + " --- ")
        print()
        for keypset, value in pset.items():
            print("  "+keypset)
            print("    * " + str(value) )
    print()