
# 1 Million Women To Tech 

## Week 11 Augmented reality

## Day 4 Asset bundles in Unity - Create, download and add to target

AssetBundles are exported prefabs that can created in one instance of unity in offline time and loaded in another one at runtime. They can include 3D models, materials, scripts, etc


Go to the proget you want to export assets from,  inside the project view select it and assign label a category and object label.


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
	#if UNITY_EDITOR // dont need this if the script is inside the "Editor" folder
	[MenuItem("Example/Build Asset Bundles")] // We need to add this to the menu.
	static void BuildABs()
	{
		// Put the bundles in a folder called "ABs" within the Assets folder.
		BuildPipeline.BuildAssetBundles("Assets/AssetsBundles", BuildAssetBundleOptions.None, BuildTarget.Android);
	}
	#endif
}
```
We can access our asset bundles from any server we may found. In our case we can use github.

Access the link to download the raw files by right click, copy link adress (on the Download Button)









