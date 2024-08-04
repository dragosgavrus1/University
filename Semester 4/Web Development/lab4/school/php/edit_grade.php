<?php
include("config.php");

header('Content-Type: application/json; charset=UTF-8');
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Content-Type");
header("Access-Control-Allow-Methods: POST, OPTIONS");

if ($_SERVER["REQUEST_METHOD"] === "OPTIONS") {
    http_response_code(200); // OK
    exit();
}

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] != "POST") {
    header("HTTP/1.1 405 Method Not Allowed");
    http_response_code(405);
    exit();
}

// Decode JSON data from the request body
$json_data = json_decode(file_get_contents('php://input'), true);

// Retrieve the parameters from the JSON data
$grade_id = $json_data['grade_id'];
$grade = $json_data['grade'];
$course = $json_data['course'];

// Prepare and execute SQL query to update the grade in the database
$sql = "UPDATE Grades SET grade = ?, course = ? WHERE grade_id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("isi", $grade, $course, $grade_id);

if ($stmt->execute()) {
    // Grade updated successfully
    http_response_code(200); // OK
    echo json_encode(array("message" => "Grade updated successfully"));
} else {
    // Failed to update grade
    http_response_code(500); // Internal Server Error
    echo json_encode(array("error" => "Failed to update grade"));
}

$stmt->close();
$conn->close();
?>
