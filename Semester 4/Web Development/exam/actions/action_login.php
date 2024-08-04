<?php
    require "config.php";

    $username = $_POST["username"];
    $city = $_POST["destination-city"];
    $date = $_POST["date"];

    // set the session and redirect to the home page
    $_SESSION["username"] = $username;
    $_SESSION["city"] = $city;
    $_SESSION["date"] = $date;

    header("Location: ../home.php");
?>