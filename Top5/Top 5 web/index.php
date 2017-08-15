<!DOCTYPE html>
<html lang="en" dir="ltr">

<!--?php

$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT song, COUNT(*) Amount FROM playedsongs GROUP BY song ORDER BY amount DESC LIMIT 5";
$result = $conn->query($sql);

?--> 

<head>
<title>Top 5 Songs</title>
<meta charset="iso-8859-1">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="styles/layout.css" type="text/css" media="all">
<link rel="stylesheet" href="styles/mediaqueries.css" type="text/css" media="all">

<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>

</head>
<body>
<div class="wrapper row1">
  <header id="header" class="clear">
    <div id="hgroup">
      <h1><a href="#">Top 5 Songs</a></h1>
      <h2>From the Musicbox</h2>
    </div>
  </header>
</div>
<div class="wrapper row2">
  <nav id="topnav">
    <ul class="clear">
      <li class="active first"><a href="index.html">Top 5</a></li>
	  <li><a href="#">Portfolio</a></li>
      <li><a href="#">Instructables</a></li>
    </ul>
  </nav>
</div>

<div class="wrapper row3">
  <div id="container">
    <div class="full_width clear">
      <div class="one_half first">
	  <table>
		  <tr>
			<th>Number</th>
			<th>Song</th>
			<th>Amount</th>
		  </tr>
		  <tr>
			<td>Nr. 1</td>
			<td>Stayin' Alive - Bee Gees</td>
			<!-- Here you fill in the php variables if you're using the real data ($result) -->
			<td>8</td>
		  </tr>
		  <tr>
			<td>Nr. 2</td>
			<td>Rythm of the Night - Corona</td>
			<td>7</td>
		  </tr>
		  <tr>
			<td>Nr. 3</td>
			<td>L'Amour Toujours - Gigi D'Agostino</td>
			<td>7</td>
		  </tr>
		  <tr>
			<td>Nr. 4</td>
			<td>Sweet Dreams - Eurythmics</td>
			<td>5</td>
		  </tr>
		  <tr>
			<td>Nr. 5</td>
			<td>You Spin Me Round - Dead or Alive</td>
			<td>4</td>
		  </tr>
		</table>
	  </div>
    </div>
  </div>
</div>

<div class="wrapper row4">
  <footer id="footer" class="clear">
    <p class="fl_left">Sam Teerlinck - 1NMCT4</p>
  </footer>
</div>
</body>

<!--?php
$conn->close();
?-->

</html>