import vtk
import math
def create_star(spike_length=2.0, spike_count=5, radius=1.0):
    points = vtk.vtkPoints()
    polyline = vtk.vtkCellArray()
    for i in range(spike_count):
        angle = i * 2 * math.pi / spike_count
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        points.InsertNextPoint(0.0, 0.0, 0.0)

        points.InsertNextPoint(x * spike_length, y * spike_length, 0.0)

        polyline.InsertNextCell(2)
        polyline.InsertCellPoint(i * 2)
        polyline.InsertCellPoint(i * 2 + 1)

    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetLines(polyline)

    tube_filter = vtk.vtkTubeFilter()
    tube_filter.SetInputData(polydata)
    tube_filter.SetRadius(0.1)  
    tube_filter.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(tube_filter.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1.0, 0.84, 0)
    return actor

def create_cube(length=1.0):
    cube = vtk.vtkCubeSource()
    cube.SetXLength(length)
    cube.SetYLength(length)
    cube.SetZLength(length)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cube.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0.2, 0.2, 0.2)  # Gray color
    return actor

def create_cylinder(radius=1.0, height=5.0):
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetRadius(radius)
    cylinder.SetHeight(height)
    cylinder.SetResolution(100)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cylinder.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0.5, 0.5, 0.5)  # Silver color
    return actor

def create_sphere(radius=1.0):
    sphere = vtk.vtkSphereSource()
    sphere.SetRadius(radius)
    sphere.SetPhiResolution(100)
    sphere.SetThetaResolution(100)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphere.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0.0, 0.5, 0.5)
    return actor

def create_pencil():
    
    pencil_body = vtk.vtkCylinderSource()
    pencil_body.SetRadius(0.1)
    pencil_body.SetHeight(6.0)
    pencil_body.SetCenter(0.0, 3.0, 0.0)

    pencil_tip = vtk.vtkConeSource()
    pencil_tip.SetRadius(0.0)  # Tip radius
    pencil_tip.SetHeight(1.0)
    pencil_tip.SetCenter(0.0, 6.0, 0.0)

    eraser = vtk.vtkCylinderSource()
    eraser.SetRadius(0.12)
    eraser.SetHeight(0.5)
    eraser.SetCenter(0.0, 0.5, 0.0)

    pencil_body_mapper = vtk.vtkPolyDataMapper()
    pencil_body_mapper.SetInputConnection(pencil_body.GetOutputPort())
    pencil_body_actor = vtk.vtkActor()
    pencil_body_actor.SetMapper(pencil_body_mapper)
    pencil_body_actor.GetProperty().SetColor(0.8, 0.6, 0.3) 

    pencil_tip_mapper = vtk.vtkPolyDataMapper()
    pencil_tip_mapper.SetInputConnection(pencil_tip.GetOutputPort())
    pencil_tip_actor = vtk.vtkActor()
    pencil_tip_actor.SetMapper(pencil_tip_mapper)
    pencil_tip_actor.GetProperty().SetColor(1.0, 1.0, 0.0)

    eraser_mapper = vtk.vtkPolyDataMapper()
    eraser_mapper.SetInputConnection(eraser.GetOutputPort())
    eraser_actor = vtk.vtkActor()
    eraser_actor.SetMapper(eraser_mapper)
    eraser_actor.GetProperty().SetColor(1.0, 0.0, 0.0)

    return pencil_body_actor, pencil_tip_actor, eraser_actor

def create_phone():
    
    phone_body = vtk.vtkCubeSource()
    phone_body.SetXLength(3.0)
    phone_body.SetYLength(0.2)
    phone_body.SetZLength(6.0)

    screen = vtk.vtkCubeSource()
    screen.SetXLength(2.8)
    screen.SetYLength(0.05)
    screen.SetZLength(5.8)
    screen.SetCenter(0.0, 0.1, 0.0)

    back = vtk.vtkCubeSource()
    back.SetXLength(3.0)
    back.SetYLength(0.2)
    back.SetZLength(6.0)
    back.SetCenter(0.0, -0.1, 0.0)

    body_actor = create_actor(phone_body, (0.2, 0.2, 0.2))
    screen_actor = create_actor(screen, (0.0, 0.0, 0.0))    
    back_actor = create_actor(back, (0.3, 0.3, 0.3))      
    return body_actor, screen_actor, back_actor

def create_chair():
    
    seat = vtk.vtkCubeSource()
    seat.SetXLength(4.0)
    seat.SetYLength(0.5)
    seat.SetZLength(4.0)
    seat.SetCenter(0.0, 2.0, 0.0)

    backrest = vtk.vtkCubeSource()
    backrest.SetXLength(4.0)
    backrest.SetYLength(3.0)
    backrest.SetZLength(0.5)
    backrest.SetCenter(0.0, 4.5, -1.75)

    legs = []
    for x, z in [(-1.75, -1.75), (1.75, -1.75), (-1.75, 1.75), (1.75, 1.75)]:
        leg = vtk.vtkCubeSource()
        leg.SetXLength(0.5)
        leg.SetYLength(2.0)
        leg.SetZLength(0.5)
        leg.SetCenter(x, 1.0, z)
        legs.append(leg)

    seat_mapper = vtk.vtkPolyDataMapper()
    seat_mapper.SetInputConnection(seat.GetOutputPort())
    seat_actor = vtk.vtkActor()
    seat_actor.SetMapper(seat_mapper)

    backrest_mapper = vtk.vtkPolyDataMapper()
    backrest_mapper.SetInputConnection(backrest.GetOutputPort())
    backrest_actor = vtk.vtkActor()
    backrest_actor.SetMapper(backrest_mapper)

    leg_actors = []
    for leg in legs:
        leg_mapper = vtk.vtkPolyDataMapper()
        leg_mapper.SetInputConnection(leg.GetOutputPort())
        leg_actor = vtk.vtkActor()
        leg_actor.SetMapper(leg_mapper)
        leg_actors.append(leg_actor)

    return seat_actor, backrest_actor, leg_actors

def create_actor(source, color):
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(color)
    return actor

def setup_renderer(actors):
    
    renderer = vtk.vtkRenderer()
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    for actor in actors:
        renderer.AddActor(actor)

    renderer.SetBackground(1.0, 1.0, 1.0)  
    render_window.Render()
    interactor.Start()

def main():
    print("Choose a shape to display:")
    print("1. Star")
    print("2. Cube")
    print("3. Cylinder")
    print("4. Sphere")
    print("5. Pencil")
    print("6. Phone")
    print("7. Chair")

    choice =input("Enter your choice: ")

    if choice == 'star':
        spike_length = float(input("Enter spike length: "))
        spike_count = int(input("Enter number of spikes: "))
        star_actor = create_star(spike_length, spike_count)
        setup_renderer([star_actor])

    elif choice == 'cube':
        length = float(input("Enter cube length: "))
        cube_actor = create_cube(length)
        setup_renderer([cube_actor])

    elif choice == 'cylinder':
        radius = float(input("Enter cylinder radius: "))
        height = float(input("Enter cylinder height: "))
        cylinder_actor = create_cylinder(radius, height)
        setup_renderer([cylinder_actor])

    elif choice == 'sphere':
        radius = float(input("Enter sphere radius: "))
        sphere_actor = create_sphere(radius)
        setup_renderer([sphere_actor])

    elif choice == 'pencil':
        pencil_actors = create_pencil()
        setup_renderer(pencil_actors)

    elif choice == 'phone':
        phone_actors = create_phone()
        setup_renderer(phone_actors)

    elif choice == 'chair':
        chair_actors = create_chair()
        setup_renderer([chair_actors[0], chair_actors[1]] + chair_actors[2])

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
