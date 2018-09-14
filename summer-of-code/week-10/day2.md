# 1 Million Women To Tech 

## Week 10 Virtual reality

## Day 2

#### Create some interaction scripts.


Most of unity documentation and community support use C#
<br /> 
View aware spinning

**Here is the Unity Scripting documentation** : https://docs.unity3d.com/ScriptReference/


**Advanced** - Implement the scripts in javascript :(Maybe)https://unity3d.com/es/learn/tutorials/topics/scripting/c-vs-js-syntax


### Comunication between objects
#### Simple kinematics
Now lets make our objects spinn 
#### Simple Dinamics
Lets put some gravity on our app
#### Object communication *SendMessage*
Now lets pass some orders to our objects
 * First - lets pass the message to just one object
 * Now lets reuse this Script for several objects - Unity scripts are reusable as long as the code inside them can be  the same for all the cases! :D - Instances of a class 
 * Now lets pass some arguments to other objects script
   ```csharp
   objectOnView.collider.gameObject.SendMessage("MyOwnFunction");
    ```
* We can also implement the dinamics a cinematics examples on the Objects, and customize it so that each one would have a different bevhaviour. 


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






