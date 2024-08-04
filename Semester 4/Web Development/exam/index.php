<?php
  require 'actions/config.php';

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login</title>
</head>
<body>

  <h1>Login</h1>
  
  <?php
    if (isset($_GET["error"])) {
      echo "<h4>Error: " . $_GET["error"] . "</h4>";
    }
    $_SESSION["username"] = "";
    $_SESSION["city"] = "";
    $_SESSION["date"] = "";
    $_SESSION["reservationIds"] = "";
  ?>

  <form action="actions/action_login.php" method="post">
    <input type="text" name="username" placeholder="username">
    <input type="text" name="destination-city" placeholder="destination city">
    <input type="date" name="date" placeholder="date">
    <input type="submit" value="Begin Reservation">
  </form>

</body>
</html>