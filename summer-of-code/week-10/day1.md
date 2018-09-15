Open this favourites at the beggining of the class
https://unity3d.com/es/unity/features/multiplatform

# 1 Million Women To Tech 

## Week 10 Virtual reality

## Day 1

Small talk about VR hardware , VR applications
Google Cardboard - One fun example : https://www.youtube.com/watch?v=bDoEYULinMU
Unity can be installed on both Mac and Windows. As well as android Studio 
Unity is a crossplatform engine 

### Prerequisites 
* Enable developer mode on your Android phone; this method is different depending on your smarthphone brand. Sometimes its Taping the Build number seven times(Settings > About > Software information > More > Build number). After the first few taps, you should see the steps counting down until you unlock the developer options. Once activated, you will see a message that reads, “You are now a developer!” .... sometimes you may just find it under Settings > Developer options
* Unity 3D - Try to pick one of the LTS releases : https://unity3d.com/es/unity/qa/lts-releases<br /> **Important** Check the box to allow the installation of Vuforia (Week11) <br /> Also make sure that you check the Android Build support option (or iOS build support if you want to build for iPhone/iPad)
I am using 2017.4.11f1 is the version we used the last time I tested 

#### For andorid deploy :
Follow the Unity documentation :https://docs.unity3d.com/Manual/android-sdksetup.html

* JDK - http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
* Android studio https://developer.android.com/studio/- Emulator is optional if you dont have to much space in your disk 
* Ignore NDK installation
*For iOS deploy:*
You need a Mac to build apps for iOS<br />
https://unity3d.com/es/learn/tutorials/topics/mobile-touch/building-your-unity-game-ios-device-testing
*
* We are going to use an online modeling tool with basic functions :  online  https://www.tinkercad.com

* *optional* - 3D modeling software (Paint 3D in windows 10)  <br />
	* On windows 10 - Paint 3D
	* https://www.sketchup.com/
	* https://www.blender.org/

* Google VR developers - Unity package


### Install Android environment in unity

**Hit** Sometimes the latest version of unity has problems identifying the android SDK during compiling. If you followed all the instructions and nothing seems to work, downgrate to another Unity version.

### Covering the basics
It is important to keep in mind that Unity *units* are in meters, this becames particularly important when developing Augemented and Mixed Reality applications
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

#### Importing assets from your computer

If you have Windows 10, you probably already have Paint3D installed. 
More resources can be found in Unity Assets Store <br />
Here some useful resources:
* https://free3d.com/3d-models/obj
* https://3dexport.com/free-3d-models
* https://www.cgtrader.com/free-3d-models
* My personal favourite https://grabcad.com/

### Import unity packages

### Objects Hierarchy
* Parents
* Children

### Good practices :
 * Organize your Asset folders : You can create folders with any name you like, **Keep in mind** there are some names that are reserved by unity : https://docs.unity3d.com/Manual/ScriptCompileOrderFolders.html
 * A good habit is to start a project always creating the folders *Models*, *Prefabs* , *Scenes* , *Scripts*
 * Keep Scripts at the Scripts folder (or *Editor* for more advanced configurations)

#### If we have time - Customizing materials 
* Standart shader
* Textures : An overview 
 <br /> This requires UVs previusly generated with the model

#### Deploy in emulator 


#### Summary
We created our first VR app for google CardBoard !! :D :D Congratulations
### Homework
* Setting up all the tools can be a lot of work, sometimes unexpected issues can come across: <br />
 Install all the Tools . Get a simple app running on your device or emulator
* Create design in tinkerCAD and share the link
* Explore resources in the asset store

