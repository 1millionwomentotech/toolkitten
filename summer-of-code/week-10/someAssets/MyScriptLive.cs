using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MyScriptLive : MonoBehaviour {

	public GameObject pointer;

	private RaycastHit hit;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {

		//The error I had on the live class , was that on the second argument, I had Vector3.forward 

		if (Physics.Raycast (Camera.main.transform.position, Camera.main.transform.forward, out hit)) {
			pointer.GetComponent<Renderer> ().material.color = Color.magenta;
			hit.collider.gameObject.SendMessage ("DoSomething");
			Debug.Log (hit.collider.gameObject.name);
		} else {
			pointer.GetComponent<Renderer> ().material.color = Color.white;
		}
			
	}
}
