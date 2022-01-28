import Controlador as cont

cont.loadFile('C:/Users/Sabiin/Downloads/Proyecto1_Normal.ifc')
cont.showSites()
cont.showBuildings()
cont.showStoreys()
print(cont.HowMuchOfAnObjectHasOtherObject("IfcDoor",cont.Storeys()[0][1]))
cont.WhereIsCotainedMyObject(cont.GetListBuildingElementsByType("IfcDoor")[0])
print(cont.CalculateSurfaceOfAllWalls())
cont.showProgram()
cont.showVersionIFC()