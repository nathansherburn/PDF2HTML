<?php
	$path = "webversions/";
	$path = $path.basename($_FILES['userfile']['name']);

	if(move_uploaded_file($_FILES['userfile']['tmp_name'], $path)) {
		echo "Successfully uploaded: ".basename($_FILES['userfile']['name'])."<br/>";
		echo "Your conversion has begun...<br/>";
		exec("sudo /usr/local/bin/wrapper.sh");
		echo "Your conversion is complete!<br/>";
		echo "Please visit: <a href='/webversions'>webversions</a>";
	} else {
		echo "Error when uploading file.<br/>";
	}
	header( 'Location: done.html' ) ;
?>
