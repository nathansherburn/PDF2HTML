<?php
	session_start();
	$session_id = session_id();
	echo $session_id;
	echo "<br/><br/>";
	$path = "webversions/".$session_id."/";
	echo $path;
	echo "<br/><br/>";
	chmod ("/var/www/webversions", 0777);
	if (file_exists ( $path )) {
		foreach(glob($path.'*.*') as $file) {
			unlink($file);
		}
		rmdir($path);
	}
	mkdir($path, 0700);
	$path = $path.basename($_FILES['userfile']['name']);
	echo $path;
	echo "<br/><br/>";
	if(move_uploaded_file($_FILES['userfile']['tmp_name'], $path)) {
		echo "Successfully uploaded: ".basename($_FILES['userfile']['name'])."<br/>";
		echo "Your conversion has begun...<br/>";
		exec("sudo /usr/local/bin/wrapper.sh ".$session_id." ".basename($_FILES['userfile']['name']));
		echo "Your conversion is complete!<br/>";
		header( 'Location: done.html' );
	} else {
		echo "Error when uploading file.<br/>";
		header( 'Location: oops.html' );
	}
	chmod ("/var/www/webversions", 0755);
?>
