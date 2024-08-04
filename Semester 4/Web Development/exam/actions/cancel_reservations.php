<?php
require "config.php";

if (isset($_SESSION['reservationIds'])) {
    $reservationIds = $_SESSION['reservationIds'];

    $sql = "DELETE FROM reservations WHERE id IN (" . $reservationIds . ")";
    mysqli_query($conn, $sql);

    $_SESSION['reservationIds'] = "";

    
} else {
    echo "No reservation IDs found in the session";
}

header("Location: ../home.php");
?>