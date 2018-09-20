# 1 Million Women To Tech 

## Week 10 Virtual reality

## Day 4  - Animations

## Today we will cover 

* Create prefabs that we can reuse as many times as needed in our scene
* Create path-defined animations to move our camara around the scene, and animate our models. **Please start thinking what kind of movement would you like us to do with your model** 
* Create and understand an animator component to create secuences of animations and  control when do we trigger each animation.
* Learn how to export our project as a single file so that we can share it (for homeworks submissions)





 The maximum distance for the raycast is under the GvrReticlePointer, if you objects are not being seen by the raycast just change this value or place them closer. 

 In our case, we are going to place some models far away from the camera so that their events cannot be triggered unless the user is closer to them

### Lets create our first animation

* Open the animation Window under Wundow->Animation.
* Now Select the object we want to animate, it will ask us to create an animator and animator clip

This window is divided en 2, at the right side there is a timeline divided in seconds to help as build our animations. On the left side we will se a list of properties that will be create

* You can see that after saving our scene we not only have a new animation clip inside the Animation window but our Gameobject now has an animator component attached to it. The animator Component is basically the controller for our objects, it decides when and how  to play each animaton 
* To start animating lets click on the record button (we know that we are animating because our timescale should have a red tint)
* To create a new state for your model clickabove some value on the timescale to move the state mark and play with your model to get a final position, you will notice that unity has create one or some diamonds bellow the timescale, these are called Keyframes and represent a new state of animations. You don't have to animate frame by frame, unity will calculate the states inbetween keyframes.

* We can change in the transform component
	* Position
	* Rotation
	* Scale

* Notice also that you can move several objects in one animation as long as the clip is applied to the parent object
* Leave record mode, and press play to see your animation.

### Understand the animator controller

Our animation appears to be playing inside an infinite loop. Open the controller object that is inside our recently auto-generated Animator component. (Double click)

* A new window called Animator is opened. and inside there is the flowchart that rules oall the states of our model's animation.
* Single click on our recently created animation and change the speed if your need to. Now double click on it and disable the Loop time checkbox to disable the loop replay
* Go to play mode to see the changes

### Trigger you animation

The transitions between states or clips are usefull and give us control over our objects. 

* Under the Parameters tap add a new trigger parameter and write a name for it, lets assign this trigger as a condition for the transition before our animation

* As we cannot add conditions to the arrow after the "Entry" state, lets create an empy state between Entry and our recently created animation

```csharp
	public Animator targetAnimator;
 ///.............///
	public void ActivetTrigger(string TriggerName){
		targetAnimator.SetTrigger (TriggerName);
	}

```


## Moving our player around the scene
We cannot move our Main camera ,  '*If the mountain will not come to Muhammad, then Muhammad must go to the mountain*'

* Group all the objects in just one parent called Stage

* Create an animation for the stage to move around it 

* Trigger the animation when the user gazes at the button


### Now lets taste our VR app!!!
:D


## A few things to try

* Create an animation for  each one of your models that will only start when the user gazes at a "next" Button inside the panel that you already created. For the character models, each body-part must have a different movement. :) Be creative and have fun

* Create animations and an animator controller for the camera object and trigger each animation to move around our 3D models musseum and interact with the panels when the Maximum reticle distance is not big enought to reach them as they are far away.


### Where to go from here

* Unity Learn : https://unity3d.com/learn
	* Roll-a-ball tutorial
	* Survival Shooter tutorial 
	* By Topics : Scripting
	* https://unity3d.com/learn/tutorials/s/xr
	* Getting started VR: https://unity3d.com/learn/tutorials/topics/virtual-reality/resources-getting-started-vr?playlist=22946

* Edx : https://www.edx.org/es/course/creating-virtual-reality-vr-apps
* Cursera Mobile VR app development unity https://www.coursera.org/learn/mobile-vr-app-development-unity