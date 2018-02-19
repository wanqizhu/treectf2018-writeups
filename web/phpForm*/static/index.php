<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>PHP Form</title>
</head>
<body>
	<?php
		if(isset($_POST["choice"])){
			$CHOICE = $_POST["choice"];
		}
		if(isset($CHOICE) && $CHOICE == "wonderful"){
			include('/home/ubuntu/php/correct.html');
		}else{
	?>
			<h1>Welcome to my website!</h1>
			<p><a href='index.php.source' target="_blank">Source</a></p>
			<form action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="post">
				<select name="choice">
					<option value="yes">Yes</option>
					<option value="no">No</option>
				</select>
				<input type="submit" value="Submit">
			</form>
	<?php
		}
	?>
</body>
</html>
