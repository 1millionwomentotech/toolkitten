# 1 Million Women To Tech 

## Week 10 Virtual reality

## Today we will cover 

* Create and edit VR UI elements in Unity 
* Import 2D images to our project to displaythem as UI elements
* Replace some of the functions in our scripts with other methods available in Google VR libraries
* Executing functions from a button interaction
* Changing the text content on our UI panels through scripting
* If we have time : Also add some 2D images as an UI elements



## Day 3 UI design and interaction - moving our player around the scene

###First


Good news:
* Gravity
* We can import colours form thinkercad

We will create a new gameObject in our scene of the type UI - > Panel, you will notice that when we create any UI element, Unity automatically generates the Canvas and event manager for us.
<br /> 
We'll also need a button element to allow our users some interaction. Create one by right clicking on our list of element in the scene (called the hierarchy) and selecting a nue UI->Button object.

<br /> 
The button component can call any function (as long as they are public) in any Monobehaviour inside any gameobject in the scene. For this example we will create it inside the Button object

## Lets attach some functions to our buttons

We will declare a new public function of any name that will try to change the content in the panel text object. Be aware that in order to access elements /components of the UI type you need to include the relevant library at the beggining of the script

```csharp
* using UnityEngine.UI;
```
also, remember to define a public variable of the type Text to easily access its properties 

Finally, on the Button component lets add our new function to the list of excetion under the OnCLic() method. If you can not find your function, check that you declared with a *public* accesor 

## How to interact with UI objects 
From our precious class, you remember we were able to interact with objects as long as they have components attached to them. However, we can not a

For another type of applications, we can trigger the *OnClick* method by basically just clicking on the button, or pressing some button in a controller; (*Live Example*) however in our cardboard experience we dont count with those tools we need to find an alternative. The google VR SDK that we imported will be healpful for this. 


## Add required prefab

Inside the G_VR documentations We can find the definition for the class *GvrPointerInputModule* as "*an implemention of Unity's BaseInputModule class, so that Canvas-based (uGUI) UI elements and 3D scene objects can be interacted with in a Gvr Application*".: https://developers.google.com/vr/reference/unity/class/GvrPointerInputModule

Lets follow the documentation and add the required prefabs

* GvrEventSystem : This script overrides the regular event system handler (for example for mouse clicks). This object  includes the *GvrPointerInputModule*script
* GVRPointerPhysicsRaycaster to our main camera
* GvrPointerGraphicRaycaste to the canvas object

## Lets explore the script in unity

In the documentation, if we take a look at the table of the available public functions for this class we see that the *IsPointerOverGameObject* is already casting rays around our scene, so it is not efficient to have several rays being casted.

As in yesterday demo, we can store the result of the reycasthit by accessing *GvrPointerInputModule.CurrentRaycastResult*

## Upgrading our interaction script 

* Create a MyNewInteraction script on the same Manager Object, but disable the past script. Lets paste the content in this new script and star modifying it



* Define a reference to an instance of GVRInputManager, we'll need it to access the *IsPointerOverGameObject* method

* Our logic:
	* The user will place the pointer above and object and we will wait 3 seconds to triiger an specific function (we need a counter variable)
	* Every time the user changes her view from and object we will reset our counter variable to 0
	* To compare between the last object in view and the current one we need to define to GameObjects, focused and oldFocused. 
	* If the object has a *Button* Component attached to it and the timer tell us that 3 seconds have passed, we will invoke the *Onclick* event
	* If the object does not has a *Button* We can still pass some messages to it as before
	* At the end of the secuence we need to refresh the value of old focused 

* Keep the pointer color changing behaviour 
Our script can look like this

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class MyNewInteraction : MonoBehaviour {

	public GvrPointerInputModule GVRInputManager; //Reference the instance of the class inside the new event manager
	public GameObject pointer;
	private GameObject focused;
	private GameObject oldfocused;
	private int timer=0;
	
	// Update is called once per frame
	void Update () {
		if (GVRInputManager.IsPointerOverGameObject (0)) {
			pointer.GetComponent<Renderer> ().material.color = Color.magenta;
			focused = GvrPointerInputModule.CurrentRaycastResult.gameObject; 
			if (focused != oldfocused ) {
				timer=0;
			} else {
				if (timer < 180) {
					timer++;
					// I can not writte return as I am not allowed to change the frequency of Update calls
				}
				if (focused.GetComponent<Button> () != null && timer ==180) {
					focused.GetComponent<Button> ().onClick.Invoke ();
					timer++;
				}
				if (focused.GetComponent<Button> () == null && timer ==180) {
					focused.SendMessage("GravityTrue");
					//Lets excecute some funtions on each object
					timer++;
				}
			}
		} else {
			pointer.GetComponent<Renderer> ().material.color = Color.white;
			focused = null;
			//Debug.Log ("reset to null");
		}
	}

	void LateUpdate(){
		oldfocused = focused;
	}
}

```
## Importing images as textures or sprites 


## A few things to try
* Create a canvas with at least one panel, one image, and two buttons, for each of your 3D objects. The panel should include a name for your model and the authors name/Allias :)  after triggering the first button the text should change to a background story of your model (description, inspiration,etc). The second button should change to say something like "Please enjoy the next art-work"

* Create another button in your canvas that will trigger your model to be affected by gravity, rotate and bounce 2 times , instead of these actions being triggerd by the users view. (Disable previous script or change the raycast one) Include restrictions, please don't let them fall.










