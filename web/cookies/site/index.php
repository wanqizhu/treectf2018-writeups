<?php
if(!isset($_COOKIE["loggedIn"])){
	setcookie("loggedIn", "False", time()+3600);
}
?>
<html>
	<head>
		<title>Cookies</title>
	<head>
	<body>
		<?php
			if($_COOKIE["loggedIn"]!="True"){
				echo "User not logged in";
			}else{
				echo "Welcome, User!<br />Flag is: <code>treeCTF{i_FOUND_the_C00KIES}</code>";
			}
		?>
	</body>
</html>
