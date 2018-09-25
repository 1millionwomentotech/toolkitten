
# 1 Million Women To Tech 

## Week 11 Augmented reality

## Day 2 -   Trigger interaction

Today we will learn:

* How to trigger events when 2 AR-traslated objects overlap
* How to create UI interaction (tap and text input)  for mobile apps 
* How to connect scenes


### Recognizing Tap gestures
The following method will allow you to interact with any gameobject as long as it has a callider set as Trigger.

```csharp
void OnMouseUpAsButton()
	{
		//Do something
		}

```


### Trigger - Trigger interaction setup

When working with 2 or more targets, the sizes are important
A pairing of 2 objects, one has to be the trigger and have a rigidbody inside (Kinematic).

### Trigger states recognition.
Triggers dont involve physics collisions. They just recognize when two objects are overlaping

* You can trigger events in the object that owns the script or on the other collider.
* **OnTriggerEnter** is called when the other Collider enters the trigger.
* **OnTriggerExit** is called when the  other Collider has stopped touching the trigger.
* **OnTriggerStay** is called almost all the frames for every  other Collider  that is touching the trigger. The function is on the physics timer so it won't necessarily run every frame.

When a trigger collision is recognized we can call any function that we want through scripting.

### Changing an Object parent

Every object has a parent we can access to. We see the parent of an object in the hierarchy as it apperears that some objects are inside another objects; we'll say from now: Object A is the parent/ a child of object B. We can access the parent property inside any Monobehaviour funcion:


```csharp
	gameobject.transform.parent

```

### Creating an UI-only screen

* Create a screenspace camera and add a sprite renderer to cover all of the camera view. Even without implementing the AR camera prefab, when using Vuforia, the AR behaviour will be forced in all scenes.
* Play around inserting Buttons, input fields, images etc.




### Navigating through scenes


```csharp
using UnityEngine.SceneManagement;
///:.....................//

public void LoadMyScene(string scenename){
		SceneManager.LoadScene (scenename);
	}
```
To test event *Loadscene manager*, the scenes must be added in the build setting

Official Vuforia Documentation
https://library.vuforia.com/articles/Solution/Smart-Terrain-Workflow-in-Unity.html

### A few things to try

* Create tap interaction with your models (trigger an animation, sound or any other scriptable behaviour)
* Create a second scene with several UI elements and create the transition from one to the other.
* Change the parent from objects that are attached to your target in movement to other markers on your scene.