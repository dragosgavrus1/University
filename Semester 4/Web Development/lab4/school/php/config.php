<?php
$env = parse_ini_file('.env');

$host = $env["DB_HOST"];
$user = $env["DB_USER"]; // Changed from DB_USERNAME
$password = $env["DB_PASS"]; // Changed from DB_PASSWORD
$database = $env["DB_NAME"];


try {
    $conn = mysqli_connect($host, $user, $password, $database);
    if (!$conn) {
        throw new Exception("Failed to connect to MySQL: " . mysqli_connect_error());
    }


} catch (Exception $e) {
    echo $e->getMessage();
}

