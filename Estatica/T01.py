# state file generated using paraview version 6.0.0-RC1
import os
import paraview
paraview.compatibility.major = 6
paraview.compatibility.minor = 0

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.Set(
    ViewSize=[1335, 705],
    CenterOfRotation=[-17.5, 0.0, 0.0],
    CameraPosition=[-17.5, 166.46464263079687, 0.0],
    CameraFocalPoint=[-17.5, 0.0, 0.0],
    CameraViewUp=[0.0, 0.0, 1.0],
    CameraFocalDisk=1.0,
    CameraParallelScale=43.084219849035215,
    OSPRayMaterialLibrary=materialLibrary1,
)

# init the 'Grid Axes 3D Actor' selected for 'AxesGrid'
renderView1.AxesGrid.Visibility = 1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1335, 705)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Disk'
disk1 = Disk(registrationName='Disk1')
disk1.Set(
    InnerRadius=1.05,
    OuterRadius=1.05,
    CircumferentialResolution=180,
)

# create a new 'Sphere'
sphere2 = Sphere(registrationName='Sphere2')
sphere2.Set(
    Radius=1.1,
    ThetaResolution=20,
)

# create a new 'Transform'
transformXZ = Transform(registrationName='Transform X-Z', Input=disk1)

# init the 'Transform' selected for 'Transform'
transformXZ.Transform.Rotate = [90.0, 0.0, 0.0]

# create a new 'Legacy VTK Reader'
test_T01_cartesian_vtk = LegacyVTKReader(registrationName='Test_T01_cartesian.vtk', FileNames=[os.path.join(SCRIPT_DIR, 'Test_T01_cartesian.vtk')])

# create a new 'Slice'
planoXZ = Slice(registrationName='Plano X-Z', Input=test_T01_cartesianvtk)
planoXZ.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
planoXZ.SliceType.Normal = [0.0, 1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
planoXZ.HyperTreeGridSlicer.Origin = [-17.5, 0.0, 0.0]

# create a new 'Calculator'
calculatorxz = Calculator(registrationName='Calculator x-z', Input=planoXZ)
calculatorxz.Function = 'igrf_X*iHat+igrf_Z*kHat'

# create a new 'Contour'
isolneasXZ = Contour(registrationName='Isolíneas X-Z', Input=calculatorxz)
isolneasXZ.Set(
    ContourBy=['POINTS', 'Result_Magnitude'],
    Isosurfaces=[50.0, 100.0, 200.0, 500.0, 1000.0, 2000.0, 5000.0],
)

# create a new 'Calculator'
calculatorXZ = Calculator(registrationName='Calculator X-Z', Input=test_T01_cartesianvtk)
calculatorXZ.Function = 'igrf_X*iHat+igrf_Z*kHat'

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=calculatorXZ,
    SeedType='Line')
streamTracer1.Set(
    Vectors=['POINTS', ''],
    MaximumStreamlineLength=60.0,
)

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Set(
    Point1=[2.0, 0.0, -3.0],
    Point2=[2.0, 0.0, 3.0],
    Resolution=100,
)

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
tube1.Set(
    Scalars=['POINTS', ''],
    Vectors=['POINTS', 'Normals'],
    Radius=0.05,
)

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSourceXZ = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource X-Z', Input=calculatorXZ,
    SeedSource=transformXZ)
streamTracerWithCustomSourceXZ.Set(
    Vectors=['POINTS', 'Result'],
    MaximumStreamlineLength=200.0,
)

# create a new 'Calculator'
calculatorXY = Calculator(registrationName='Calculator X-Y', Input=test_T01_cartesianvtk)
calculatorXY.Function = 'igrf_X*iHat+igrf_Y*jHat'

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSourceXY = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource X-Y', Input=calculatorXY,
    SeedSource=disk1)
streamTracerWithCustomSourceXY.Set(
    Vectors=['POINTS', 'Result'],
    MaximumStreamlineLength=200.0,
)

# create a new 'Sphere'
tierra = Sphere(registrationName='Tierra')
tierra.Radius = 1.0

# create a new 'Transform'
transformYZ = Transform(registrationName='Transform Y-Z', Input=disk1)

# init the 'Transform' selected for 'Transform'
transformYZ.Transform.Rotate = [0.0, 90.0, 0.0]

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSource1 = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource1', Input=test_T01_cartesianvtk,
    SeedSource=sphere2)
streamTracerWithCustomSource1.Set(
    Vectors=['POINTS', 'igrf'],
    MaximumStreamlineLength=1000.0,
)

# create a new 'Contour'
isoplanosXZ = Contour(registrationName='Isoplanos X-Z', Input=test_T01_cartesianvtk)
isoplanosXZ.Set(
    ContourBy=['POINTS', 'igrf_Magnitude'],
    Isosurfaces=[50.0, 100.0, 200.0, 500.0, 1000.0, 2000.0, 5000.0],
)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=isoplanosXZ)

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Normal = [0.0, 1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [-1.6736512184143066, -0.011203765869140625, 0.4592742919921875]

# create a new 'Calculator'
calculatorYZ = Calculator(registrationName='Calculator Y-Z', Input=test_T01_cartesianvtk)
calculatorYZ.Function = 'igrf_Y*jHat+igrf_Z*kHat'

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSourceYZ = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource Y-Z', Input=calculatorYZ,
    SeedSource=transformYZ)
streamTracerWithCustomSourceYZ.Set(
    Vectors=['POINTS', 'Result'],
    MaximumStreamlineLength=200.0,
)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tierra
tierraDisplay = Show(tierra, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tierraDisplay.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', ''],
    SelectNormalArray='Normals',
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
tierraDisplay.ScaleTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
tierraDisplay.OpacityTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# show data from test_T01_cartesianvtk
test_T01_cartesianvtkDisplay = Show(test_T01_cartesianvtk, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
test_T01_cartesianvtkDisplay.Set(
    Representation='Outline',
    ColorArrayName=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
test_T01_cartesianvtkDisplay.ScaleTransferFunction.Points = [-17080.470703125, 0.0, 0.5, 0.0, 15604.7001953125, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
test_T01_cartesianvtkDisplay.OpacityTransferFunction.Points = [-17080.470703125, 0.0, 0.5, 0.0, 15604.7001953125, 1.0, 0.5, 0.0]

# show data from clip1
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'igrf_Magnitude'
igrf_MagnitudeLUT = GetColorTransferFunction('igrf_Magnitude')
igrf_MagnitudeLUT.Set(
    RGBPoints=[
        # scalar, red, green, blue
        49.99999999999999, 0.0564, 0.0564, 0.47,
        110.19299935560011, 0.243, 0.46035, 0.81,
        197.6751169162826, 0.356814, 0.745025, 0.954368,
        365.78677904620656, 0.6882, 0.93, 0.91791,
        499.99999999999994, 0.899496, 0.944646, 0.768657,
        750.6232363462797, 0.957108, 0.833819, 0.508916,
        1291.9687357734026, 0.927521, 0.621439, 0.315357,
        2478.848611705728, 0.8, 0.352, 0.16,
        4999.999999999999, 0.59, 0.0767, 0.119475,
    ],
    UseLogScale=1,
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
clip1Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'igrf_Magnitude'],
    LookupTable=igrf_MagnitudeLUT,
    SelectNormalArray='Normals',
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [50.0, 0.0, 0.5, 0.0, 5000.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [50.0, 0.0, 0.5, 0.0, 5000.0, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for igrf_MagnitudeLUT in view renderView1
igrf_MagnitudeLUTColorBar = GetScalarBar(igrf_MagnitudeLUT, renderView1)
igrf_MagnitudeLUTColorBar.Set(
    WindowLocation='Any Location',
    Position=[0.8840986394557823, 0.33475177304964543],
    Title='igrf_Magnitude',
    ComponentTitle='',
    ScalarBarLength=0.32999999999999996,
)

# set color bar visibility
igrf_MagnitudeLUTColorBar.Visibility = 1

# show color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'igrf_Magnitude'
igrf_MagnitudePWF = GetOpacityTransferFunction('igrf_Magnitude')
igrf_MagnitudePWF.Set(
    Points=[50.0, 0.0, 0.5, 0.0, 5000.0, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation scene

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.Set(
    ViewModules=renderView1,
    Cues=timeAnimationCue1,
    AnimationTime=0.0,
)

# ----------------------------------------------------------------
# restore active source
SetActiveSource(isoplanosXZ)
# ----------------------------------------------------------------


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
