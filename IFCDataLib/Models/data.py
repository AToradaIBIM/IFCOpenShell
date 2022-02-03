#Modulo con clase Data que se encarga de cálculos y propiedades específicas

import math
from ifcopenshell import geom
import ifcopenshell.util.element
from shapely.ops import triangulate
from shapely.geometry import Polygon, MultiPoint
from geometer import *
import numpy as np
#from shapely.geometry import Point, Plane


class Data:
    
    def __init__(self):
        self.settings = geom.settings()

    #Calcula la distancia entre dos vértices
    def distance_between_two_points_3d(self, x1, y1, z1, x2, y2, z2):
        d = math.sqrt(math.pow(x2 - x1, 2) +
                    math.pow(y2 - y1, 2) +
                    math.pow(z2 - z1, 2)* 1.0)
        return d

    #Obtiene los vértices de un objecto
    def get_the_verts_of_an_object(self, object):
        shape = geom.create_shape(self.settings, object)
        verts = shape.geometry.verts
        grouped_verts = [[verts[i], verts[i + 1], verts[i + 2]] for i in range(0, len(verts), 3)]
        return grouped_verts

    #Obtiene las caras de un objeto
    def get_the_faces_of_an_object(self, object):
        shape = geom.create_shape(self.settings, object)
        faces = shape.geometry.faces
        grouped_faces = [[faces[i], faces[i + 1], faces[i + 2]] for i in range(0, len(faces), 3)]
        return grouped_faces

    #Calcula el área del triángulo rectágulo pasando sus 3 distancias y descartando su hipotenusa
    def area_triangle_with_three_numbers(self, d1,d2,d3):
        if (d1 > d2) and (d1 > d3):
            area = (d2 * d3)/2
        elif (d2 > d1) and (d2 > d3):
            area = (d1 * d3)/2
        else:
            area = (d2 * d1)/2
        return area

    #Calcula la superficie de un objeto
    def calculate_surface_of_an_object(self, object):
        surface = 0
        #Obtengo los datos de los vértices y las caras con referencias a sus vértices
        verts = self.get_the_verts_of_an_object(object) # x y z
        faces = self.get_the_faces_of_an_object(object) #f1v1, f1v2, f1v3...
        
        #Calculo la distancia entre los puntos de un triángulo rectángulo
        #De 0 a 1, de 1 a 2 y de 0 a 2.
        for face in faces:
            d1 = self.distance_between_two_points_3d(verts[face[0]][0],#x₁
                                            verts[face[0]][1],#y₁
                                            verts[face[0]][2],#z₁
                                            verts[face[1]][0],#x₂
                                            verts[face[1]][1],#y₂
                                            verts[face[1]][2])#z₂
            
            d2 = self.distance_between_two_points_3d(verts[face[1]][0],#x₁
                                            verts[face[1]][1],#y₁
                                            verts[face[1]][2],#z₁
                                            verts[face[2]][0],#x₂
                                            verts[face[2]][1],#y₂
                                            verts[face[2]][2])#z₂

            d3 = self.distance_between_two_points_3d(verts[face[0]][0],#x₁
                                            verts[face[0]][1],#y₁
                                            verts[face[0]][2],#z₁
                                            verts[face[2]][0],#x₂
                                            verts[face[2]][1],#y₂
                                            verts[face[2]][2])#z₂
            
            #Calcula el área de la cara pasango la distancia entre los vértices
            surface += self.area_triangle_with_three_numbers(d1,d2,d3)
            
        #pointOne = Point(1,2,3)
        #pointTwo = Point(1,2,3)
        #point3 = Point(1,2,3)
        #Plane(pointOne,pointTwo,point3)
        return surface

    #Calculamos la superficie de todos los muros
    def calculate_surface_of_all_walls(self, walls):
        surface = 0
        for wall in walls:
            surface += self.calculate_surface_of_an_object(wall)
        return surface

    #Calculamos la superficie de todas las puertas
    def calculate_surface_of_all_doors(self, doors):
        surface = 0
        for door in doors:
            surface += self.calculate_surface_of_an_object(door)
        return surface

    #Calculamos la superficie de todos los tejados (En desarrollo)
    def calculate_surface_of_all_roofs(self, roofs):
        surface = 0
        for roof in roofs:
            surface += self.calculate_surface_of_an_object(roof)
        return surface

    #Mostramos los atributos de un objeto
    def show_atributes_of_an_object(self, object):
        for key, pset in ifcopenshell.util.element.get_psets(object).items():
        
            print("         --- "+key + " --- ")
            print()
            for keypset, value in pset.items():
                print("  "+keypset)
                print("    * " + str(value) )
        print()
    
    def get_all_faces(self, object):
        #Obtengo los datos de los vértices y las caras con referencias a sus vértices

        verts = self.get_the_verts_of_an_object(object) # x y z
        faces = self.get_the_faces_of_an_object(object) #f1v1, f1v2, f1v3...
        
        grouped_faces = []
        for face in faces:
            #Obtiene los vértices
            face_vert1 = face[0]
            face_vert2 = face[1]
            face_vert3 = face[2]
            #Luego los hace puntos
            point_vert1 = Point(verts[face_vert1][0],#x₁
                             verts[face_vert1][1],#y₁
                             verts[face_vert1][2])#z₁
            
            point_vert2 = Point(verts[face_vert2][0],#x₂
                             verts[face_vert2][1],#y₂
                             verts[face_vert2][2])#z₂
            
            point_vert3 = Point(verts[face_vert3][0],#x₃
                               verts[face_vert3][1],#y₃
                               verts[face_vert3][2])#z₃
            #Hace un conjunto de puntos
            points = [point_vert1, point_vert2, point_vert3]
            #Saca el plano
            plane = Plane(point_vert1, point_vert2, point_vert3)
                
            #Estas dos cosas son lo mismo
            #Saca el Tensor (Mirar apunte de que es un Tensor) (Vector)
            #Que en verdad es una normal porque lo hace con cálculos 2D (Lo dice mi profe)
            """normals.append({face : basisMatrix}); """
            print("Movida")
            print(point_vert1)
            newTensor = plane.T.array
            print("plano")
            print(plane)
            print("newTensor")
            print(newTensor)
            print(type(newTensor[3]))
            flag = False;
            for face in grouped_faces:
                if(np.allclose(face[0], newTensor)):
                    face.append(points)
                    flag = True
                    break

            if(not flag):
                grouped_faces.append([newTensor, points])
        
        #for face in grouped_faces:
           # polys = face.polygons
           # area = face.totalArea
        return grouped_faces