﻿using UnityEngine;
using System.Collections;

public class PlayerController : MonoBehaviour {

	public float speed;
	void Update()
	{
		//before screen update

	}

	void FixedUpdate()
	{
		//before physics update
		float moveHorizontal = Input.GetAxis ("Horizontal");
		float moveVertical = Input.GetAxis ("Vertical");

		Vector3 movement = new Vector3 (moveHorizontal, 0.0f, moveVertical);

		rigidbody.AddForce (movement * speed * Time.deltaTime);
	}
	void OnTriggerEnter(Collider other) {
		if (other.gameObject.tag == "Pickup") {
			other.gameObject.SetActive(false);
		}
	}
}
