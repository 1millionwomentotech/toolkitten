

# 1 Million Women To Tech 

## Week 11 Augmented reality

### Vumarks 


using Vuforia;

```csharp


   using Vuforia;
public class DecodeStrings : MonoBehaviour {

	public TextMesh vumarkinfo;
	VuMarkManager myManager;

	// Use this for initialization
	void Start () {
		myManager = TrackerManager.Instance.GetStateManager ().GetVuMarkManager ();
		myManager.RegisterVuMarkDetectedCallback (OnVumarkDetection);
	}
	

	void OnVumarkDetection( VuMarkTarget target){
		Debug.Log( "This vumark says:" + target.InstanceId.StringValue);
		vumarkinfo.text = target.InstanceId.StringValue;
	}
}

```

