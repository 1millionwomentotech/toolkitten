# 1 Million Women To Tech 

## Week 10 Virtual reality

## Day 2

#### Create some interaction scripts.
**Optional** : Setup your text editor to monodevelop. 
Most of unity documentation and community support use C#
<br /> 
View aware pointer : Raycast needs a collider component on the object to work
* Lets create the script from the objects Inspector
```csharp
if (Physics.Raycast (Camera.main.transform.position, Camera.main.transform.forward, out objectOnView, max_Distance)) { //we perform a raycast every frame
			pointer.GetComponent<Renderer> ().material.color = Color.magenta;
		} else {
			pointer.GetComponent<Renderer> ().material.color = Color.white;
		}
```
All game objects have components inside them.
Components also have properties that we can easily access. A good guide to each component is the the Unity documentation.


**Here is the Unity Scripting documentation** : https://docs.unity3d.com/ScriptReference/


**Advanced** - Implement the scripts in javascript :(Maybe)https://unity3d.com/es/learn/tutorials/topics/scripting/c-vs-js-syntax


### Comunication between objects
#### Simple kinematics
Now lets make our objects spinn 
```csharp
   // To translate the object in in the y / green axis
   objectOnView.transform.Translate(Vector3.up * Time.deltaTime , Space.World);
   // We can also rotate objects
   objectOnView.transform.Rotate( Vector3.up * Time.deltaTime * 30);
```

#### Simple Dinamics
Lets put some gravity on our app.. first we need a floor :P. Otherwise our objects would fall forever <br />
* Lets add a Quad object
* Lets add rigidBodies to our models - disable use gravity
* Lets create a new script this time from the Project explorer



#### Object communication *SendMessage*
Now lets pass some orders to our objects
 * First - lets pass the message to just one object
    ```csharp
   objectOnView.collider.gameObject.SendMessage("MyOwnFunction");
    ```
 * Now lets reuse this Script for several objects - Unity scripts are reusable as long as the code inside them can be  the same for all the cases! :D - Instances of a class 
 

## Homework

* We can also implement cinematics examples on the Objects, and customize it so that each one would have a different bevhaviour. 


#### Deploy your app inside the editor


### The Monobehaviour class
* Start()
* Awake()
* Update()
* LateUpdate()
* FixedUpdate()

Unity execution Order of events : https://docs.unity3d.com/Manual/ExecutionOrder.html <br /> 
Lets test this with Logs - Unity console

### If we have time - some debugging tools

### Scripts
* Names
* What happens if I change the name of my script (outside or insed the code)?
* Monobehaviour vs classes





