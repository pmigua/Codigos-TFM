# state file generated using paraview version 6.0.0-RC1
import paraview
paraview.compatibility.major = 6
paraview.compatibility.minor = 0

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
    ViewSize=[1420, 705],
    CenterOfRotation=[-20.0, 0.0, 0.0],
    CameraPosition=[-20.0, 72.33425303706383, 0.0],
    CameraFocalPoint=[-20.0, 0.0, 0.0],
    CameraViewUp=[0.0, 0.0, 1.0],
    CameraFocalDisk=1.0,
    CameraParallelScale=33.166247903554,
    OSPRayMaterialLibrary=materialLibrary1,
)

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1420, 705)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Sphere'
sphere1 = Sphere(registrationName='Sphere1')
sphere1.Radius = 1.0

# create a new 'PVD Reader'
t01_SM_seeds_timeseries_month_XMLpvd = PVDReader(registrationName='T01_SM_seeds_timeseries_month_XML.pvd', FileName='C:\\Users\\pmigu\\Desktop\\T01_Time2\\T01_timeseries_month\\T01_SM_seeds_timeseries_month_XML.pvd')
t01_SM_seeds_timeseries_month_XMLpvd.PointArrays = ['hemisphere']

# create a new 'PVD Reader'
t01_field_timeseries_month_XMLpvd = PVDReader(registrationName='T01_field_timeseries_month_XML.pvd', FileName='C:\\Users\\pmigu\\Desktop\\T01_Time2\\T01_timeseries_month\\T01_field_timeseries_month_XML.pvd')
t01_field_timeseries_month_XMLpvd.PointArrays = ['B_total']

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=t01_field_timeseries_month_XMLpvd)
calculator1.Function = 'B_total_X*iHat+B_total_Z*kHat'

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSourceXZ = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource X-Z', Input=calculator1,
    SeedSource=t01_SM_seeds_timeseries_month_XMLpvd)
streamTracerWithCustomSourceXZ.Set(
    Vectors=['POINTS', 'Result'],
    MaximumStreamlineLength=60.0,
)

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSource3D = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource 3D', Input=t01_field_timeseries_month_XMLpvd,
    SeedSource=t01_SM_seeds_timeseries_month_XMLpvd)
streamTracerWithCustomSource3D.Set(
    Vectors=['POINTS', 'B_total'],
    MaximumStreamlineLength=60.0,
)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sphere1
sphere1Display = Show(sphere1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
sphere1Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', ''],
    SelectNormalArray='Normals',
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
sphere1Display.ScaleTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
sphere1Display.OpacityTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# show data from streamTracerWithCustomSource3D
streamTracerWithCustomSource3DDisplay = Show(streamTracerWithCustomSource3D, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'B_total'
b_totalLUT = GetColorTransferFunction('B_total')
b_totalLUT.Set(
    RGBPoints=[
        # scalar, red, green, blue
        0.33778585794345295, 0.0564, 0.0564, 0.47,
        2.657926000510715, 0.243, 0.46035, 0.81,
        12.220727282681974, 0.356814, 0.745025, 0.954368,
        60.930719686207766, 0.6882, 0.93, 0.91791,
        137.78392355368607, 0.899496, 0.944646, 0.768657,
        397.95738305687416, 0.957108, 0.833819, 0.508916,
        1642.4200707235348, 0.927521, 0.621439, 0.315357,
        9000.50085277173, 0.8, 0.352, 0.16,
        56202.499729950454, 0.59, 0.0767, 0.119475,
    ],
    UseLogScale=1,
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
streamTracerWithCustomSource3DDisplay.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'B_total'],
    LookupTable=b_totalLUT,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
streamTracerWithCustomSource3DDisplay.ScaleTransferFunction.Points = [-35090.2582400414, 0.0, 0.5, 0.0, 29658.767115054223, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
streamTracerWithCustomSource3DDisplay.OpacityTransferFunction.Points = [-35090.2582400414, 0.0, 0.5, 0.0, 29658.767115054223, 1.0, 0.5, 0.0]

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Set(
    Representation='Outline',
    ColorArrayName=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-18041.0625, 0.0, 0.5, 0.0, 31793.640625, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-18041.0625, 0.0, 0.5, 0.0, 31793.640625, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for b_totalLUT in view renderView1
b_totalLUTColorBar = GetScalarBar(b_totalLUT, renderView1)
b_totalLUTColorBar.Set(
    WindowLocation='Any Location',
    Position=[0.8866104868913857, 0.03120567375886525],
    Title='B_total',
    ComponentTitle='Magnitude',
    ScalarBarLength=0.932836879432624,
)

# set color bar visibility
b_totalLUTColorBar.Visibility = 1

# show color legend
streamTracerWithCustomSource3DDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'B_total'
b_totalPWF = GetOpacityTransferFunction('B_total')
b_totalPWF.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 56202.49972995045, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.Set(
    ViewModules=renderView1,
    Cues=timeAnimationCue1,
    AnimationTime=0.0,
    EndTime=11.0,
    PlayMode='Snap To TimeSteps',
)

# initialize the animation scene

# ----------------------------------------------------------------
# restore active source
SetActiveSource(streamTracerWithCustomSource3D)
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