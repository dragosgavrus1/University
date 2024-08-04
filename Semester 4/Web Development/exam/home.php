<?php

    require 'actions/action_get_all.php';

    session_start();
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>

<style>
    .entity {
        border: 1px solid black;
        padding: 10px;
        margin: 10px;
    }

    .entity:hover {
        background-color: #eee;
        cursor: pointer;
    }
</style>

<body>
    <?php 
        echo "<h2>Welcome, " . $_SESSION["username"] . "!</h2>" . $_SESSION["city"] ." ". $_SESSION["date"] . " " . $_SESSION["reservationIds"] ;
    ?>

    <button onclick="window.location.href = 'hotels.php';">View Hotels</button>
    <button onclick="window.location.href = 'flights.php';">View Flights</button>
    <button onclick="window.location.href = 'actions/cancel_reservations.php';">Cancel All Reservations</button>
</body>
