<?php

    $db_url = "127.0.0.1:3306";
    $db_username = "root";
    $db_name = "reservations";
    $db_password = "";

    // connect to the database
    $conn = mysqli_connect($db_url, $db_username, $db_password, $db_name);
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
    
    header("Access-Control-Allow-Origin: *");
    header("Access-Control-Allow-Methods: POST");
    header("Access-Control-Allow-Headers: Content-Type");

    // start the session if not already started
    if (!isset($_SESSION['username'])) session_start();
?>

