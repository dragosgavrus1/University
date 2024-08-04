<?php

include("config.php");

header('Content-Type: application/json; charset=UTF-8');
header("Access-Control-Allow-Origin: *");
header("Header Set Access-Control-Allow-Headers *");

function checkStudentCredentials($name, $password) {
    global $conn;
    // Query to check if the name and password match in the students table
    $query = "SELECT * FROM students WHERE name = '$name' AND password = '$password'";
    
    $result = mysqli_query($conn, $query);
    if ($result && mysqli_num_rows($result) > 0) {
        $row = mysqli_fetch_array($result);
        $studentId = $row['id'];

        session_start();
        $_SESSION['student_id'] = $studentId;

        // Return JSON response indicating successful login as student
        echo json_encode(array("userType" => "student", "studentId" => $studentId));

        exit();
    } 
    
}

function checkTeacherCredentials($name, $password) {
    global $conn;
    // Query to check if the name and password match in the teachers table
    $query = "SELECT * FROM teacher WHERE name = '$name' AND password = '$password'";
    
    $result = mysqli_query($conn, $query);
    
    if ($result && mysqli_num_rows($result) > 0) {
        // Return JSON response indicating successful login as teacher
        echo json_encode(array("userType" => "teacher"));

    } else {
        // Return JSON response indicating invalid credentials
        echo json_encode(array("error" => "Invalid credentials"));
    }
    
}

$name = $_POST['name'];
$password = $_POST['password'];

// Check student credentials
checkStudentCredentials($name, $password);

// Check teacher credentials
checkTeacherCredentials($name, $password);

?>
