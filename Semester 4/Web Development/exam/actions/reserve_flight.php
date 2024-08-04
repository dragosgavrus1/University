<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $flightID = $_POST['flightID'];
    reserveFlight($flightID);
}

function reserveFlight($flightID) {
    require "config.php";

    $type = 'Flight';
    $username = $_SESSION["username"];
    $query = "INSERT INTO reservations (person, type, idReservedResource) VALUES ('$username', '$type', '$flightID')";
    mysqli_query($conn, $query);

    $reservationId = mysqli_insert_id($conn);
    $_SESSION["reservationIds"] .= "," . $reservationId;

    $updateQuery = "UPDATE flights SET availableSeats = availableSeats - 1 WHERE flightID = '$flightID'";
    mysqli_query($conn, $updateQuery);

    header("Location: ../home.php");
    exit();
}
?>
