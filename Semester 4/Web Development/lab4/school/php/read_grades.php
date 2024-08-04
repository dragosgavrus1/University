<?php
include("config.php");

header('Content-Type: application/json; charset=UTF-8');
header("Access-Control-Allow-Origin: *");

// Check if the request method is GET
if ($_SERVER["REQUEST_METHOD"] != "GET") {
    header("HTTP/1.1 405 Method Not Allowed");
    http_response_code(405);
    exit();
}

// Check if the student ID is provided in the query string
if (!isset($_GET['student_id'])) {
    header("HTTP/1.1 400 Bad Request");
    http_response_code(400);
    echo json_encode(array("error" => "Student ID is required"));
    exit();
}

// Retrieve the student ID from the query string
$student_id = $_GET['student_id'];

// Prepare and execute SQL query to retrieve grades for the specified student
$sql = "SELECT * FROM Grades WHERE student_id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $student_id);
$stmt->execute();
$result = $stmt->get_result();
$data = [];
while ($row = $result->fetch_assoc()) {
    $data[] = $row;
}
$stmt->free_result();
$stmt->close();
$conn->close();

// Return the retrieved data as JSON response
echo json_encode($data);
http_response_code(200);
exit();
?>
