'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided “as is” with no warranty of any kind and you use the applications at your own risk.

Scripted by Simon Nagel, supported by Rutvik Bhatt
'''
'''
Just paste the Scene in the Script Editor of VRED and press run.
Hover over Geometries to see the geometries name, parents and materials in the viewpoint.
Feel free to adjust annotation properties in the Annotation Module.
'''


import PySide2.QtGui
QColor = PySide2.QtGui.QColor
QVector3D = PySide2.QtGui.QVector3D

timerRealtimeInspector = vrTimer()
timerRealtimeInspector.setActive(0)

annos = vrAnnotationService.getAnnotations()
if len(annos) == 0:  
    anno = createAnnotation("MY New Annotation")
    anno.setText("nodename")

else:
    anno = findAnnotation("MY New Annotation")
    if anno == None:
        anno = createAnnotation("MY New Annotation")
        anno.setText("nodename")
    anno.setText("nodename")
    

parentList = []

def inspect():
    global parentList
    del parentList[:]
    global anno
    mousePos = getMousePosition(-1)

    intersection = getSceneIntersection(-1,mousePos[0],mousePos[1])
    interPos = intersection[1]
    interObj = intersection[0]
    interDir = intersection[2]

    if interObj.isValid(): 
        nodename = interObj.getName()
        parentnode = interObj.getParent()
        parentnodeName = parentnode.getName()
        mat = interObj.getMaterial()
        matname = interObj.getMaterial().getName()
        matType = interObj.getMaterial().getType()
        inpectText = ""
        firstParentName = parentnodeName
        
        while parentnodeName != "Root":
            parentnode =  parentnode.getParent()
            parentnodeName = parentnode.getName()
            parentList.append(parentnodeName)
        
        for i in range(len(parentList)-1,-1,-1):
            inpectText = inpectText +str(parentList[i])+"\n"
            #inpectText.append(str(parentList[i]))
        inpectText = "Nodename: "+"\n"+nodename+"\n\n"+"Parent Nodes: "+"\n"+inpectText

        inpectText = inpectText+firstParentName+ "\n\n"+"Applied Material: "+"\n"+matname
        
        if matType== "SwitchMaterial":
            choice = mat.getChoice()
            choicematname = mat.getMaterialByChoice(choice).getName()
            inpectText = inpectText+ "\n"+choicematname
        
    
        anno.setPosition(QVector3D(interPos.x(),interPos.y(),interPos.z()))
        anno.setText(inpectText)

timerRealtimeInspector.connect(inspect)
timerRealtimeInspector.setActive(true)
