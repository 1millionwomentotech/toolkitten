# 1 Million Women To Tech 

## Week 10 Virtual reality

## Day 3 UI design and interaction - moving our player around the scene

When we create any UI element, Unity automatically generates the Canvas and event manager for us

## Lets attach some functions to our buttons
* using UnityEngine.UI;


## Add required prefab
* GvrEventSystem : This script overrides the regular event system handler (for example for mouse clicks)

## Add Scripts to GameObjects
* GVRPointerPhysicsRaycaster to our main camera
* GvrPointerGraphicRaycaste to the canvas object

## Lets explore the script *GvrPointerInputModule*
This script is already casting rays around our scene, so it is not efficient to have several rays being casted (don't repeat yourself)

## Upgrading our interaction script 

* Create a MyNewInteraction script and 

## Add our new script 
For development to test several scripts we can play with enable and disable option.









