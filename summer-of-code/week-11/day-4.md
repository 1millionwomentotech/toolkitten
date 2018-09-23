
# 1 Million Women To Tech 

## Week 11 Augmented reality

### Today we will learn

* How to create an AR app that takes the marker and the objects from a server
* How to create and later download Unity AssetsBundles, wich are a format of unity to pack information of a specific prefabs in a lighter way

## Day 4 Asset bundles in Unity - Create, download and add to target

*First a quick review of how to export unitypackage*

AssetBundles are exported prefabs that can created in one instance of Unity in offline time and loaded in another one at runtime. They have to be prefabs, not individual components.


Go to the projet you want to export assets from, inside the project view select it and assign label a category and object label.


Create the script

CLick on Assets->Build assetBundels 

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
#if UNITY_EDITOR
using UnityEditor;
#endif
public class ExportAssets : MonoBehaviour {
	#if UNITY_EDITOR // you don't need this if the script is inside the "Editor" folder
	[MenuItem("Example/Build Asset Bundles")] // We need to add this to the menu.
	static void BuildABs()
	{
		// Put the bundles in a folder called "ABs" within the Assets folder.
		BuildPipeline.BuildAssetBundles("Assets/AssetsBundles", BuildAssetBundleOptions.None, BuildTarget.Android);
	}
	#endif
}
```
We can access our asset bundles from any server we may access. In our case we can use Github.

Access the link to download the raw files by right click, copy link address (on the Download Button)


Now to download the models and instantiate them 
```csharp
using UnityEngine.Networking;

public class DownloadAsset : MonoBehaviour {


	public string url;
	// Use this for initialization


	IEnumerator Start(){
		var uwr = UnityWebRequest.GetAssetBundle(url); //carefull, this is diferent in each documentation
		// if you are working with older versions try 
		yield return uwr.SendWebRequest();
		// The name inside the LoadAssets command is the one the prefab had when I was created, not the labels
		GameObject g = Instantiate (DownloadHandlerAssetBundle.GetContent (uwr).LoadAsset ("PrefabName"), this.transform.position, this.transform.rotation,this.transform) as GameObject;

		g.transform.localScale = new Vector3 (0.01f, 0.01f, 0.01f); // This is optional, if your models come form tinkerCAD you may want to use this anyways
		g.name = "myName";

	}

```

Notice that not only the 3D mesh got imported, but also material, rigidbodies and colliders.





