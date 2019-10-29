function gpioWrite(port, digital) {
	var xmlHttp = new XMLHttpRequest();
	var url = "/";
	if(port == 2) {
		if(digital == 1) {
			url = "/ligarLed"
		} else {
			url = "/desligarLed"
		}
	} else if(port == 3) {
	
	}
	xmlHttp.open("GET", url, false);
	xmlHttp.send(null);
	return xmlHttp.responseText;
}

function servoWrite() {
	var xmlHttp = new XMLHttpRequest();
	var position = document.getElementById("range").value;
	var url = "/servo?position=" + position;
	xmlHttp.open("GET", url, false);
	xmlHttp.send();
	return xmlHttp.responseText;
}
function servoWrite2() {
	var xmlHttp = new XMLHttpRequest();
	var position = document.getElementById("range2").value;
	var url = "/servo2?position=" + position;
	xmlHttp.open("GET", url, false);
	xmlHttp.send();
	return xmlHttp.responseText;
}
