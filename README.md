# VRED-realtimeSceneInspector
## Use this script to enable an Autofocus with GPU Raytracing

Execute the cameraAutoFocus.py in your VRED Scene.
Turn on GPU Raytracing. Navigate Around. The focus point is always the Center of your scene.

Note: Glass Materials will be ignored. While centering on Glass Materials, the performance is a bit lower.
Switch Materials and their children are taken into account.
The seeThrough value will be taken into account. You can adjust threshold to define, where to set the focus.
The transparency of Mulitplass Materials, LayeredMaterials, XRay, X-Rite etc will be ignored.

### VRED-GPUAutoFocus:
GPU Realtime Raytracing Autofocus
![](cameraAutoFocus.gif)
