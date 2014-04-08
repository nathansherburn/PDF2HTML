function getPreview() {
	console.log("hello");
	var sess_id = document.cookie.match(/PHPSESSID=[^;]+/);
	console.log(sess_id[0]);
	console.log(sess_id[0].replace("PHPSESSID=", ""));
	var path =  sess_id[0].replace("PHPSESSID=", "");
	parent.location = 'webversions/' + path + '/page.html';
}

function getDownload() {
	console.log("hello");
	var sess_id = document.cookie.match(/PHPSESSID=[^;]+/);
	console.log(sess_id[0]);
	console.log(sess_id[0].replace("PHPSESSID=", ""));
	var path =  sess_id[0].replace("PHPSESSID=", "");
	parent.location = 'webversions/' + path + '/website.zip';
}