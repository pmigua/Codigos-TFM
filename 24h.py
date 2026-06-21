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
    ViewSize=[1335, 705],
    CenterOfRotation=[-20.0, 0.0, 0.0],
    CameraPosition=[24.064122004495086, 57.67705646037241, -0.8674911423907098],
    CameraFocalPoint=[-14.93305709145223, -3.2446565253906483, -0.7722447837175836],
    CameraViewUp=[0.003943836106389299, -0.0009611172460781134, 0.9999917611712636],
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
layout1.SetSize(1335, 705)

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
t01_field_timeseries_XMLpvd = PVDReader(registrationName='T01_field_timeseries_XML.pvd', FileName='C:\\Users\\pmigu\\Desktop\\T01_Time2\\T01_timeseries\\T01_field_timeseries_XML.pvd')
t01_field_timeseries_XMLpvd.PointArrays = ['B_total']

# create a new 'PVD Reader'
t01_SM_seeds_timeseries_XMLpvd = PVDReader(registrationName='T01_SM_seeds_timeseries_XML.pvd', FileName='C:\\Users\\pmigu\\Desktop\\T01_Time2\\T01_timeseries\\T01_SM_seeds_timeseries_XML.pvd')
t01_SM_seeds_timeseries_XMLpvd.PointArrays = ['hemisphere']

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSource1 = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource1', Input=t01_field_timeseries_XMLpvd,
    SeedSource=t01_SM_seeds_timeseries_XMLpvd)
streamTracerWithCustomSource1.Set(
    Vectors=['POINTS', 'B_total'],
    MaximumStreamlineLength=60.0,
)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from t01_field_timeseries_XMLpvd
t01_field_timeseries_XMLpvdDisplay = Show(t01_field_timeseries_XMLpvd, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
t01_field_timeseries_XMLpvdDisplay.Set(
    Representation='Outline',
    ColorArrayName=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
t01_field_timeseries_XMLpvdDisplay.ScaleTransferFunction.Points = [-18768.130859375, 0.0, 0.5, 0.0, 17801.884765625, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
t01_field_timeseries_XMLpvdDisplay.OpacityTransferFunction.Points = [-18768.130859375, 0.0, 0.5, 0.0, 17801.884765625, 1.0, 0.5, 0.0]

# show data from sphere1
sphere1Display = Show(sphere1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
sphere1Display.Set(
    Representation='Surface',
    ColorArrayName=[None, ''],
    SelectNormalArray='Normals',
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
sphere1Display.ScaleTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
sphere1Display.OpacityTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# show data from streamTracerWithCustomSource1
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

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
streamTracerWithCustomSource1Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'B_total'],
    LookupTable=b_totalLUT,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
streamTracerWithCustomSource1Display.ScaleTransferFunction.Points = [-65150.58169882715, 0.0, 0.5, 0.0, 56937.043389142615, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
streamTracerWithCustomSource1Display.OpacityTransferFunction.Points = [-65150.58169882715, 0.0, 0.5, 0.0, 56937.043389142615, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for b_totalLUT in view renderView1
b_totalLUTColorBar = GetScalarBar(b_totalLUT, renderView1)
b_totalLUTColorBar.Set(
    Title='B_total',
    ComponentTitle='Magnitude',
)

# set color bar visibility
b_totalLUTColorBar.Visibility = 1

# show color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

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
    EndTime=23.0,
    PlayMode='Snap To TimeSteps',
)

# ----------------------------------------------------------------
# restore active source
SetActiveSource(streamTracerWithCustomSource1)
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