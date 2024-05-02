def few_shot_examples():
    few_shot_example = """
### [User message]
Make the CAD design of a pentagon box (open from one face)

### [Answer]
```python
import Part
import math
from FreeCAD import Base
side_length = 30.0  # Length of each side of the pentagon
height = 20.0  # Height of the pentagon box
App.newDocument("PentagonBox")
App.setActiveDocument("PentagonBox")
App.ActiveDocument = App.getDocument("PentagonBox")
Gui.ActiveDocument = Gui.getDocument("PentagonBox")
pentagon_points = []  # List to hold the points of the pentagon
angle = 360 / 5  # Angle between each vertex of the pentagon

# Calculate the points of the pentagon
for i in range(5):
    x = side_length * math.cos(math.radians(i * angle))
    y = side_length * math.sin(math.radians(i * angle))
    pentagon_points.append(Base.Vector(x, y, 0))

# Create the pentagon wire
pentagon_wire = Part.makePolygon(pentagon_points)
pentagon_face = Part.Face(pentagon_wire)
pentagon_solid = pentagon_face.extrude(Base.Vector(0, 0, height))
Part.show(pentagon_solid)
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```

### [User message]
Make a CAD design of a column that is in the shape of a pentagon with side length 30mm and height 20 mm.

### [Answer]
from FreeCAD import Base

side_length = 30.0  # Length of each side of the pentagon
height = 20.0  # Height of the pentagon box

App.newDocument("PentagonBox")
App.setActiveDocument("PentagonBox")
App.ActiveDocument = App.getDocument("PentagonBox")
Gui.ActiveDocument = Gui.getDocument("PentagonBox")

pentagon_points = []  # List to hold the points of the pentagon
angle = 360 / 5  # Angle between each vertex of the pentagon

# Calculate the points of the pentagon
for i in range(5):
    x = side_length * math.cos(math.radians(i * angle))
    y = side_length * math.sin(math.radians(i * angle))
    pentagon_points.append(Base.Vector(x, y, 0))

pentagon_points.append(pentagon_points[0])  # Close the sketch.

# Create the pentagon wire
pentagon_wire = Part.makePolygon(pentagon_points)
pentagon_face = Part.Face(pentagon_wire)

# Extrude the pentagon face to create a solid
pentagon_solid = pentagon_face.extrude(Base.Vector(0, 0, height))

# Show the solid
Part.show(pentagon_solid)
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")


### [User message]
Make the CAD design of a ball-bearing

### [Answer]
```python
import Part
#needed for calculating the positions of the balls
import math
#needed for translation of torus
from FreeCAD import Base
#
#VALUES#
#(radius of shaft/inner radius of inner ring)
R1=15.0
#(outer radius of inner ring)
R2=25.0
#(inner radius of outer ring)
R3=30.0
#(outer radius of outer ring)
R4=40.0
#(thickness of bearing)
TH=15.0
#(number of balls)
NBall=10
#(radius of ball)
RBall=5.0
#(rounding radius for fillets)
RR=1
#first coordinate of center of ball
CBall=((R3-R2)/2)+R2
#second coordinate of center of ball
PBall=TH/2
#
#Create new document
App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
#
#Inner Ring#
B1=Part.makeCylinder(R1,TH)
B2=Part.makeCylinder(R2,TH)
IR=B2.cut(B1)
#get edges and apply fillets
Bedges=IR.Edges
IRF=IR.makeFillet(RR,Bedges)
#create groove and show shape
T1=Part.makeTorus(CBall,RBall)
T1.translate(Base.Vector(0,0,TH/2))
InnerRing=IRF.cut(T1)
Part.show(InnerRing)
#
#Outer Ring#
B3=Part.makeCylinder(R3,TH)
B4=Part.makeCylinder(R4,TH)
OR=B4.cut(B3)
#get edges and apply fillets
Bedges=OR.Edges
ORF=OR.makeFillet(RR,Bedges)
#create groove and show shape
T2=Part.makeTorus(CBall,RBall)
T2.translate(Base.Vector(0,0,TH/2))
OuterRing=ORF.cut(T2)
Part.show(OuterRing)
#
#Balls#
for i in range(NBall):
  Ball=Part.makeSphere(RBall)
  Alpha=(i*2*math.pi)/NBall
  BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),TH/2)
  Ball.translate(BV)
  Part.show(Ball)
#
#Make it pretty#
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```

### [User message]
Make the CAD design of a knob

### [Answer]
On thinking like a designer, the door knob would look like a hollow sphere and also there would be a cut at one place to 
```python
import Part
OuterSphere=Part.makeSphere(4) #make the outer sphere

#make a cylinder and do cut that cylinder from the sphere
Cylinder = Part.makeCylinder(2, 10) 
DoorKnob = OuterSphere.cut(Cylinder)
Part.show(DoorKnob)
```

### [User message]
Make a cad model of a cube of side length 10, with one of its vertex at origin

### [Answer]
```pythonimport Part
import Sketcher

#create a new document
doc = App.newDocument()

#make box with its starting edge at origin
box = Part.makeBox(10, 10, 10)

#show the box
Part.show(box)
```

### [User message]
Make a cad model of a sphere which has a radius of 10 millimeters and it has its center at location (50, 0, 0)

### [Answer]
```python
import Part
import Sketcher

#create a new document
doc = App.newDocument()

#make a plane which has its origin as (50, 0, 0)
placement = App.Placement(App.Vector(50, 0, 0), App.Rotation()) #creates a plane at this location.
Plane = doc.addObject("Part::Plane", "Plane")
Plane.Placement = placement
Plane.Length = 10  # Set the length of the plane as desired

#always make the visibility of the plane generated as False
Plane.ViewObject.Visibility = False

#Sketch on the plane generated and make sphere with its center at the origin of the plane generated previously
plane_placement = Plane.Placement
plane_location = plane_placement.Base
box_at_plane = Part.makeSphere(10, plane_location)
Part.show(box_at_plane)
```

### [User message]
Make a sketch of a circle and then extrude it to make a CAD design of a cylinder. 

### [Answer]
```python
import Part
import Sketcher

#start a new document
doc = App.newDocument()
sketch = doc.addObject("Sketcher::SketchObject", "Sketch")

#make sketch of a circle.
sketch.addGeometry(Part.Circle(App.Vector(0.2, 0, 0), App.Vector(0, 0, 1), 1), False)
doc.recompute()

#convert it into the format of a wire
wire = FreeCAD.ActiveDocument.Sketch.Shape.Wires[0]
face = Part.Face(wire)

#extrude the face (wire)
extr = face.extrude(FreeCAD.Vector(0,0,10))
Part.show(extr)
```
"""
    return few_shot_example

def get_code_prompt(user_query, steps):
    
    few_shot_example = few_shot_examples()
    prompt = f"""
### Instructions ###
You are a Computer Aided Design Engineer with a lot of industrial experience. You are proficient in using the FreeCAD software.
Your task is to write the corresponding python code for generating what the user asked, using the FreeCAD library to generate the CAD model. Make sure to follow the steps given. Do not save the code at the end. 
Use the following functions to make simple solids:
1. makeBox(length,width,height,[pnt,dir]) #Description: Makes a box located at pnt with the dimensions (length,width,height). By default pnt is Vector(0,0,0) and dir is Vector(0,0,1)
2. makeCircle(radius,[pnt,dir,angle1,angle2]) #Description: Makes a circle with a given radius. By default pnt is Vector(0,0,0), dir is Vector(0,0,1), angle1 is 0 and angle2 is 360.
3. makeCone(radius1,radius2,height,[pnt,dir,angle]) #Description: Makes a cone with given radii and height. By default pnt is Vector(0,0,0), dir is Vector(0,0,1) and angle is 360
4. makeCylinder(radius,height,[pnt,dir,angle]) #Description: Makes a cylinder with a given radius and height. By default pnt is Vector(0,0,0),dir is Vector(0,0,1) and angle is 360
5. makeHelix(pitch,height,radius,[angle,lefthand,heightstyle]) #Description: Makes a helix shape with a given pitch, height and radius. Defaults to right-handed cylindrical helix. Non-zero angle parameter produces a conical helix. Lefthand True produces left handed helix. Heightstyle applies only to conical helices. Heightstyle False (default) will cause the height parameter to be interpreted as the length of the side of the underlying frustum. Heightstyle True will cause the height parameter to be interpreted as the vertical height of the helix. Pitch is "metric pitch" (advance/revolution). For conical helix, radius is the minor radius.
6. makeLine((x1,y1,z1),(x2,y2,z2)) #Description: Makes a line of two points
7. makeLoft(shapelist<profiles>,[boolean<solid>,boolean<ruled>]) #Description: Creates a loft shape using the list of profiles. Optionally make result a solid (vs surface/shell) or make result a ruled surface.
8. makePlane(length,width,[pnt,dir]) #Description: Makes a plane. By default pnt is Vector(0,0,0) and dir is Vector(0,0,1)
9. makePolygon(list) #Description: Makes a polygon of a list of Vectors
10. makeRevolution(Curve,[vmin,vmax,angle,pnt,dir]) #Description: Makes a revolved shape by rotating the curve or a portion of it around an axis given by (pnt,dir). By default vmin/vmax are set to bounds of the curve,angle is 360,pnt is Vector(0,0,0) and dir is Vector(0,0,1)
11. makeShell(list) #Description: Creates a shell out of a list of faces. Note: Resulting shell should be manifold. Non-manifold shells are not well supported.
12. makeSolid(Part.Shape) #Description: Creates a solid out of the shells inside a shape.
13. makeSphere(radius,[center_pnt, axis_dir, V_startAngle, V_endAngle, U_angle]) #Description: Makes a sphere (or partial sphere) with a given radius. By default center_pnt is Vector(0,0,0), axis_dir is Vector(0,0,1), V_startAngle is 0, V_endAngle is 90 and U_angle is 360
14. makeTorus(radius1,radius2,[pnt,dir,angle1,angle2,angle]) #Description: Makes a torus with a given radii and angles. By default pnt is Vector(0,0,0),dir is Vector(0,0,1),angle1 is 0,angle2 is 360 and angle is 360
15. makeTube(edge,float) #Description: Creates a tube.

These are a few example codes you can take reference from:
### Examples ###
{few_shot_example}

### [User message]
Steps to follow while writing the code are given below: 
{steps}
Follow these steps and generate a Python code using the FreeCAD library to make a CAD design of a {user_query}

### [Answer]
```python
"""
    return prompt

def get_steps_prompt(user_query):
    steps_prompt = f"""
### Instructions ###
You are a Computer Aided Design Engineer with a lot of industry experience. You are proficient in mechanical engineering concepts and you know the detailed steps to design any object. You have been using FreeCAD software for designing the CAD models.

### Task ###
The user asked to {user_query}. Your task is to write down the steps you would follow to make the make what the user asked. Before writing the steps I want you think about how the 3D model of what the user asked would look like. Write it in an ordered list. First, visualize what the user is asking for. Then try designing the model step by step. You can follow the template in the examples given below.

### Examples ###
### [User message]
What is the step by step approach to make a CAD design of rectangular prism.

### [Answer]
Step 1: Create a new document.
Step 2: Using the Part.makeBox function make a cuboid.
Step 3: Write Part.show to see the part generated.

### [User message]
What is the step by step approach to make a CAD design of a knob

### [Answer]
Step 1: Create a new document
Step 2: Make a 3D model of sphere using makeSphere function of FreeCAD.
Step 3: Make a cylinder and cut extrude the intersection of cylinder and the sphere.
Step 4: Write Part.show to see the part generated.

### [User message]
What is the step-by-step approach to make a CAD design of a chair?

### [Answer]
Step 1: Sketch the basic outline of the chair, including the seat, backrest, and legs.
Step 2: Extrude the sketches to create solid bodies for the seat and backrest.
Step 3: Create additional sketches for details such as armrests and support structures.
Step 4: Extrude or revolve these sketches to add the details to the chair.

### [User message]
What is the step-by-step approach to make a CAD design of a gear?

### [Answer]
Step 1: Create a new document.
Step 2: Sketch the profile of the gear tooth using the involute curve.
Step 3: Create a circular pattern of the tooth profile to form the complete gear.
Step 4: Extrude the profile to the desired thickness to form the gear.
Step 5: Add a shaft hole at the center of the gear if necessary.

### [User message]
What is the step-by-step approach to make a CAD design of a wrench?

###[Answer]
Step 1: Sketch the outline of the wrench, including the handle and jaws.
Step 2: Extrude the sketches to create solid bodies for the handle and jaws.
Step 3: Add details such as knurling or grip patterns to the handle.
Step 4: Create a separate sketch for the opening of the wrench jaws.
Step 5: Extrude or revolve the sketch to create the opening.

### [User message]
What is the step by step approach to make a CAD design of {user_query}.

### [Answer]
    """
    return steps_prompt

def get_error_prompt(generated_code, error):

    error_prompt = f""" You are an intelligent CAD designer who makes CAD designs using FreeCAD library of python. The user will give you the code he executed and the error message he encountered. 
Your task is to find the error in the code and make the required modifications to it. After making the modifications give the entire modified code. You can take reference from the examples given below. 
    
### Examples ###
### [User message]
The code I worked on is:
```python
import Part
cuboid = Part.Box(1,2,3)
Part.show(cuboid)
```
The error I encountered is:
```
16:03:01  Traceback (most recent call last):
File "C:/Subjects/Semester2/NLP/Project/assignment4/pyautogui/xyz.FCMacro", line 2, in <module>
cuboid = Part.Box(1,2,3)
<class 'AttributeError'>: module 'Part' has no attribute 'Box'
```
### [Answer]
```python
import Part
cuboid = Part.makeBox(1,2,3)
Part.show(cuboid)
```

### [User message]
The code I worked on is
```python
import FreeCAD as App
import Part

# Create a new document
doc = App.newDocument("MyRectangle")

# Define dimensions of the rectangle
length = 10  # Length of the rectangle
breadth = 5    # Width of the rectangle

# Create a rectangle sketch
sketch = doc.addObject('Sketcher::SketchObject', 'RectangleSketch')
sketch.addGeometry(Part.Line(App.Vector(0, 0, 0), App.Vector(length, 0, 0)), False)
sketch.addGeometry(Part.Line(App.Vector(length, 0, 0), App.Vector(length, breadth, 0)), False)
sketch.addGeometry(Part.Line(App.Vector(length, breadth, 0), App.Vector(0, breadth, 0)), False)
sketch.addGeometry(Part.Line(App.Vector(0, breadth, 0), App.Vector(0, 0, 0)), False)
Part.show(sketch)

# Close the sketch
sketch.close()

# Create a pad from the sketch
rectangle = doc.addObject("PartDesign::Pad", "Rectangle")
rectangle.Sketch = sketch
rectangle.Length = 10  # Extrusion length

# Display the document
App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```
The error I encountered is
```
Traceback (most recent call last):
  File "/home/abadagab/results/code/query_3_direct_attempt_2.FCMacro", line 13, in <module>
    sketch.addGeometry(Part.Line(App.Vector(0, 0, 0), App.Vector(length, 0, 0)), False)
<class 'TypeError'>: Unsupported geometry type: Part::GeomLine
```

### [Answer]
```python
import Part
import math
from FreeCAD import Base

length = 30.0
breadth = 20.0
height = 20

#Another way of making the sketch of a rectangle is by appending all the points in this manner and making a wire.
App.newDocument("RectangleBox")
App.setActiveDocument("RectangleBox")
App.ActiveDocument = App.getDocument("RectangleBox")
Gui.ActiveDocument = Gui.getDocument("RectangleBox")
rectangle_points = []
rectangle_points.append(Base.Vector(0, 0, 0))
rectangle_points.append(Base.Vector(length, 0, 0))
rectangle_points.append(Base.Vector(length, breadth, 0))
rectangle_points.append(Base.Vector(0, breadth, 0))
rectangle_points.append(Base.Vector(0, 0, 0))

# Create the rectangle wire
rectangle_wire = Part.makePolygon(rectangle_points)
rectangle_face = Part.Face(rectangle_wire)
rectangle_solid = rectangle_face.extrude(Base.Vector(0, 0, height))
Part.show(rectangle_solid)
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```

### [User message]
The code I worked on is
```python
```
The error I encountered is
```
Traceback (most recent call last):
  File "/home/abadagab/results/code/query_0_direct_attempt_1.FCMacro", line 25, in <module>
    rectangle_solid = Part.extrude(rectangle_face, Base.Vector(0, 0, height))
<class 'AttributeError'>: module 'Part' has no attribute 'extrude'
```

### [Answer]
```python
import Part
import math
from FreeCAD import Base

length = 30.0
breadth = 20.0
height = 20

#Another way of making the sketch of a rectangle is by appending all the points in this manner and making a wire.
App.newDocument("RectangleBox")
App.setActiveDocument("RectangleBox")
App.ActiveDocument = App.getDocument("RectangleBox")
Gui.ActiveDocument = Gui.getDocument("RectangleBox")
rectangle_points = []
rectangle_points.append(Base.Vector(0, 0, 0))
rectangle_points.append(Base.Vector(length, 0, 0))
rectangle_points.append(Base.Vector(length, breadth, 0))
rectangle_points.append(Base.Vector(0, breadth, 0))
rectangle_points.append(Base.Vector(0, 0, 0))

# Create the rectangle wire
rectangle_wire = Part.makePolygon(rectangle_points)
rectangle_face = Part.Face(rectangle_wire)
rectangle_solid = rectangle_face.extrude(Base.Vector(0, 0, height)) #This is how the sketch should be extruded

### [User message]
The code I worked on is:
``` python
{
    generated_code
}
```
The error I encountered is
```
{error}
```

### [Answer]
```python
    """
    return error_prompt

def get_feedback_reason_prompt(feedback, user_query, code):
    few_shot_examples_call = few_shot_examples()
    prompt = f"""You are an intelligent CAD designer who makes CAD designs using FreeCAD library of python. The user will give you a code he executed and the information about what design was generated on executing the code and what he wanted to generate.
Your task is to take into consideration what the user wants and modify the code given below. After making the modifications give the entire modified code.

You can use the following functions to make simple solids:
1. makeBox(length,width,height,[pnt,dir]) #Description: Makes a box located at pnt with the dimensions (length,width,height). By default pnt is Vector(0,0,0) and dir is Vector(0,0,1)
2. makeCircle(radius,[pnt,dir,angle1,angle2]) #Description: Makes a circle with a given radius. By default pnt is Vector(0,0,0), dir is Vector(0,0,1), angle1 is 0 and angle2 is 360.
3. makeCone(radius1,radius2,height,[pnt,dir,angle]) #Description: Makes a cone with given radii and height. By default pnt is Vector(0,0,0), dir is Vector(0,0,1) and angle is 360
4. makeCylinder(radius,height,[pnt,dir,angle]) #Description: Makes a cylinder with a given radius and height. By default pnt is Vector(0,0,0),dir is Vector(0,0,1) and angle is 360
5. makeHelix(pitch,height,radius,[angle,lefthand,heightstyle]) #Description: Makes a helix shape with a given pitch, height and radius. Defaults to right-handed cylindrical helix. Non-zero angle parameter produces a conical helix. Lefthand True produces left handed helix. Heightstyle applies only to conical helices. Heightstyle False (default) will cause the height parameter to be interpreted as the length of the side of the underlying frustum. Heightstyle True will cause the height parameter to be interpreted as the vertical height of the helix. Pitch is "metric pitch" (advance/revolution). For conical helix, radius is the minor radius.
6. makeLine((x1,y1,z1),(x2,y2,z2)) #Description: Makes a line of two points
7. makeLoft(shapelist<profiles>,[boolean<solid>,boolean<ruled>]) #Description: Creates a loft shape using the list of profiles. Optionally make result a solid (vs surface/shell) or make result a ruled surface.
8. makePlane(length,width,[pnt,dir]) #Description: Makes a plane. By default pnt is Vector(0,0,0) and dir is Vector(0,0,1)
9. makePolygon(list) #Description: Makes a polygon of a list of Vectors
10. makeRevolution(Curve,[vmin,vmax,angle,pnt,dir]) #Description: Makes a revolved shape by rotating the curve or a portion of it around an axis given by (pnt,dir). By default vmin/vmax are set to bounds of the curve,angle is 360,pnt is Vector(0,0,0) and dir is Vector(0,0,1)
11. makeShell(list) #Description: Creates a shell out of a list of faces. Note: Resulting shell should be manifold. Non-manifold shells are not well supported.
12. makeSolid(Part.Shape) #Description: Creates a solid out of the shells inside a shape.
13. makeSphere(radius,[center_pnt, axis_dir, V_startAngle, V_endAngle, U_angle]) #Description: Makes a sphere (or partial sphere) with a given radius. By default center_pnt is Vector(0,0,0), axis_dir is Vector(0,0,1), V_startAngle is 0, V_endAngle is 90 and U_angle is 360
14. makeTorus(radius1,radius2,[pnt,dir,angle1,angle2,angle]) #Description: Makes a torus with a given radii and angles. By default pnt is Vector(0,0,0),dir is Vector(0,0,1),angle1 is 0,angle2 is 360 and angle is 360
15. makeTube(edge,float) #Description: Creates a tube.

Some examples of FreeCAD codes are shown below. You are not restricted to these codes. Use them solely as a reference.
### Code examples ###
{few_shot_examples_call}

An example of refinement is shown below.

### Examples ###
### [User message]
I worked on a code with the aim of generating a 3D CAD model of a Cube of side length 2 millimeters. The code I have written is:
```python
import Part
cube = Part.makeBox(1,2,3)
Part.show(cube)
```
On executing this code the CAD model generated resembles the CAD model of a cuboid, whereas I wanted the CAD model of a cube with side length 2 millimeters. Identify the difference between both of them and then modify the code to generate what I actually want.

### [Answer]
```python
import Part
cube = Part.makeBox(2,2,2)
Part.show(cube)
```
### [User message]
I worked on a code with the aim of generating a 3D CAD model of a {user_query}. The code I have written is:
```python
{code}
```
On executing this code the CAD model generated resembles {feedback}, whereas I wanted the CAD model of a {user_query}. Identify the difference between both of them and then modify the code to generate what I actually want. 

### [Answer]
```python
    """

    return prompt

def get_vqa_prompt(user_query):
    prompt = f"""
### Instruction ###
Your task is to tell what the user has been designing. Strictly follow the examples given below. 

### Examples ###
### [User message]
A cylinder of radius 20 millimeters and height 30 millimeters
### [Answer]
A cylinder

### [User message]
A rectangle with 10 millimeters as the length of shorter side and 20 millimeters as the length of longer side.
### [Answer]
A rectangle

### [User message]
{user_query}
### [Answer]
"""

    return prompt
