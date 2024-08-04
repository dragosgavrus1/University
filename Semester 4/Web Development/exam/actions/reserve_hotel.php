<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $hotelID = $_POST['hotelID'];
    reserveHotel($hotelID);
}

function reserveHotel($hotelID) {
    require "config.php";

    $type = 'Hotel';
    $username = $_SESSION["username"];
    $query = "INSERT INTO reservations (person, type, idReservedResource) VALUES ('$username', '$type', '$hotelID')";
    mysqli_query($conn, $query);

    $reservationId = mysqli_insert_id($conn);
    $_SESSION["reservationIds"] .= "," .  $reservationId;

    $updateQuery = "UPDATE hotels SET availableRooms = availableRooms - 1 WHERE hotelID = '$hotelID'";
    mysqli_query($conn, $updateQuery);

    header("Location: ../home.php");
    exit();
}
?>
