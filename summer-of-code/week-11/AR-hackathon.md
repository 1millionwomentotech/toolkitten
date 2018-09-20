# 1 Million Women To Tech 

## Summer of Code

### Week 11 Hackaton Challenge: 1mwtt AR log in / access to class material.

Create an Augmented Reality experience for handheld devices (smartphone or tablet), hosted inside a mobile app. 
The app must be composed of 3 scenes linked betwen each other and the user must be able to return to the "main" screen at any time.

* First screen : The user will insert her username / alias 
* Second screen : The user will show her encripted ID card (AR marker) to the camera. The app will then search for this marker on the Vuforia *cloud targets* database, read the metadata attached to it and compare it with the string given by the user on the first scene. If both strings are equal, it will display some information included in the metadata. 
* Third scene : This will only be triggered if the user showed a valid ID + user combination, The content of this windows is free It can be from a simple string message, to a video being played or an animation (You have literaly a blank canvas in here). 

### Creating the targets : They must be inside a cloud database.

* The matadata metadata attached to the target must be a *.txt* file including the string with each target username and another property minimum.
* Try to always get a 5 stars assessment of your target inside the Vuforia Target manager.

### **Hint**: First screen 

* Making a variable static in a script that is instatiated in different scenes will help you pass values between scenes ;)


### **Hint**: Second screen 

* Be patient, cloud recognition speed depends on your internet speed, it can take up to 5-6 seconds for the camera to recognize your target
*  Read all the metadata and then apply some string processing to tokenize your properties if you need to.
	* Some usefull processing string tokenizer techniques in c# are here: https://docs.microsoft.com/en-us/dotnet/csharp/how-to/parse-strings-using-split 

### Ideas for the third screen

* Redirect the user to the 1mwtt Website /Onboarding webinar video /member portal : https://docs.unity3d.com/ScriptReference/Application.OpenURL.html
* 


**Hint** : Remember that you only have 1000 cloud recognitions per month with the Vuforia Developer Licence. Try to leave a couple for us to test your app ;)


#### Bonuses for :
* Include a 3D model in the target with idle animation
* Animate the 3D model depending of it the user log in succeded or not.
* Attach Asset bundles 
* Creative UI elements. 


### Useful documentation links :

* Using Vuforia in Unity : https://library.vuforia.com/articles/Training/getting-started-with-vuforia-in-unity.html
* Cloud Recognition in Unity : https://library.vuforia.com/content/vuforia-library/en/articles/Solution/How-To-Work-with-Cloud-Databases.html
* Implement Cloud recognition in unity : https://library.vuforia.com/content/vuforia-library/en/articles/Solution/How-To-Implement-Cloud-Reco.html#unity
* Change from scenes : https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager.LoadScene.html