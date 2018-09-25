using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IamMoving : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	public  void DoSomething(){
		//this.gameObject.transform.Rotate (Vector3.up* Time.deltaTime*20, Space.Self);
		//this.gameObject.transform.Translate(Vector3.forward* Time.deltaTime*20, Space.Self);
		this.gameObject.GetComponent<Rigidbody>().useGravity = true;


	}


}
