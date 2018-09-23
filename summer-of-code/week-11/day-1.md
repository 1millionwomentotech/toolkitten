
# 1 Million Women To Tech 

## Week 11 Augmented reality

## Day 1 - Image and cilinder targets

Today we'll learn:

* How to work inside the Vuforia developers portal
* How to create a marker that will work with Vuforia AR
* How to create our first AR app in Unity using image targets (and if we have time cilindrical targets)



### Introdution

We are going to use Vuforia -  Wiki definition *It is a machine vision engine that use cognize and track planar images (Image Targets) and simple 3D objects, such as boxes, in real time. This image registration capability enables developers to position and orient virtual objects, such as 3D models and other media, in relation to real world images when they are viewed through the camera of a mobile device*


### Get ready
We'll continue working with Unity3D, be sure you have your developer tools properly configured for Andrioid/iOS build.
* Get your developer account at https://developer.vuforia.com/vui/auth/register
* Create a development licence



### Working with Vuforia

Unlike ARcore or the ARkit, Vuforia doesn't track the device's movement in space. Vuforia uses machine vision to recognize the features distribution in space of user-defined targets.




* A guide to install Vuforia in Unity:
	* If you didnt check Vuforia during your Unity installation, you can re-run the installer and enable the checkbox to select *Vuforia Augmented Reality Support* 
	* Create a new gameObject: Select Vuforia -> AR camera
	* In the player settings, enable Vuforia Augmented reality support 
	* Paste your licence number inside the AR camera settings

* A guide to design AR markers: https://library.vuforia.com/articles/Solution/Optimizing-Target-Detection-and-Tracking-Stability
* Features introduction: https://upcommons.upc.edu/bitstream/handle/2099.1/17769/memoria.pdf

### Generating our markers
 * A good free tool: http://www.brosvision.com/ar-marker-generator/
 * If you want to improve your markers even more. You can open the image file in any editor to play with the colors and contrast until you get something you are happy with.
 * Go to your developer portal and create a target database of the type *Device* 
 * Create a target: You can choose from Image, Cilinder, Multitarget and Object. Lets create an Image and a Cilindrical target.
 * When the target is created we can open it and see the assesment that Vuforia gives to our marker based on the features density and distribution. Always try to work with a 5 stars marker. Be aware that a HUGE amount of features can make our marker untrackable unless it is placed really close to the camera.
 * Remember : Non repetitive patterns
 * Once you are happy with your database, you can download your database as a Unity Package and import it to your scene
 * Be sure to activete your database in the Vuforia configuration

### Some examples of good markers - Sizes and features density



### Vuforia on the scene
 

* The image target that we uploaded was processed by the engine and its features were extracted, now is ready to be imported as a unity package
* The gameobjects that we want to include in our AR experience must be attached as a child of the image target Object so that they can inherit its position and orientation on the screen.



### Extended tracking




### A few things to try

* Create a simple AR app with at least one Image target, one Cilindrical target and one Multitarget object. Attach some 3D content to them so that it is clear that the marker got recognized - Submit the screenshot of the unity play mode or a picture of your phone.
* *Optional*: Try working with Vumarks instead of image targets (you need Adobe illustrator for this)
Official documentation : https://library.vuforia.com/articles/Solution/Working-with-VuMarks.html

#### AR Unity packages - Advanced
* **Hololens Mixed reality toolkit:** https://github.com/Microsoft/MixedRealityToolkit-Unity
* **Magic Leap:** Right now is only available in the US but developers can download the emulator at https://unity3d.com/es/partners/magicleap
* **ARcore:** https://github.com/google-ar/arcore-unity-sdk
* **ARKit:** https://assetstore.unity.com/packages/essentials/tutorial-projects/unity-arkit-plugin-92515