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
    ViewSize=[1470, 705],
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
layout1.SetSize(1470, 705)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVD Reader'
t01_field_timeseries_XMLpvd = PVDReader(registrationName='T01_field_timeseries_XML.pvd', FileName='C:\\Users\\pmigu\\Desktop\\T01_Time2\\T01_timeseries\\T01_field_timeseries_XML.pvd')
t01_field_timeseries_XMLpvd.PointArrays = ['B_total']

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=t01_field_timeseries_XMLpvd)
calculator1.Function = 'B_total_X*iHat+B_total_Z*kHat'

# create a new 'PVD Reader'
t01_SM_seeds_timeseries_XMLpvd = PVDReader(registrationName='T01_SM_seeds_timeseries_XML.pvd', FileName='C:\\Users\\pmigu\\Desktop\\T01_Time2\\T01_timeseries\\T01_SM_seeds_timeseries_XML.pvd')
t01_SM_seeds_timeseries_XMLpvd.PointArrays = ['hemisphere']

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSourceXZ = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource X-Z', Input=calculator1,
    SeedSource=t01_SM_seeds_timeseries_XMLpvd)
streamTracerWithCustomSourceXZ.Set(
    Vectors=['POINTS', 'Result'],
    MaximumStreamlineLength=60.0,
)

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSource3D = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource 3D', Input=t01_field_timeseries_XMLpvd,
    SeedSource=t01_SM_seeds_timeseries_XMLpvd)
streamTracerWithCustomSource3D.Set(
    Vectors=['POINTS', ''],
    MaximumStreamlineLength=60.0,
)

# create a new 'Sphere'
sphere1 = Sphere(registrationName='Sphere1')
sphere1.Radius = 1.0

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
        0.24347912696950247, 0.0564, 0.0564, 0.47,
        2.0286674995773923, 0.243, 0.46035, 0.81,
        9.730628563418366, 0.356814, 0.745025, 0.954368,
        50.726145238024515, 0.6882, 0.93, 0.91791,
        117.33357215958856, 0.899496, 0.944646, 0.768657,
        349.00853594059, 0.957108, 0.833819, 0.508916,
        1498.1615163834904, 0.927521, 0.621439, 0.315357,
        8606.589884258297, 0.8, 0.352, 0.16,
        56543.52111034892, 0.59, 0.0767, 0.119475,
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
streamTracerWithCustomSource3DDisplay.ScaleTransferFunction.Points = [-65150.58169882715, 0.0, 0.5, 0.0, 56937.043389142615, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
streamTracerWithCustomSource3DDisplay.OpacityTransferFunction.Points = [-65150.58169882715, 0.0, 0.5, 0.0, 56937.043389142615, 1.0, 0.5, 0.0]

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Set(
    Representation='Outline',
    ColorArrayName=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-18768.130859375, 0.0, 0.5, 0.0, 17801.884765625, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-18768.130859375, 0.0, 0.5, 0.0, 17801.884765625, 1.0, 0.5, 0.0]

# show data from streamTracerWithCustomSourceXZ
streamTracerWithCustomSourceXZDisplay = Show(streamTracerWithCustomSourceXZ, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')
resultLUT.Set(
    RGBPoints=[
        # scalar, red, green, blue
        0.4502247245115051, 0.0564, 0.0564, 0.47,
        3.3533800053869025, 0.243, 0.46035, 0.81,
        14.804727336132778, 0.356814, 0.745025, 0.954368,
        70.72395721787223, 0.6882, 0.93, 0.91791,
        156.49340022754802, 0.899496, 0.944646, 0.768657,
        439.41241755289633, 0.957108, 0.833819, 0.508916,
        1746.3531914384641, 0.927521, 0.621439, 0.315357,
        9146.372235553363, 0.8, 0.352, 0.16,
        54395.46737765561, 0.59, 0.0767, 0.119475,
    ],
    UseLogScale=1,
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
streamTracerWithCustomSourceXZDisplay.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'Result'],
    LookupTable=resultLUT,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
streamTracerWithCustomSourceXZDisplay.ScaleTransferFunction.Points = [-43796.09423121925, 0.0, 0.5, 0.0, 44210.92954761621, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
streamTracerWithCustomSourceXZDisplay.OpacityTransferFunction.Points = [-43796.09423121925, 0.0, 0.5, 0.0, 44210.92954761621, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'B_total'
b_totalPWF = GetOpacityTransferFunction('B_total')
b_totalPWF.Set(
    Points=[0.24347912696950244, 0.0, 0.5, 0.0, 56543.52111034893, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')
resultPWF.Set(
    Points=[0.4502247245115051, 0.0, 0.5, 0.0, 54395.46737765562, 1.0, 0.5, 0.0],
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
    EndTime=23.0,
    PlayMode='Snap To TimeSteps',
)

# initialize the animation scene

# ----------------------------------------------------------------
# restore active source
SetActiveSource(streamTracerWithCustomSourceXZ)
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