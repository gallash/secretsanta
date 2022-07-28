// Main JavaScript for SantApp, created by Phillip Gallas
// This script works in tandem with the Django backend

// console.log("Hello World");

$( document ).ready(function(){
	$('#room-joining-div').on('click', openRoomJoining);
	$('#room-creation-div').on('click', openEventCreation);
});


function openEventCreation(){
	// What should I do now?
	return window.location.href = "event-creation/";
}

function openRoomJoining(){
	console.log("Still under construction");
	return window.location.href = "event-dashboard";
}