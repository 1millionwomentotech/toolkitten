
# 1 Million Women To Tech 

## Week 11 Augmented reality

## Day 3 - Cloud targets 

Today we will learn:

* More UI elements in unity
* How to create cloud recognition targets and implement them in unity
* How to update the information of a target without changing any information in our app
* How to process the target metadata with a simple c# string tokenizer
* Trigger a function to open urls in the external explorer 

### Create Cloud target databases

Cloud targets are targets that exist on your account database rather than on the device. Right now, everytime you want to update an image target or want to include another target to your database, you would have to download the .unitypackage file and reimport it. Cloud targets allow the users of your app to get your target updates without requiring you to reinstall the app.

Uploading the image target works similar to device databases. However, this time the target manager will allow you to include some motedata on it. This can be a string that we will process later.

### Setting up a cloud target in Unity

* Insert a Cloud Recognition Object and a Cloud image target
* Set up the keys of the database
* Create a script to handle the CloudRecoBehaviour following the documentation
https://library.vuforia.com/content/vuforia-library/en/reference/unity/interfaceVuforia_1_1ICloudRecoEventHandler.html#details

```csharp

	private CloudRecoBehaviour mCloudRecoBehaviour;
	private bool mIsScanning = false;
	private string mTargetMetadata = "";
	public ImageTargetBehaviour ImageTargetTemplate;
	ObjectTracker m_ObjectTracker;

	// Use this for initialization
	void Start () {
		
		// register this event handler at the cloud reco behaviour

		mCloudRecoBehaviour = GetComponent<CloudRecoBehaviour>();


		if (mCloudRecoBehaviour)
		{
			mCloudRecoBehaviour.RegisterEventHandler(this);
		}


		scessfulLoggin.SetActive (false);
		unsucessfulLogin.SetActive (false);
	}

	public void OnInitialized() {
		Debug.Log ("Cloud Reco initialized");
		// get a reference to the Object Tracker, remember it
		m_ObjectTracker = TrackerManager.Instance.GetTracker<ObjectTracker>();
	}
	public void OnInitError(TargetFinder.InitState initError) {
		Debug.Log ("Cloud Reco init error " + initError.ToString());
	}
	public void OnUpdateError(TargetFinder.UpdateState updateError) {
		Debug.Log ("Cloud Reco update error " + updateError.ToString());
	}

	/// <summary>
	///  to keep track of the scanning mode. This action lets you know whether Vuforia is scanning the clou
	/// </summary>
	/// <param name="scanning">If set to <c>true</c> scanning.</param>

	public void OnStateChanged(bool scanning) {
		mIsScanning = scanning;
		if (scanning)
		{
			// clear all known trackables
			m_ObjectTracker.TargetFinder.ClearTrackables(false);
		}
	}



	// Here we handle a cloud target recognition event
	public void OnNewSearchResult(TargetFinder.TargetSearchResult targetSearchResult) {
		// do something with the target metadata
		mTargetMetadata = targetSearchResult.MetaData;
		// stop the target finder (i.e. stop scanning the cloud)
		mCloudRecoBehaviour.CloudRecoEnabled = false;
		// Build augmentation based on target

		tokenized = GetUserFromMetadata (mTargetMetadata);
		Debug.Log("user:" + tokenized[0]);

		if (inputedUsername == tokenized [0]) {
			scessfulLoggin.SetActive (true);
			fullName.text = "Name: " + tokenized [1];
			role.text = "Role: " + tokenized [2];
			membership.text = "Membership: " + tokenized [3];
		} else {
			unsucessfulLogin.SetActive (true);
		}


		//I found it in the cloud, now I am going to tell unity that an image target is in my view

		if (ImageTargetTemplate) {
			// enable the new result with the same ImageTargetBehaviour:
			ObjectTracker tracker = TrackerManager.Instance.GetTracker<ObjectTracker>();
			ImageTargetBehaviour imageTargetBehaviour =
				m_ObjectTracker.TargetFinder.EnableTracking(targetSearchResult, ImageTargetTemplate.gameObject) as ImageTargetBehaviour;
		}
	}

```



### Opening URL elements 




