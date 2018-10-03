Open this favourites at the beggining of the class

# 1 Million Women To Tech 

## Week 10 Virtual reality

## Day 1

Today we will cover

* Unity and Andorid environtment setup
* Basis of app development in Unity
* We will create some 3D models and import it to our scene 
* Set up our project with the required packages for a google cardboard development
* We will build our first 360 VR app :D :D














In virtual reality, our aim is to generate a three dimentional computer generated environment. Depending on the hardware capabilties we are able to trick a not only the sight  sense but also touch and hearing. 
Even though its development was highly influenced by the gaming industry, VR applications are not limited to it. Right now some of the top applocations are being develop for Architecture, hospitality, sports, arts, teaching and medicine.

In order to trick the sight sense we need a hardware able to project 2 images for each eye with some sutile differences form each other. 
(https://www.youtube.com/watch?v=bDoEYULinMU)

Today we are going to create our first 360 VR experience for Google cardboard. You will be able to implement this app on both android and iOS devices; however we will only cover the Android depoloyment in this course.

The game engine we are going to use is Unity (https://unity3d.com/unity/features/multiplatform), wich is a multiplatform development tool and will be dealing with all the physics and graphics calculations while we only worry about the content and the interaction :) :).

### Prerequisites 
For this week you will need :


* Unity 3D - Try to pick one of the LTS releases : https://unity3d.com/es/unity/qa/lts-releases<br /> **Important** While installing check the box to allow the installation of Vuforia (Week11) <br /> Also make sure that you check the Android Build support option (or iOS build support if you want to build for iPhone/iPad)
* Google VR developers - Unity package https://developers.google.com/vr/develop/unity/download



#### For andorid deploy :

* Enable developer mode and USB debugging on your Android phone; this method is different depending on your smarthphone brand. Sometimes its taping the Build number seven times(Settings > About > Software information > More > Build number). After the first few taps, you should see the steps counting down until you unlock the developer options. Once activated, you will see a message that reads, “You are now a developer!” .... sometimes you may just find it under Settings > Developer options
Follow the Unity documentation :https://docs.unity3d.com/Manual/android-sdksetup.html

* JDK - http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
* Android studio https://developer.android.com/studio/- Emulator is optional if you dont have to much space in your disk 
* Ignore NDK installation

**Hit** Sometimes the latest version of Andorid SDK has compatibility issues working with Unity. If you followed all the instructions and in during building stage unity seems not to recognize the sdk-tools folder, downgrade to another Unity / Android SDK version.
**I am using 2017.4.11f1 with the Android SDK tools v 26.1.1**

####For iOS deploy:

You need a Mac to build apps for iOS<br />
https://unity3d.com/es/learn/tutorials/topics/mobile-touch/building-your-unity-game-ios-device-testing

### 3D modeling 

* We are going to use an online modeling tool with basic functions :  online  https://www.tinkercad.com

* *optional* - Any 3D modeling software you feel comfortable with (Paint 3D in windows 10)  <br />
	* On windows 10 - Paint 3D
	* https://www.sketchup.com/
	* https://www.blender.org/

Once we have our model done we must exported to some of the Unity supported 3D formats https://docs.unity3d.com/540/Documentation/Manual/HOWTO-importObject.html

### Install Android environment in unity

Once we create a new unity project, we need to link Unity with the directories were you installed the Andorid tools and the JDK.

### Covering the basics

For VR and AR applications sometimes it is important to keep in mind that Unity *units* are in meters, this becames particularly important when developing Augemented and Mixed Reality applications or for VR devices tracked in space such as the HTC Vive

#### Unity layout
* Asset windows
* Hierarchy panel
* Game view
* Scene view

#### Lights and camera
In VR/AR expereinces it is good practice to have ONLY one main Camera.<br />
The two main types are
* Directional lights : Their possition in the scene is not relevant, oly its direction has an effect on the lighting
* Point lights

If you have hardware resources limitations try to limit your ilumination to 3 lights in the scene, as lighting calculations such as shadows and reflections are *expensive* to calculate

#### Importing assets from your computer

More resources can be found in Unity Assets Store <br />
Here some useful resources:
* https://free3d.com/3d-models/obj
* https://3dexport.com/free-3d-models
* https://www.cgtrader.com/free-3d-models
* My personal favourite https://grabcad.com/

### Import unity packages



### Objects Hierarchy
Objects in Unity can be organized in a Hierarchy order level. Children our bounded to parent by transform relationships


### Good practices :
 * Organize your Asset folders : You can create folders with any name you like, **Keep in mind** there are some names that are reserved by unity : https://docs.unity3d.com/Manual/ScriptCompileOrderFolders.html
 * A good habit is to start a project always creating the folders *Models*, *Prefabs* , *Scenes* , *Scripts*
 * Keep Scripts at the Scripts folder (or *Editor* for more advanced configurations)


### Create your first scene 
All the resources you will need for your development are under the GoogleVR folder.

From insde of the prefabs sub folder
* Grvr editoremulator : This is optional but it provide us really usufull tools to test our apps inside of unity before building them.
* Grvr headset : This object contains and script responsable of tracking the device rotation and build the 2 images during the compiling stage

### Add the models to your scene
* Change the values of the trasform component and see the changes (scale, rotation , position)
* Create a material and assign it to your model

#### Deploy in emulator 


### Build the app

Under the the player settings pick and app name and company, then add enable Virtual reality support and add Google cardboard to the list of SDKs

* From Q&A : please make sure your bild system option is set to *Internal*

#### If we have time - Customizing materials 
* Standart shader
* Textures : An overview 
 <br /> This requires UVs previusly generated with the model
* **Logo colours** : 
	* Hair : R241 G55 B155
	* Hair Border R143 G65 B103

#### Summary
We created our first VR app for google CardBoard !! :D :D Congratulations
### A few things to try
* Install all the Tools . Get a simple app running on your device or emulator
* Create design of 5 figures minimum in tinkerCAD, at least 2 of them to be a character with legs and arms. Explore all the available basic shapes and challange your creativity 
* Import the models into your scene and place them around the camera object 
* Explore resources in the asset store 

### Other SDKs to explore

* Oculus SDK: https://developer.oculus.com/downloads/package/oculus-utilities-for-unity-5/
* HTC vive - Steam VR: https://assetstore.unity.com/packages/templates/systems/steamvr-plugin-32647
* Mixed reality toolkit (VR and AR headsets): https://github.com/Microsoft/MixedRealityToolkit-Unity
